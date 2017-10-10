import sys


class Sentence:
    def __init__(self, op, args=[]):
        self.op = op
        self.args = map(Sentence.build_sentence, args)

    def __hash__(self):
        return hash(self.op) ^ hash(tuple(self.args))

    def __repr__(self):
        if len(self.args) == 0:
            return self.op
        elif self.op not in ['&&', '=>']:
            args = str(self.args[0])
            if args[0].islower():
                args = '_'
            for arg in self.args[1:]:
                arg = str(arg)
                if arg[0].islower():
                    arg = '_'
                args = args + ', ' + arg
            return self.op + '(' + args + ')'
        else:
            if self.args[0].op in ['&&', '=>']:
                sentence = '(' + str(self.args[0]) + ')'
            else:
                sentence = str(self.args[0])
            sentence += ' ' + self.op + ' '

            if self.args[1].op in ['&&', '=>']:
                sentence += '(' + str(self.args[1]) + ')'
            else:
                sentence += str(self.args[1])
            return sentence

    def __eq__(self, other):
        return isinstance(other, Sentence) and self.op == other.op and self.args == other.args

    @staticmethod
    def build_sentence(element):
        if isinstance(element, Sentence):
            #print(element)
            return element

        if '=>' in element:
            pos = element.index('=>')
            left, right = element[0:pos], element[pos + 1:]
            expr = Sentence('=>', [left, right])
            #print(expr)
            return expr
        elif '&&' in element:
            pos = element.index('&&')
            first, second = element[0:pos], element[pos + 1:]
            expr = Sentence('&&', [first, second])
            return expr
        elif isinstance(element, str):
            return Sentence(element)

        if len(element) == 1:
            return Sentence.build_sentence(element[0])

        sentence = Sentence(element[0], element[1:][0])
        return sentence

    @staticmethod
    def parse(s):
        s = '(' + s + ')'
        s = s.replace('(', ' ( ')
        s = s.replace(')', ' ) ')
        s = s.replace(',', ' ')

        s = s.replace('&&', ' && ')
        s = s.replace('=>', ' => ')
        tokens = s.split()
        #print(Sentence.read_token_list(tokens))
        return Sentence.read_token_list(tokens)
    

    @staticmethod
    def read_token_list(tokens):
        first = tokens.pop(0)
        if first == '(':
            new_sentence = []
            while tokens[0] != ')':
                new_sentence.append(Sentence.read_token_list(tokens))
            tokens.pop(0)
            return new_sentence
        else:
            #print(first)
            return first
            

    @staticmethod
    def is_variable(element):
        return isinstance(element, Sentence) and element.op.islower() and element.args == []

