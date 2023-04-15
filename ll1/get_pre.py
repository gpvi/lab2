#encoding=utf-8
"""
@FileName：get_pre.py\n
@Description：\n
@Author：NZQ\n
@Time：2023/4/7 10:43\n
"""
import sys

import numpy as np

from get_first_s import FirstS
import pandas as pd
import numpy
class PreTbl(FirstS):
    def __init__(self):
        super(PreTbl, self).__init__()
        self.len_row = len(self.no_term)
        self.len_columns = len(self.input_set)
        self.columns = self.input_set.copy()
        self.columns.add('$')
        self.val_list = [['-1']*(self.len_columns+1) for _ in range(self.len_row)]
        self.val_array = np.array(self.val_list)
        self.pre_table = pd.DataFrame(self.val_array,index=list(self.no_term),columns=list(self.columns))
        self.pre_tbl_create()
    def init_pre_table(self):
        row_name = []
        # print(self.columns)
        # print(self.pre_table.columns)
        # print(self.input_set)
        # print(self.pre_table)
    def add_content(self):
        select_set = self.first_s_set_list
        # print(len(select_set))
        for i in range(len(select_set)):
            r = select_set[i][0]
            # print('i')
            for s in select_set[i][1]:
                # print(r," ",s)
                if self.pre_table.loc[r,s] != '-1':
                    print(r," ",s," ",self.pre_table.loc[r,s]," ",i,file=sys.stderr)
                    # print()
                self.pre_table.loc[r, s] = str(i)
    def pre_tbl_create(self):
        self.add_content()
        # print(pre.no_term)
        # print(pre.input_set)
        self.init_pre_table()
if __name__ == '__main__':

    pre =PreTbl()
