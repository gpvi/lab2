# encoding=utf-8
"""
@FileName：pre.py\n
@Description：\n
@Author：NZQ\n
@Time：2023/4/7 12:30\n
"""
import sys

from  get_pre import PreTbl


class Judge(PreTbl):
    def __init__(self):
        super(Judge, self).__init__()
        self.sentence_table = {}
        self.term_stack = []
        self.token_list = []
        self.basic = ['int','char']
    def get_input(self):
        self.token_list = input().split(" ")


    def in_stack(self,sentence:list):
        while len(sentence) != 0:
            self.term_stack.append(sentence.pop())

    def init_data(self):
        self.term_stack.append('$')
        self.term_stack.append('program')
        count = 0
        for i in self.sentence.items():
            for j in i[1]:
                self.sentence_table[count] = j
                count += 1
        # print(self.sentence_table)

    def judge_token(self):
        self.get_input()
        self.init_data()
        for i in self.token_list:
            cur_token = i
            if cur_token not in self.no_term and i != '$':
                # print(cur_token,"-----")
                if cur_token in self.basic:
                    cur_token = 'basic'
                elif cur_token.isdigit():
                    if '.' in cur_token:
                        cur_token = 'real'
                    else:
                        cur_token = 'num'
                else:
                    cur_token = 'id'
            while self.term_stack[-1] in self.no_term and  not (ch == '$' and cur_token == '$'):
                ch = self.term_stack.pop()
                index_num = self.pre_table.loc[ch,cur_token]
                if index_num == '-1':
                    print('error',file=sys.stderr)
                    return False
                in_stack_s = self.sentence_table[index_num]

                if in_stack_s[0] == self.empty_str:
                    continue
                self.in_stack(in_stack_s)


    def pre_to_csv(self,path="pre_table.csv"):
        self.pre_table.to_csv(path)




if __name__ == '__main__':

    judge = Judge()
    judge.init_data()
    # print(judge.sentence)
    # basic = ['int','char']
    # cur_token= ''
    # head_table = []
    #
    judge.pre_to_csv()
