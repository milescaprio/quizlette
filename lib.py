from functools import reduce
import importlib
import random
import os

def nest(*fns):
    #Reduce(fun, seq, initial) calls fun of each pair of elements in seq; pushing to the left and moving the next one in
    #Here we are calling each function in fns as the sequence, so we need to manually feed the function into the function
    return lambda a : reduce(lambda x, y : y(x), fns, a)

def lowercased(a):
    return a.lower()

def stripped(a):
    return a.strip()

def filtered_equals(filter_fn):
    return lambda a, b : filter_fn(a) == filter_fn(b)

def save_filename(fn):
    return "__"+fn+"_save__.py"

def save_filename_extensionless(fn):
    return "__"+fn+"_save__"

class QuestionType:
    FRQ = 0
    MCQ = 1

class Question:
    term = ""
    definition = ""
    wrongAnswers = [] # Only for MCQ
    answer_count = 4 # Only for MCQ
    answer_check = lambda a, b : a == b # Only for FRQ
    question_type = QuestionType.MCQ
    reinforcements_needed = 3
    end_hint = None
    def MCQ(term, definition, wrongAnswers, answer_count = 4, reinforcements_needed = 3):
        return Question(term, definition, QuestionType.MCQ, answer_count, wrongAnswers, reinforcements_needed)

    def FRQ(term, definition, answer_check = lambda a, b : a == b, reinforcements_needed = 3, end_hint = None):
        return Question(term, definition, QuestionType.FRQ, answer_check = answer_check, reinforcements_needed = reinforcements_needed, end_hint = end_hint)

    def __init__(self, term, definition, questiontype, answer_count = 4, wrongAnswers=[], answer_check=lambda a, b : a == b, reinforcements_needed=3, end_hint = None):
        self.term = term
        self.definition = definition
        self.question_type = questiontype
        self.wrongAnswers = wrongAnswers
        self.answer_check = answer_check
        self.end_hint = end_hint
    def with_answer_check_function(self, answer_check):
        copy = self
        copy.answer_check = answer_check
        return copy
    def with_wrong_answers(self, wrongAnswers):
        copy = self
        copy.wrongAnswers = wrongAnswers
        return copy

