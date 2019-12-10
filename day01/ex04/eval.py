#!/usr/bin/env python3
# -*-coding:utf-8 -*

class Evaluator:

    def zip_evaluate(cls, coefs, words):
        if len(coefs) != len(words):
            return -1
        return sum([coef * len(word) for coef, word in zip(coefs, words)])

    def enumerate_evaluate(cls, coefs, words):
        if len(coefs) != len(words):
            return -1
        return sum([coef * len(words[index]) for index, coef in enumerate(coefs)])

    zip_evaluate = classmethod(zip_evaluate)
    enumerate_evaluate = classmethod(enumerate_evaluate)

if __name__ == '__main__':
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    result = Evaluator.zip_evaluate(coefs, words)
    print(f"Evaluator.zip_evaluate(coefs, words) = {result}")

    words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    result = Evaluator.zip_evaluate(coefs, words)
    print(f"Evaluator.zip_evaluate(coefs, words) = {result}")

    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    result = Evaluator.enumerate_evaluate(coefs, words)
    print(f"Evaluator.enumerate_evaluate(coefs) = {result}")

    words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    result = Evaluator.enumerate_evaluate(coefs, words)
    print(f"Evaluator.enumerate_evaluate(coefs) = {result}")
