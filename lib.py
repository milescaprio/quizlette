from functools import reduce
import random

def nest(*fns):
    #reduce(fun, seq, initial) calls fun of each pair of elements in seq; pushing to the left and moving the next one in
    #Here we are calling each function in fns as the sequence, so we need to manually feed the function into the function
    return lambda a : reduce(lambda x, y : y(x), fns, a)
    def iter_fn(x, y, *args):
        for i in args:
            fns[i] = fns[i](fns[i+1])

def lowercased(a):
    return a.lower()

def stripped(a):
    return a.strip()

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
    def __init__(self, term, definition, questiontype, answer_count = 4, wrongAnswers=[], answer_check=lambda a, b : a == b):
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

def run_game(questions):
    question_scores = [0 for i in questions]
    while True:
        question = random.choice(questions)
        if question.question_type == QuestionType.FRQ:
            answer = input(question.term+": ")
            if question.answer_check(answer, question.definition):
                question_scores[questions.index(question)] += 1
            else:
                print("Incorrect, it was: " + question.definition)
                question_scores[questions.index(question)] -= 1
        elif question.question_type == QuestionType.MCQ:
            answers = random.sample(question.wrongAnswers, questions.answer_count - 1)
            answers.append(question.definition)
            random.shuffle(answers)
            answer = answers.find(question.definition)
            print("A: " + answers[0])
            print("B: " + answers[1])
            print("C: " + answers[2])
            print("D: " + answers[3])
            answer = input("Answer: ")
            if question.answer_check(answer, question.definition):
                question_scores[questions.index(question)] += 1
            else:
                question_scores[questions.index(question)] -= 1
                print("Incorrect, it was: " + question.definition)
    # print("Score: " + str(score) + "/" + str(len(questions))