# coding=utf-8
# path = './lr_sentence.txt'

from  get_first import  FirstSet as fs
from get_follow import FollowSet
class FirstSet:

    def __init__(self):
        self.path = './lr_sentence.txt'
        self.first = {}
        self. sentences = {}
        self.no_term = set()
        self.create_first()
        self.empty_str = 'ε'
        self.input_term = set()
        self.get_input_term()
    def read_sentence(self):
        path = self.path

        sentences = self.sentences

        with open(path ,'r' ,encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                temp = line.split('@')
                temp[1] = temp[1].strip('\n')
                temp[1] = temp[1].split()
                # temp[1] = list(filter(lambda x: x != "",temp[1]))
                # print(temp[1])
                if temp[0] not in sentences:
                    sentences[temp[0]] = []
                    sentences[temp[0]].append(temp[1])
                else:
                    sentences[temp[0]].append(temp[1])
        no_term = self.no_term
        for i in sentences.items():
            no_term.add(i[0])

    def create_first(self):
    # sentences 字典
        self.read_sentence()
        count = 0
        first = self.first
        flag = 0
        sentences = self.sentences
        no_term = self.no_term
        while flag == 0:
            flag = 1
            for i in sentences.items():
                term_sentences = i[1][:]
                if i[0] not in first:
                    first[i[0]] = set()
                for sentence in term_sentences:
                    k = 0
                    while sentence[k] == i[0]:
                        k += 1
                    term = sentence[k]
                    if term not in no_term:
                        if term not in first[i[0]]:
                            first[i[0]].add(term)
                            flag = 0
                    else:
                        if term not in first:
                            continue
                        else:
                            first[i[0]] = first[i[0]].union(first[term])
    def get_input_term(self):
        for i in self.sentences.items():
            for j in i[1]:
                if j[0] not in self.no_term and j[0] != self.empty_str:
                    self.input_term.add(j[0])
    


if __name__ == '__main__':
    first = FirstSet()
    first.create_first()
