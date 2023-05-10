# coding=utf-8
# 数据结构
import os.path
import sys
from copy import deepcopy
# from get_first import FirstSet
from get_follow import FollowSet
import pandas as pd
import numpy as np
from newfirst import FirstSet

first = FirstSet()
follow = FollowSet()
# first_set = first.first_set
first_set = first.first
follow_set = follow.follow_set
sentence = first.sentences

# for i in sentence.items():
#     print(i[0])
#     for k in i[1]:
#         print(k)
#     print("----------------")
t = ['program\''+"@"+' program']
for i in sentence.items():
    for j in i[1]:
        temp = i[0] + '@'
        for n in j:
              temp += " "+n
        t.append(temp)

sentence_table = {}
co = 0
for i in t:
    sentence_table[i] = co
    co += 1
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
            s += i + " "
        s += "#" + self.end + " # "
        s += str(self.n_p)
        self.sentence_for_hash = s
    # 转为原来的语句，类型为string
    def to_origin_sentence(self):
        emp = self.left
        emp += "@"
        for i in self.right:
            emp += " " + i
        return emp
    # 转为HashTable
    def to_dic(self):
        right = "right"
        left = "left"
        next = "end"
        n_p = "n_p"
        self.dic = {left: self.left, right: self.right, next: self.end, n_p: self.n_p}
    # n_p加一 ，相当于 圆点向前移动一格
    def count(self):
        self.n_p += 1
        self.to_dic()
        self.get_sentence()
    # 重写生成式哈希 用于 比较 是否相同
    def __eq__(self, other):
        return self.sentence_for_hash == other.sentence_for_hash

    def __hash__(self):
        return hash(self.sentence_for_hash)
# 单个状态/项目
class SetI:
    """

    """
    def __init__(self, I: list):
        self.index = 0
        # 项目集，其中内容为生成式，确保各个生成式在此项目集的唯一性 采用数据结构 -- list
        self.contain = I
        self.sentences = []
        self.hash_sentence = ""
        self.goto_ch = {}
        self.get_sentences()
        self.from_set = -1
        self.by_ch = ""
        self.goto_table = {}

    def add_goto(self, x, next_setI):
        if x not in self.goto_ch:
            self.goto_ch[x] = next_setI

    def get_sentences(self):
        ts = ""
        for i in self.contain:
            self.sentences.append(i.sentence_for_hash)
            ts += i.sentence_for_hash
        self.hash_sentence = ts
    # 重写哈希 用于比较状态是否相同
    def __eq__(self, other):
        return self.hash_sentence == other.hash_sentence

    def __hash__(self):
        return hash(self.hash_sentence)

    def __lt__(self, other):
        if self.index <= other.index:
            return True
        else:
            return False
# 项目集
class CSet:
    """
    count:状态数目计数
    contain:set类型 元素未 SetI 单个项目
    dic:Hash table 项目集: index #index 为 int 类型
    sort_list = 排序后的项目集
    """
    def __init__(self):
        self.count = -1
        self.contain = set()
        self.dic = {}
        self.sorted_list = []
        # self.reduce_t = set()

    def add(self, x: SetI):
        self.count += 1
        x.index = self.count
        self.contain.add(x)

    def set_to_index(self):
        for i in self.contain:
            self.dic[i] = i.index

    def sortedc(self):
        self.sorted_list = sorted(list(self.contain))


# sub_function 求闭包，输入为项目
def closure(cur_set: SetI):
    I = cur_set.contain
    # 下一个要读的字符 相同句子 放在 同一个set()，next_ch_table键为下一个要读的字符，值为set
    next_ch_table = {}
    flag = 0
    J = I.copy()
    while flag == 0:
        flag = 1
        # 拷贝 集合 用于求闭包，与原来的对比是否有变化，有变化flag = 0,无变化flag = 1
        T = J.copy()
        for i in iter(T):
            # 处理未到终结状态的生成式
            if i.n_p < len(i.right):
                # 点在n_p前，next_term 为点后第一个字符
                next_term = i.right[i.n_p]
                # 收集 添加下一个字符相同的句子
                if i.right[i.n_p] not in next_ch_table:
                    next_ch_table[i.right[i.n_p]] = set()
                    next_ch_table[i.right[i.n_p]].add(i)
                else:
                    next_ch_table[i.right[i.n_p]].add(i)

                # 下一个字符为 非终结符
                # 应该使用 first(βa)
                # 求闭包关键程序，
#-------------------------------------------------------------------------
                if next_term in first.no_term:
                    # 设定前看符号 last_c,
                    last_c = ""
                    # 下一个字符为非终结符，且该非终结符为该句的最后一个字符
                    # 以该字符扩展出来得到生成式的，前看符继承先前句子的字符
                    # 否则 
                    if i.n_p + 1 == i.l_right:
                        last_c = i.end
                    else:
                        last_c = i.right[i.n_p + 1]
                    

                    left = next_term
                    right = list(sentence[left])
                    for k in right:
                        if k[0] != 'ε':
                            new_g = GSentence(left, k, last_c)
                            if new_g not in J:
                                flag = 0
                                J.append(new_g)
