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

class QuestionType:
    FRQ = 0
    MCQ = 1

class Question:
    term = ""
    definition = ""
    wrongAnswers = [] # Only for MCQ
    answers_count = 4 # Only for MCQ
    answer_check = lambda a, b : a == b # Only for FRQ
    question_type = QuestionType.MCQ
    reinforcements_needed = 3
    def MCQ(term, definition, wrongAnswers, answer_count = 4, reinforcements_needed = 3):
        return Question(term, definition, QuestionType.MCQ, answer_count, wrongAnswers, reinforcements_needed)

    def FRQ(term, definition, answer_check = lambda a, b : a == b, reinforcements_needed = 3):
        return Question(term, definition, QuestionType.FRQ, answer_check = answer_check, reinforcements_needed = reinforcements_needed)

    def __init__(self, term, definition, questiontype, answer_count = 4, wrongAnswers=[], answer_check=lambda a, b : a == b, reinforcements_needed=3):
        self.term = term
        self.definition = definition
        self.question_type = questiontype
        self.wrongAnswers = wrongAnswers
        self.answer_check = answer_check
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
    def __init__(self, questions, fn):
        self.questions = questions
        self.fn = fn

    def __del__(self):
        if self.fn is not None and self.do_save:
            with open("__"+self.fn+"_save__.py", "w") as f:
                f.write("s = " + str(self.question_scores) + "\n")

    def add(self, question):
        self.questions.append(question)

    def run(self):
        print("Type \"Override\" at any point to make your answer to the last question correct.")
        print("(The purpose of this program is to help you learn, not to test you, so discounting.")
        print("certain mistakes is up to you. However, it's not recommended to override unless")
        print("there was actually a good reason.)")
        print("Type \"Quit or Q\" at any point to quit the game, and save your progress")
        self.question_scores = [0 for i in self.questions]
        if os.path.isfile(self.fn+".txt"):
            print("It looks like you weren't done... would you like to attempt to continue where you left off (load scores from file)?")
            answer = input("Y/R/G (Yes / Restart / Guest Session): ").lower().strip()
            if answer == "y":
                temp = importlib.import_module("__"+self.fn+"_save__").s
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
            if self.question_scores[self.questions.index(question)] == question.reinforcements_needed:
                continue #TODO: Improve this
            questions_cache.append(question)
            if question.question_type == QuestionType.FRQ:
                answer = input(question.term+": ")
                if answer.lower().strip() == "quit" or answer.lower().strip() == "q":
                    return
                elif answer.lower().strip() == "override":
                    self.question_scores[questions_cache[-2]] += 2
                    print("Overrided")
                if question.answer_check(answer, question.definition):
                    self.question_scores[self.questions.index(question)] += 1
                    if self.question_scores[self.questions.index(question)] == question.reinforcements_needed:
                        print("You have mastered " + question.term + ", with {} points".format(question.reinforcements_needed))
                else:
                    print("Incorrect, it was: " + question.definition)
                    self.question_scores[self.questions.index(question)] -= 1
            elif question.question_type == QuestionType.MCQ:
                answers = random.sample(question.wrongAnswers, self.questions.answer_count - 1)
                answers.append(question.definition)
                random.shuffle(answers)
                answer = answers.find(question.definition)
                print("A: " + answers[0])
                print("B: " + answers[1])
                print("C: " + answers[2])
                print("D: " + answers[3])
                answer = input("Answer: ")
                if answer.lower().strip() == "quit":
                    return
                elif answer.lower().strip() == "override":
                    self.question_scores[questions_cache[-2]] += 2
                    print("Overrided")
                if question.answer_check(answer, question.definition):
                    self.question_scores[self.questions.index(question)] += 1
                    if self.question_scores[self.questions.index(question)] == question.reinforcements_needed:
                        print("You have mastered " + question.term + ", with {} points".format(question.reinforcements_needed))
                else:
                    self.question_scores[self.questions.index(question)] -= 1
                    print("Incorrect, it was: " + question.definition)
        # print("Score: " + str(score) + "/" + str(len(questions))