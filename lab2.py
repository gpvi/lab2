# coding=utf-8
# 数据结构
import sys

from get_first import FirstSet
from get_follow import FollowSet

first = FirstSet()
follow = FollowSet()

first_set = first.first_set
follow_set = follow.follow_set
sentence = first.sentence


class GSentence:
    def __init__(self, l: str, r: list, n: str):
        self.left = l
        self.right = r
        self.end = n
        self.n_p = 0
        self.sentence_for_hash = None
        self.dic = None
        self.get_sentence()
        self.to_dic()
        self.l_right = len(self.right)

    def get_sentence(self):
        s = self.left
        s += " @ "
        for i in self.right:
            s += i + " " + ","
        s += self.end + " , "
        s += str(self.n_p)
        self.sentence_for_hash = s

    def to_dic(self):
        right = "right"
        left = "left"
        next = "end"
        n_p = "n_p"
        self.dic = {left: self.left, right: self.right, next: self.end, n_p: self.n_p}

    def __eq__(self, other):
        return self.sentence_for_hash == other.sentence_for_hash

    def __hash__(self):
        return hash(self.sentence_for_hash)


class Set_I:
    def __init__(self, I: list):
        self.index = 0
        # 项目集，其中内容为生成式，确保各个生成式在此项目集的唯一性 采用数据结构 -- list
        self.contain = I
        self.sentences = []
        self.hash_sentence = ""

    def get_sentences(self):
        ts = ""
        for i in self.contain:
            self.sentences.append(i.sentence_for_hash)
            ts += i.sentence_for_hash
        self.hash_sentence = ts

    def __eq__(self, other):
        return self.hash_sentence == other.hash_sentence

    def __hash__(self):
        return self.hash_sentence


# sub_function
# 求闭包
def closure(I: list):
    flag = 0
    J = I.copy()
    while flag == 0:
        flag = 1
        T = J.copy()
        for i in iter(T):
            if i.n_p < len(i.right):
                next_term = i.right[i.n_p]
                if next_term in first.no_term:
                    # 设定前看符号 last
                    last_c = ""
                    if i.n_p + 1 == i.l_right:
                        last_c = i.end
                    elif i.right[i.n_p + 1] not in next_term:
                        last_c = i.right[i.n_p + 1]
                    else:
                        print("error,two no_term", file=sys.stderr)

                    left = next_term
                    right = list(sentence[left])
                    for k in right:
                        if k[0] != 'ε':
                            new_g = GSentence(left, k, last_c)
                            if new_g not in I:
                                J.append(new_g)
    I = J


def goto(cur_list: list, c: set):
    pass


if __name__ == '__main__':
    # # pass
    l = {1: [1, 2, 3]}
    s = set()
    s.add(l)
    # # for i in first_set.items():
    # #     for j in i[1]:
    # #         print(j)
    # #     print("---------------")
    # # print(first_set['program'])
    # # right = list(first_set['program'])
    # # print(right)
    # # for i in sentence.items():
    # #     print(i[1])
    # a = G_sentence('1','2','3')
    # b = G_sentence('1','5','3')
    #
    # p = [G_sentence('1','2','3'), G_sentence('1','5','3')]
    # l = []
    # l.append(a)
    # l.append(b)
    #
    # c = G_sentence('2','2','3')
    # d = G_sentence('3','5','3')
    #
    # ll = [c,d]
    #
    # print(p == l)
    # c = G_sentence('1','2','3')
    # if c in l:
    #     print(2556)
    # g = G_sentence('program\'',['program'],'$')