#--------------------------------------------------------------------------                                
    I = J
    cur_set.goto_ch = next_ch_table
    cur_set.contain = J
    return cur_set

#遇到字符执行状态跳转行为
def goto(cur_set: SetI, x: str):
    cur_list = cur_set.contain
    j = []
    if len(cur_set.goto_ch) == 0:
        return 0
    # cur_list 为 GSentence 列表
    for i in iter(cur_set.goto_ch[x]):
        # for each item
        if i.n_p < i.l_right:
            if i.right[i.n_p] == x:
                t = deepcopy(i)
                t.count()
                j.append(t)

    if len(j) == 0:
        return 1
    else:
        temp = SetI(j)
        new_set = temp
    return closure(new_set)


# 求解全部状态
def items(g):
    C = CSet()
    init_g = GSentence('program\'', ['program'], '$')
    init_I = SetI([init_g])
    init_I = closure(init_I)
    C.add(init_I)
    flag = 0
    already_clu = []
    already_goto = []
    already_clu.append(0)
    while flag == 0:
        flag = 1
        # print(C.count)
        contain1 = C.contain
        contain2 = contain1.copy()
        for i in iter(contain2):

            # i type is class SetI
            if i.index in already_goto:
                continue
            already_goto.append(i.index)
            for ch in i.goto_ch:
                t = goto(i, ch)
                if type(t) != int:
                    temp_set = t
                    if temp_set not in C.contain:
                        temp_set.from_set = i.index
                        temp_set.by_ch = ch
                        # print(temp_set.index)
                        if ch not in i.goto_table:
                            i.goto_table[ch] = set()
                            i.goto_table[ch].add(temp_set)
                        else:
                            i.goto_table[ch].add(temp_set)
                        C.add(temp_set)
                        flag = 0
                    else:
                        for j in iter(C.contain):
                            if j == temp_set:
                                if ch not in i.goto_table:
                                    i.goto_table[ch] = set()
                                    i.goto_table[ch].add(temp_set)
                                else:
                                    i.goto_table[ch].add(temp_set)
    return C


def get_set():
    g = CSet()
    g = items(g)
    g.set_to_index()
    g.sortedc()

# # 测试代码
#     for i in g.sorted_list:
#         print("序号:",i.index)
#         for j in i.contain:
#             print(j.sentence_for_hash)
#             # a = j.to_origin_sentence()
#             # if a in t:
#             #     print("True",sentence_table[a])
#             # else:
#             #     print('False',a,file=sys.stderr)
#             #     sys.exit(0)
#         print("--------------------------")

    return g

# DataFrame 类型 纵列 状态index,行：非终结符 +$
def init_action_table():
    ch = list(follow.input_set)
    ch.append("$")
    # ch_no_term = list(first.no_term)
    # ch = ch +ch_no_term
    ch.sort()
    # print(ch)
    # get_set()
    index = [i for i in range(0, 244)]
    temp = np.zeros((244, len(ch)), dtype="str")
    df = pd.DataFrame(temp, index=index, columns=ch)
    # print(df)
    return df

# DataFrame 类型 纵列 状态index,行：终结符
def init_goto_table():
    ch = list(first.no_term)
    ch.sort()
    index = [i for i in range(0, 244)]
    temp = np.zeros((244, len(ch)), dtype="str")
    df = pd.DataFrame(temp, index=index, columns=ch)
    return df

# 填写ACTION 和 GOTO
def start():
    states = get_set()
    # for i in states.sorted_list:
    #     print(i.index)
    table_action = init_action_table()
    table_goto = init_goto_table()
    states.set_to_index()
    # for i in states.contain:
    for i in states.sorted_list:
        # goto table : 
        # 由此状态出发 到达的 状态
        # index 当前状态
        dic = i.goto_table
        index = i.index
        for j in dic.items():
            ch = j[0]
            t = list(j[1])
            next_I = t[0]
            val = states.dic[next_I]
            if ch not in first.no_term:
                table_action.loc[index,ch] = 's'+str(val)
            else:
                table_goto.loc[index,ch] =  str(val)
        # contain 中为此状态下的所有生成式
        for j in i.contain:
            # j is a GSentence
            if j.n_p == len(j.right) and j.left != 'program\'':
                s = j.to_origin_sentence()
                table_action.loc[index,j.end] = 'r'+str(sentence_table[s])

        table_action.loc[1,'$'] = 'acc'
        

    return table_action,table_goto


def test():
    g = GSentence('program\'', ['program'], '$')
    s = SetI([g])
    closure(s)


if __name__ == '__main__':

    # pass
    # get_set()
    # test()
    # for i in sentence.items():
    #     print(i)



    action,goto = start()
    # print(action.index)
    action.to_csv('action.csv')
    goto.to_csv('goto.csv')

    # if not os.path.exists('.\\no_term.txt'):
    #     with open('.\\no_term.txt','w') as f:
    #         for i in iter(first.no_term):
    #             t = i+"\n"
    #             f.write(t)
    # if not os.path.exists('.\\res_sentence.txt'):
    #     with open('.\\res_sentence.txt','w') as f:
    #         for i in t:
    #             # print(i)
    #             kt = i + "\n"
    #             f.write(kt)

    # # print(first.first_set)
    # # print(first.no_term)
