import csv
import sys


input_file=sys.argv[1]
Time=int(sys.argv[2])
evalrow=int(sys.argv[3])-1
hits=5

def majority(l):
    result=[0]*len(l[0])
    for item in l:
        for key,i in enumerate(item):
            result[key]=result[key]+int(i)
    for i,r in enumerate(result):
        if int(r)>hits/2:
            result[i]=1
        else:
            result[i]=0
    return result

def lessmajority(l):
    result=[0]*len(l[0])
    for item in l:
        for key,i in enumerate(item):
            result[key]=result[key]+int(i)
    for i,r in enumerate(result):
        if int(r)>hits/2+1:
            result[i]=1
        else:
            result[i]=0
    return result

def allvote(l):
    result=[0]*len(l[0])
    for item in l:
        for key,i in enumerate(item):
            result[key]=result[key]+int(i)
    for i,r in enumerate(result):
        if int(r)==hits:
            result[i]=1
        else:
            result[i]=0
    return result

def metric4(l):
    result=[0]*len(l[0])
    for item in l:
        for key,i in enumerate(item):
            result[key]=result[key]+int(i)
    for i,r in enumerate(result):
        if int(r)>1:
            result[i]=1
        else:
            result[i]=0
    return result
def metric5(l):
    result=[0]*len(l[0])
    for item in l:
        for key,i in enumerate(item):
            result[key]=result[key]+int(i)
    for i,r in enumerate(result):
        if int(r)>0:
            result[i]=1
        else:
            result[i]=0
    return result

def evaluation(diction):
    questions=0
    majority_eal=0
    lmajority_eal=0
    allvote_eal=0
    m4=0
    m5=0
    for key,val in diction.items():
        questions=questions+len(val[0])
        for k,i in enumerate(majority(val)):
            majority_eal=majority_eal+int(i)
        for k,i in enumerate(lessmajority(val)):
            lmajority_eal=lmajority_eal+int(i)
        for k,i in enumerate(allvote(val)):
            allvote_eal=allvote_eal+int(i)
        for k,i in enumerate(metric4(val)):
            m4=m4+int(i)
        for k,i in enumerate(metric5(val)):
            m5=m5+int(i)
    print 'accuracy using majority algorithm',round(float(majority_eal)/float(questions),2)
    print 'accuracy using metric2 algorithm',round(float(lmajority_eal)/questions,2)
    print 'accuracy using metric3 algorithm',round(float(allvote_eal)/questions,2)
    print 'accuracy using metric4 algorithm',round(float(m4)/questions,2)
    print 'accuracy using metric5 algorithm',round(float(m5)/questions,2)

assignment=0
dic={}
allinfo=0
understanding=0
naturalness=0
useagain=0
satisfacotry=0
user=0
sys=0
questions=0
with open(input_file, 'rb') as f:
    reader = csv.reader(f)
    for hit, row in enumerate(reader):
        if hit==0:
            continue
        elif row[16]=="Approved":
            allinfo=allinfo+int(row[evalrow].split('|')[1])
            understanding=understanding+int(row[evalrow].split('|')[2])
            naturalness=naturalness+int(row[evalrow].split('|')[3])
            useagain=useagain+int(row[evalrow].split('|')[4])
            satisfacotry=satisfacotry+int(row[evalrow].split('|')[5])
            assignment=assignment+1
            #generate evaluation dictionary
            if row[0] in dic.keys():
                lis=dic[row[0]]
                lis.append(row[evalrow].split('|')[0])
                dic[row[0]]=lis
            else:
                lis=[]
                lis.append(row[evalrow].split('|')[0])
                dic[row[0]]=lis
            #compute the efficiency cost
                for k,col in enumerate(row):
                    col=col.strip('\"')
                    if col.startswith('USR'):
                        user=user+1
                    elif col.startswith('SYS'):
                        sys=sys+1
                    elif col.startswith('Answer'):
                        questions=questions+1
    conversations=len(dic.keys())
    evaluation(dic)
    print 'Total number of user/system turns: ',sys+user
    print 'Total number of system turns: ',sys
    print 'Average number of user/system turns per task: ',(sys+user)/conversations
    print 'Total elapse time: ',Time,'minutes'
    print 'Average elapsed time per task: ', round(float(Time)/float(conversations),2),'minutes'
    print 'Questionnnaire: from 1(Not at all) to 5(Yes, Absolutely)'
    print 'Get all the wanted information: ',round(float(allinfo)/float(assignment),2)
    print 'Clarity: ',round(float(understanding)/float(assignment),2)
    print 'Naturalness: ',round(float(naturalness)/float(assignment),2)
    print 'Willingness to use system again: ',round(float(useagain)/float(assignment),2)
    print 'User satisfactory: ',round(float(satisfacotry)/float(assignment),2)




    



