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
            list1[i]=float(list1[i])
            list2[i]=float(list2[i])
            XiYi+=list1[i]*list2[i]
            Xi2+=np.square(list1[i])
            Yi2+=np.square(list2[i])
        similarity=XiYi/np.sqrt(Xi2*Yi2)
        return similarity

    noun=[]
    g=open('./data/noun.txt','r',encoding='utf-8')
    count=0
    for line in g.readlines():
        if count==50:
            break
        else:
            line_clean=line.split()
            noun.append(line_clean[0])
            count+=1
    g.close()
    print (len(noun))

    f=open('./data/NA.txt','r',encoding='utf-8').readlines()
    NA_dict={}
    for word in noun:
        temp_dict={}
        for line in f:
            line_clean=line.split()
            if line_clean[0]==word:
                temp_dict[line_clean[1]]=line_clean[2]
            else:
                pass
        NA_dict[word]=temp_dict

    print (NA_dict['信号/n'])

    h=open('./result/N_N_similarity.txt','w',encoding='utf-8')
    for word in noun:
        h.write(word+'\n')
        related_dict={}
        for key in NA_dict:
            temp_list1=[]
            temp_list2=[]
            if key==word:
                continue
            else:
                for k in NA_dict[key]:
                    if k in NA_dict[word]:
                        temp_list1.append(NA_dict[word][k])
                        temp_list2.append(NA_dict[key][k])
                    else:
                        pass
            if temp_list1:
                similarity=cosine(temp_list2,temp_list1)
                print (key,similarity)
            else:
                similarity=0
            related_dict[key]=similarity
        for k,v in sorted(related_dict.items(),key=lambda d:d[1],reverse=True)[:10]:
            h.write('   '+k+'  '+str(v)+"\n")

    h.close()

def AspectBased():
    """名词做为属性聚类"""
    noun=[]
    g=open('./data/noun.txt','r',encoding='utf-8')
    count=0
    for line in g.readlines():
        if count==50:
            break
        else:
            line_clean=line.split()
            noun.append(line_clean[0])
            count+=1
    g.close()

    f=open('./data/test/NA.txt','r',encoding='utf-8').readlines()
    NA_dict={}
    for word in noun:
        temp_dict={}
        for line in f:
            line_clean=line.split()
            if line_clean[0]==word:
                temp_dict[line_clean[1]]=line_clean[2]
            else:
                pass
        NA_dict[word]=temp_dict

    ADJ_dict={}
    h=open('./data/ADJ.txt','r',encoding='utf-8')
    for line in h.readlines():
        line_clean=line.split()
        ADJ_dict[line_clean[0]]=line_clean[1]
    h.close()

    f2=open('./data/test/N_N_similarity.txt','w',encoding='utf-8')
    for word1 in noun:
        similarity=0
        Total_similarity=0
        word_similarity={}
        copy_noun=noun[:]
        copy_noun.remove(word1)
        for word2 in copy_noun:
            for key in NA_dict[word1]:
                if key in NA_dict[word2]:
                    WjI=NA_dict[word2][key]
                    WiI=NA_dict[word1][key]
                    Sum_I=ADJ_dict[key]
                    similarity+=float(WjI)*float(WiI)/float(Sum_I)
                else:
                    pass
            word_similarity[word2]=similarity
        f2.write(word1+'\n')
        for k,v in sorted(word_similarity.items(),key=lambda d:d[1],reverse=True):
            if Total_similarity!=0:
                f2.write("  "+k+"  "+str(float(v)/Total_similarity)+'\n')
            else:
                f2.write("  "+k+"  0"+'\n')
        f2.write('\n')

AspectBased()