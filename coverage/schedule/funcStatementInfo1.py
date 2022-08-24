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
with open('statementResultV9.csv', 'w') as csvfile2 :
    spamwriter2 = csv.writer(csvfile2, delimiter=',')
    fp = open("/home/dhaval07/Downloads/schedule_2.0/schedule/testplans.alt/universe");
    i = 0
    for l1 in fp:
        li1=[]
        li1=l1.split('<')
        s2=li1[1].split('/')[1]
        s3=li1[0]+ '</home/dhaval07/Downloads/schedule_2.0/schedule/inputs/input/'+s2
        os.system("gcc -fprofile-arcs -ftest-coverage schedule.c")
        os.system("./a.out "+s3)
        i = i+1
        j = 1
        k = 1
        os.system("gcov schedule.c")
        fp1 = open("schedule.c.gcov");
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

        p = filecmp.cmp('/home/dhaval07/Downloads/schedule_2.0/schedule/Orignal_output/t'+str(i), '/home/dhaval07/Downloads/schedule_2.0/schedule/newoutputs/V9/t'+str(i))
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
