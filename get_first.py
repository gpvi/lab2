# coding=utf-8
import os
'''
数据介绍
#  first_set dict(set:set)
#  first_set_sorted: dic(str:list)
#  no_term: 非终结符
#  input_char: 终结符
获取first集：
code:
first = FirstSet()
first_set = first.get_sorted_first_set()
'''
class FirstSet:
    def __init__(self):
        self.sentence = {}
        # sentence type : HashTable： ('program', [['block']])
        self.no_term = set()
        # 单个词汇
        self.no_term_list = []
        self.right_sub_term = set()
        self.input_set = set()
        self.first_set = {}
        self.first_set_sorted = {}
        self._create()
        self.empty_str = 'ε'
    def get_first_set(self):
        return self.first_set

    def get_sorted_first_set(self):
        return self.first_set_sorted

    def get_input(self):
        return self.input_set

    def get_no_term(self):
        return self.no_term
    def create_input_set(self):
        # print(self.right_sub_term)
        input_set = self.input_set
        for i in self.right_sub_term:
            if i not in self.no_term:
                input_set.add(i)

    def _create_no_term(self, sentence):
        no_term = self.no_term
        for i in sentence:
            # print(i)
            t = i[0][0]
            no_term.add(t)


    def _create_right_term_set(self, sentence):
        for i in sentence:
            for j in i[1]:
                self.right_sub_term.add(j)
        self.right_sub_term.remove("ε")

    def _get_dic_suport_first(self, sentence):
        dic = self.sentence
        for i in sentence:
            if i[0][0] not in dic:
                dic[i[0][0]] = [i[1]]
            else:
                dic[i[0][0]].append(i[1])
        return dic

    def _sort_first(self):
        for i in self.first_set.items():
            k = list(i[1]).copy()
            k.sort()
            self.first_set_sorted[i[0]] = k

    def _get_struct_sentence(self):
        sentence = []
        path = "./lr_sentence.txt"
        with open(path, 'r', encoding='utf-8') as f:
            strs = f.readlines()
            for s in strs:
                s = s.replace("\t", "")
                s = s.replace('.', "")
                s = s.replace('\n', "")
                s = list(filter(lambda x: not x.isdigit(), s))
                e_s = " "
                for i in s:
                    e_s += i
                new_s = e_s.split('@')
                try:
                    s2 = new_s[1].split(" ")
                except:
                    pass
                ss = list(filter(lambda x: x != "", s2))
                sentence.append([[new_s[0].replace(" ", "")], ss])
        sentence = sentence[:-1]
        self.no_term_list = [i[0][0] for i in sentence]
        if not os.path.exists('./sentence_for_set.txt'):
            with open('./sentence_for_set.txt', 'w') as f:
                for i in sentence:
                    temps = i[0][0] + "@"

                    t = i[1]
                    for j in t:
                        temps += j + " "
                    temps += '\n'
                    f.write(temps)
        return sentence


    def _get_res_first_set(self, ch):
        temp_first_set = ()
        first_set = self.first_set
        no_term = self.no_term
        ch_first = first_set[ch]
        temp_set = ch_first.copy()
        for i in temp_set:
            if i in no_term:
                ch_first = ch_first
        return ch_first

    def _add_first(self,dic_sentence):
        a = dic_sentence
        raw_first_term = self.first_set
        no_term = self.no_term
        first_set = self.first_set
        for t in a.items():
            i = t[1]
            first_term = [j[0] for j in i]  # 每个句子的第一项
            raw_first_term[t[0]] = set(first_term)

        for i in raw_first_term.items():
            ch_set = i[1].copy()
            for j in ch_set:
                if j in no_term:
                    first_set[i[0]] = first_set[i[0]]

        ###  核心运行函数
    def _create(self):
        sentence = self._get_struct_sentence()

        self._create_right_term_set(sentence)
        self._create_no_term(sentence)
        # self._create_input_set()
        dic_first = self._get_dic_suport_first(sentence)
        self.create_input_set()
        self._add_first(dic_first)
        self._sort_first()

    def first_set_to_txt(self,path = 'first.txt'):
        res = self.first_set_sorted
        if not os.path.exists(path):
            with open(path, 'w') as f:
                for i in res.items():
                    temp_str = i[0] + " ~~~~ "
                    for j in i[1]:
                        temp_str += j + " "
                    f.write(temp_str + "\n")

    def _test(self):
        for i in self.first_set.items():
            print(i[1])


if __name__ == '__main__':
    first = FirstSet()
    # first.first_set_to_txt()
    # print(type(first.sentence))
    # for i in first.sentence.items():
    #     print(i)
    for i in first.first_set.items():
        print(i)
