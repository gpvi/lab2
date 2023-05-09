# coding=utf-8
path = './lr_sentence.txt'
class LR_first:

    def __init__(self):
        self.path = './lr_sentence.txt'
        self.first = {}
        self. sentences = {}
        self.no_term = set()
    def read_sentence(self):
        path = self.path

        sentences = self.sentences

        with open(path ,'r' ,encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                temp = line.split('@')
                temp[1] = temp[1].strip('\n')
                temp[1] = temp[1].split()
                # temp[1] = list(filter(lambda x: x != "",temp[1]))
                # print(temp[1])
                if temp[0] not in sentences:
                    sentences[temp[0]] = []
                    sentences[temp[0]].append(temp[1])
                else:
                    sentences[temp[0]].append(temp[1])
        no_term = self.no_term
        for i in sentences:
            no_term.add(i)

    def create_first(self):
    # sentences 字典
        self.read_sentence()
        count = 0
        first = self.first
        flag = 0
        sentences = self.sentences
        no_term = self.no_term
        while flag == 0:
            flag = 1
            for i in sentences.items():
                term_sentences = i[1][:]
                if i[0] not in first:
                    first[i[0]] = set()
                for sentence in term_sentences:
                    k = 0
                    while sentence[k] == i[0]:
                        k += 1
                    term = sentence[k]
                    if term not in no_term:
                        if term not in first[i[0]]:
                            first[i[0]].add(term)
                            flag = 0
                    else:
                        if term not in first:
                            continue
                        else:
                            first[i[0]] = first[i[0]].union(first[term])

# print(first)
# for i in first.items():
#     if len(i[1]) == 0:
#         print(i[0])

# for i in first.items():
#     print(i[1])

if __name__ == '__main__':
    first = LR_first()
    first.create_first()

    for i in first.first.items():
        print(i)