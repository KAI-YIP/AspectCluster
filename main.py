#coding=utf-8
import numpy as np

def Noun_Dict():
    """形成名词字典"""
    noun=[]
    g=open('./data/noun.txt','r',encoding='utf-8').readlines()
    count=0
    for line in g:
        if count==50:
            break
        else:
            line_clean=line.split()
            noun.append(line_clean[0])
            count+=1

    f2=open('./data/NA.txt','r',encoding='utf-8').readlines()
    NA_dict={}
    for word in noun:
        temp_dict={}
        for line in f2:
            line_clean=line.split()
            if line_clean[0]==word:
                temp_dict[line_clean[1]]=line_clean[2]
            else:
                pass
        NA_dict[word]=temp_dict
    f1=open('./result/NandA.txt','w',encoding='utf-8')
    for key in noun:
        f1.write(key+'    ')
        for k in NA_dict[key]:
            f1.write(k+":"+str(NA_dict[key][k])+" ")
        f1.write('\n')

def Similarity():
    """根据余弦相似度对名词进行聚类"""
    def cosine(list1,list2):
        """计算cosine"""
        XiYi=0
        Xi2=0
        Yi2=0
        for i in range(len(list1)):
            XiYi+=list1[i]*list2[i]
            Xi2+=np.square(list1[i])
            Yi2+=np.square(list2[i])
        similarity=XiYi/np.sqrt(Xi2*Yi2)
        return similarity

    noun=[]
    g=open('./data/noun.txt','r',encoding='utf-8').readlines()
    count=0
    for line in g:
        if count==50:
            break
        else:
            line_clean=line.split()
            noun.append(line_clean[0])
            count+=1

    f=open('./result/NandA.txt','r',encoding='utf-8')
    for word in noun:
        for line in f.readlines():
            line_clean=line.split()

