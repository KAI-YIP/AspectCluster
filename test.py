#coding=utf-8
f=open('./data/NA.txt','r',encoding='utf-8')
h=open('./data/test/NA.txt','w',encoding='utf-8')
for line in f.readlines():
    line_clean=line.split()
    if float(line_clean[2])>=5:
        h.write(line_clean[0]+" "+line_clean[1]+" "+"1"+'\n')
    else:
        break
