import csv
import os
import sys
import subprocess
import filecmp
functitle = []
funcvalue = []
statetitle = []
statefault=[]
statevalue = []
pq = 0
g = 0

# /home/dhaval07/Downloads/replace_2.1/replace/testplans.alt
# /home/dhaval07/Downloads/totinfo_2.0/totinfo/inputs/universe/tst88
with open('statementResultV10.csv', 'w') as csvfile2 :
    spamwriter2 = csv.writer(csvfile2, delimiter=',')
    fp = open("/home/dhaval07/Downloads/printtokens2_2.0/printtokens2/testplans.alt/universe");
    i = 0
    for l1 in fp:
        s2=""
        if l1[0]=='<':
            # print('<')
            l2=l1.split('<')[1]
            s2='/home/dhaval07/Downloads/printtokens2_2.0/printtokens2/inputs/'+l2
            # print(s2)
        elif l1[0]=='.':
            # print('.') 
            l2=l1.split('..')[1]
            s2='/home/dhaval07/Downloads/printtokens2_2.0/printtokens2'+l2
            # print(s2)
        else:
            s2=l1
            # print(s2) 
        os.system("gcc -fprofile-arcs -ftest-coverage print_tokens2.c")
        os.system("./a.out "+s2)
        i = i+1
        j = 1
        k = 1
        os.system("gcov print_tokens2.c")
        fp1 = open("print_tokens2.c.gcov");
        for line1 in fp1:
            try:
                flag = line1.split(":")[0];
                if "-" in flag:
                    continue
                elif "#####" in flag:
                    statevalue.append("0")
                    statetitle.append(k)
                    k = k+1
                else:
                    statevalue.append("1")
                    statetitle.append(k)
                    k = k+1
            except:
                print ("exiting")
                exit(1)

        p = filecmp.cmp('/home/dhaval07/Downloads/printtokens2_2.0/printtokens2/Orignal_Output/t'+str(i), '/home/dhaval07/Downloads/printtokens2_2.0/printtokens2/newoutputs/V10/t'+str(i))
        if p == True:
            statevalue.append(int('0'))
        else:
            statevalue.append(int('1'))
        if pq == 0:
            statetitle.append("Result")
            spamwriter2.writerow(statetitle)
            pq = 1
        if len(statevalue) > 1:
            spamwriter2.writerow(statevalue)
            statevalue = []
        else:
            statevalue = []