class Game:
    questions = []
    fn = None
    question_scores = []
    do_save = True
    quit_keywords = ["Quit", "q"]
    override_keywords = ["Override", "o"]
    allow_overrides = True
    repeat_probability = lambda s, r : 0.0
    between_question_gap = "" #For double spacing
    #TODO make this interface and similar customizations
    #much more user friendly it's pretty much a hack at this point also I really hate lambdas
    worst_hole = -1
    def __init__(self, questions, fn, okeywords = ["Override", "o"], qkeywords = ["Quit", "q"], allow_overrides = True):
        self.questions = questions
        self.fn = fn
        self.override_keywords = okeywords
        self.allow_overrides = allow_overrides
        self.quit_keywords = qkeywords

    def cleanup(self):
        if self.fn is not None and self.do_save:
            with open(save_filename(self.fn), "w") as f:
                f.write("s = " + str(self.question_scores) + "\n")

    def add(self, question):
        self.questions.append(question)

    def mainloop(self):
        ostr = ""
        for o in self.override_keywords:
            ostr += '"' + o + '" or '
        ostr = ostr[:-4]
        qstr = ""
        for q in self.quit_keywords:
            qstr += '"' + q + '" or '
        qstr = qstr[:-4]
        if self.allow_overrides:
            print("Type " + ostr + " at any point to change your last answer to be correct.")
            print("(This program is to help you learn, not to test you. Your choice.)")
        print("Type " + qstr + " at any point to quit the game, and save your progress")
        self.question_scores = [0 for i in self.questions]
        if os.path.isfile(save_filename(self.fn)):
            print("It looks like you weren't done... would you like to attempt to continue where you left off (load scores from file)?")
            answer = input("Y/R/G (Yes / Restart / Guest Session): ").lower().strip()
            if answer == "y":
                temp = importlib.import_module(save_filename_extensionless(self.fn)).s
                if len(temp) == len(self.questions):
                    self.question_scores = temp
                else:
                    print("The save file is not compatible with the current question set. Starting over.")
            elif answer == "r":
                print("Restarting...")
            elif answer == "g": 
                print("Starting a guest session...")
                self.do_save = False
        questions_cache = []
        while True:
            question = random.choice(self.questions)
            if self.question_scores[self.questions.index(question)] >= question.reinforcements_needed:
                continue
                # Future: add better method for learning besides random question selection
            questions_cache.append(question)
            if question.question_type == QuestionType.FRQ:
                print(self.between_question_gap)
                answer = input(question.term+": ")
                if answer.lower().strip() in self.quit_keywords:
                    return
                elif answer.lower().strip() in self.override_keywords and self.allow_overrides:
                    self.question_scores[self.questions.index(questions_cache[-2])] += 2
                    print("Overrided")
                    if question.end_hint is not None: 
                        print("Correct! End hint:", question.end_hint)
                    if self.question_scores[self.questions.index(question)] == question.reinforcements_needed:
                        print("You have mastered " + question.term + ", with {} points".format(question.reinforcements_needed))
                    answer = input(question.term+": ")
                if question.answer_check(answer, question.definition):
                    self.question_scores[self.questions.index(question)] += 1
                    if question.end_hint is not None: 
                        print("Correct! End hint:", question.end_hint)
                    if self.question_scores[self.questions.index(question)] == question.reinforcements_needed:
                        print("You have mastered " + question.term + ", with {} points".format(question.reinforcements_needed))
                else:
                    print("Incorrect, it was: " + question.definition)
                    self.question_scores[self.questions.index(question)] -= 1
                    if self.question_scores[self.questions.index(question)] < self.worst_hole:
                        self.question_scores[self.questions.index(question)] = self.worst_hole
                    if self.repeat_probability(self.question_scores[self.questions.index(question)], question.reinforcements_needed) > random.random():
                        i = 0
                        a = input("Rewrite the answer: ")
                        while a != question.definition and i < 3:
                            a = input("Oops! Try again! Rewrite the answer: ")
                            if answer.lower().strip() in self.quit_keywords:
                                return
                            i+=1
                        if i >= 3:
                            print("Moving")
            elif question.question_type == QuestionType.MCQ:
                answers = random.sample(question.wrongAnswers, question.answer_count - 1)
                answers.append(question.definition)
                random.shuffle(answers)
                answer = answers.index(question.definition)
                print(self.between_question_gap)
                print(question.term + ": ")
                print("A: " + answers[0])
                print("B: " + answers[1])
                print("C: " + answers[2])
                print("D: " + answers[3])
                answer = input("Answer: ")
                if answer.lower().strip() in self.quit_keywords:
                    return
                elif answer.lower().strip() in self.override_keywords and self.allow_overrides:
                    self.question_scores[questions_cache[-2]] += 2
                    print("Overrided")
                    if self.question_scores[self.questions.index(question)] == question.reinforcements_needed:
                        print("You have mastered " + question.term + ", with {} points".format(question.reinforcements_needed))
                if answer.lower().strip() == "abcd"[answers.index(question.definition)]:
                    self.question_scores[self.questions.index(question)] += 1
                    if self.question_scores[self.questions.index(question)] == question.reinforcements_needed:
                        print("You have mastered " + question.term + ", with {} points".format(question.reinforcements_needed))
                else:
                    self.question_scores[self.questions.index(question)] -= 1
                    print("Incorrect, it was: " + question.definition)
                    if self.question_scores[self.questions.index(question)] < self.worst_hole:
                        self.question_scores[self.questions.index(question)] = self.worst_hole
    def run(self):
        self.mainloop()
        self.cleanup()