# coding=utf-8
# 数据结构

from get_first import FirstSet
from get_follow import FollowSet

first = FirstSet()
follow = FollowSet()

first_set = first.first_set
follow_set = follow.follow_set


class G_sentence:
    def __init__(self,l:str,r:list,n:str):
        self.left  = l
        self.right  = r
        self.next  = n
        self.n_p = 0
        self.sentence_for_hash =None
        self.dic = None
        self.get_sentence()
        self.to_dic()

    def get_sentence(self):
        s = self.left
        s += " @ "
        for i in self.right:
            s += i+" "
        s += self.next+" , "
        s += str(self.n_p)
        self.sentence_for_hash = s

    def to_dic(self):
        right = "right"
        left = "left"
        next = "next"
        n_p = "n_p"
        self.dic = {left:self.left,right:self.right,next:self.next,n_p:self.n_p}

    def __eq__(self, other):
        return self.sentence_for_hash == other.sentence_for_hash

    def __hash__(self):
        return hash(self.sentence_for_hash)

class Set_I:
    def __init__(self):
        self.index = 0
        # 项目集，其中内容为生成式，确保各个生成式在此项目集的唯一性 采用数据结构 -- list
        self.contain = []
# sub_function
# 求闭包
def closure(I:set):
    flag = 0
    while flag == 0:
        flag = 1
        for i in iter(I):
            if i.n_p <len(i.right):
                next_term = i.right[i.n_p]
                if next_term in first.no_term:



if __name__ == '__main__':





