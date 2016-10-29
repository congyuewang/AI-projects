#!/usr/bin/env python
import sys
from KnowledgeBase import KnowledgeBase
from Sentence import Sentence

class main:
    @staticmethod
    def run():
        rules = []#rules store all the items
        file_name = "sample01.txt"


        with open(file_name) as f:
            goal = f.readline().strip()
            count = int(f.next().strip())#number of rules written at second line
            while count > 0:
                sentence = f.next().strip()
                rules.append(sentence)
                count -= 1
                

        f = open("output_01.txt", "w")
        if main.is_valid(goal, rules):
            for log in KnowledgeBase.logs:
                f.write(log + "\n")
            f.write("True")
        else:
            for log in KnowledgeBase.logs:
                f.write(log + "\n")
            f.write("False")

    @staticmethod
    def is_valid(goal, rules):
        knowledge_base = KnowledgeBase(map(Sentence.build_sentence, map(Sentence.parse, rules)))
        #print(rules)
        #print(map(Sentence.build_sentence, map(Sentence.parse, rules)))
        queries = goal.split("&&")
        results = []
        for query in queries:
            q = Sentence.build_sentence(Sentence.parse(query))
            flag = False
            for ans in knowledge_base.ask(q):
                flag = True
                break
            results.append(flag)

        for result in results:
            if not result:
                return False

        return True


if __name__ == '__main__':
    main.run()
