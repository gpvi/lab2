# coding=gbk
import os
import pandas
import numpy
from get_first import FirstSet



class FollowSet(FirstSet):

    def __init__(self):
        super().__init__()
        self.ch_stack = []
        self.follow_set = {}
        self.sorted_follow = {}
        self.create()
    def is_empty(self,container):
        return len(container) == 0

    def init_follow_set(self):
        no_term = self.no_term
        follow_set = self.follow_set
        for i in no_term:
            follow_set[i] = set()

        self.follow_set['program'].add('$')


    def _follow_set_to_txt(self,path='follow.txt'):
        res = self.sorted_follow
        if not os.path.exists(path):
            with open(path, 'w') as f:
                for i in res.items():
                    temp_str = i[0] + " ~~~~ "
                    for j in i[1]:
                        temp_str += j + " "
                    f.write(temp_str + "\n")


    def _follow_compute(self):
        f = False
        sentence = self.sentence
        follow_set = self.follow_set
        input_set = self.input_set
        no_term = self.no_term
        first_set = self.first_set
        empty_str = self.empty_str
        for s in sentence.items():
            right_sentences = s[1]
            # print(s[0])
            for sub_s in right_sentences:
                temp = follow_set[s[0]]
                for j in range(len(sub_s) - 1, -1, -1):
                    ts = sub_s[j]
                    if ts in input_set:
                        temp.add(ts)
                    if ts in no_term:
                        old_set = follow_set[ts]
                        follow_set[ts] = follow_set[ts] | temp
                        if old_set != follow_set[ts]:
                            f = True
                        tt = first_set[ts].copy()
                        tt.discard(empty_str)
                        if empty_str not in first_set[ts]:
                            temp = tt
                        else:
                            temp = temp | tt
        return f

    def create(self):
        self.init_follow_set()
        f = True
        while f:
            f = self._follow_compute()
        res = self.sorted_follow
        for i in self.no_term_list:
            p1 = i
            p2 = list(self.follow_set[i].copy())
            p2.sort()
            res[p1] = p2

        self._follow_set_to_txt()
if __name__ == '__main__':
    follow = FollowSet()
        # print(f)
    # follow_compute()
    # for i in follow_set.items():
    #     print(i)

    # print(first.no_term_list)


    # for i in res.items():
    #     print(i)
