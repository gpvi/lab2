
import os
import sys

if __name__ == '__main__':

    path = ".\sentence2.txt"
    raw_l = []
    with open(path,'r') as f:
        k =f.readlines()

        for i in k:
            if i !=" ":
                temp = i.strip('\n').split('@')
                # print(temp)
                temp[0] = temp[0].strip(" ")
                raw_l.append(temp)
    # print(raw_l)
    k = {}
    for i in raw_l:
        right = i[1]
        temp = right.split("#")
        ktemp = []
        for j in temp:
            sub_temp = j.split(" ")
            news = list(filter(lambda x: x!="",sub_temp))
            ktemp.append(news)
        k[i[0]] = ktemp


    # for i in k.items():
    #     print(i)
    # #
    path2 = ".\lr_sentence.txt"
    with open(path2,'w',encoding= "utf-8") as f:
        for i in k.items():
            s = i[0] + "@"
            for j in i[1]:
                t = s
                for k in j:
                    t += " " + k
                t += "\n"
                f.write(t)