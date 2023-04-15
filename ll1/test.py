"""
@FileName：test.py\n
@Description：\n
@Author：NZQ\n
@Time：2023/4/3 23:06\n
if ( a > b ) { a = b + 3.0 }
"""
import sys


arr = get_table.get_pre_table()
index_table = get_table.get_no_term_table()
head_table = get_table.get_input_table()
no_term_to_sentence ,index_to_sentence = get_table.get_g_sentence()
sentence_list = get_table.get_sentence_list()
# print(index_table)
# print(head_table)
# print(g_sentence)
# print(index_table)
no_term_set = set([i for i in index_table.keys()])
# print(no_term_set)
basic = ['int','char']
view_pre_table = get_table.get_view_pre_table()

def get_sentence_by_pd(cur_no_term,cur_char):
    # temp = view_pre_table[cur_no_term,cur_char]
    # print(cur_no_term,cur_char,'555555')
    if len(temp) == 0:
        return 'error'
    else:
        # print(view_pre_table.loc[cur_no_term,cur_char])
        val = view_pre_table.loc[cur_no_term,cur_char].split(" ")[:-1]
        a = list(filter (lambda x: x!="" ,val))
        # print(a)
        return a


def get_sentence(cur_no_term,cur_char):
    # print(cur_no_term,cur_char)
    r = index_table[cur_no_term]
    l = head_table[cur_char]
    # print(r,l)
    # print(r,l)
    index = arr[r,l]
    # print(index)
    # print(r,l)
    next_sentence = []
    if index != -1:
        next_sentence = sentence_list[index][1]
        # print(next_sentence)
        # print(next_sentence,"--------------")
    else:
        return "error"
    return  next_sentence

def judge(stack, token):
    pass

if __name__ == '__main__':

    token = get_input_test.input_arg()
    # print(type(token))
    stack = ['$','program']
    top = stack[-1]
    i = 0

    while i <len(token) or stack[-1] == '$':
        cur_token = token[i]

        # print(cur_token)
        while stack[-1]  in no_term_set:
            print(stack,end="       ")
            temp = stack.pop()
            # print(temp,cur_token)
            g_sentence = get_sentence_by_pd(temp,cur_token)
            print(i,"  ",token,end="       ")
            print(temp,"-->",g_sentence)

            if g_sentence == 'error':
                print('error', file=sys.stderr)
                sys.exit(0)
            print("*********************",g_sentence,"\n")
            if len(g_sentence) == 0:
                print('empty','stake[-1]:',stack[-1],'cur:',cur_token, file=sys.stderr)
                sys.exit(0)
            if g_sentence[0] == 'ε':
                continue
            if g_sentence == 'error':
                print('error',file=sys.stderr)
            else:
                while len(g_sentence) != 0:
                    stack.append(g_sentence.pop())


        if stack[-1] == cur_token:
            stack.pop()
            i += 1
        else:
            print('error token', file=sys.stderr)
            print("---------------------")
            print(stack)
            print(token, i)
            print(get_sentence_by_pd(temp,cur_token))
            print(stack[-1])
            print(stack[-1] in no_term_set)
            sys.exit(0)


