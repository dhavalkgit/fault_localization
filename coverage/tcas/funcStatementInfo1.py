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
with open('statementResultV40.csv', 'w') as csvfile2 :
    spamwriter2 = csv.writer(csvfile2, delimiter=',')
    fp1 = open("/home/dhaval07/Downloads/tcas_2.0/tcas/testplans.alt/universe");
    i = 0
    for l1 in fp1:
        os.system("gcc -fprofile-arcs -ftest-coverage tcas.c")
        os.system("./a.out "+l1)
        i = i+1
        j = 1
        k = 1
        os.system("gcov tcas.c")
        fp1 = open("tcas.c.gcov");
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

        p = filecmp.cmp('/home/dhaval07/Downloads/tcas_2.0/tcas/outputs/orignaloutputs/t'+str(i), '/home/dhaval07/Downloads/tcas_2.0/tcas/newoutputs/v40/t'+str(i))
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
