import os

from get_follow import FollowSet,FirstSet


class FirstS(FollowSet):

    def __init__(self):
        super(FirstS, self).__init__()
        self.first_s_set = {}
        self.first_s_set_list = []
        self.init_first_s()
        self.compute_firsts()

    def init_first_s(self):
        count = 0
        for i in self.no_term_list:
            self.first_s_set[count] = set()
            count += 1
    def select_to_txt(self,path = "select.txt"):

        if not os.path.exists(path):
            with open(path,'w') as f:
                for i in self.first_s_set_list:
                    temp_s = i[0]+" @ "
                    for j in i[1]:
                        temp_s += j+" "
                    temp_s += '\n'
                    f.write(temp_s)


    def compute_firsts(self):
        l = self.first_s_set_list

        count = -1
        firsts_set = self.first_s_set
        for s in self.sentence.items():
            # print(s)
            lt = s[0]
            right_sentences = s[1]
            for sub_s in right_sentences:
                count += 1
                # print(sub_s)
                head = lt
                f = True
                sub_s = list(filter(lambda x:x!=self.empty_str,sub_s))
                # print(sub_s)
                for j in range(len(sub_s)):
                    ts = sub_s[j]
                    if ts != self.empty_str:
                        if ts in self.input_set:
                            firsts_set[count].add(ts)

                            l.append ([head,list(firsts_set[count])])
                            f = False

                            break
                        if ts in self.no_term:
                            tt= self.first_set[ts].copy()
                            tt.discard(self.empty_str)
                            firsts_set[count] = firsts_set[count] | tt
                            if self.empty_str not in self.first_set[ts]:
                                f = False
                                l.append ([head,list(firsts_set[count])])
                                break

                if f and len(sub_s)>0:
                    firsts_set[count] = firsts_set[count] | self.follow_set[sub_s[len(sub_s)-1]]
                    l.append ([head,list(firsts_set[count])])


if __name__ == '__main__':
    firsts_set = FirstS()
    firsts_set.select_to_txt()
