import sys
import time
from datetime import datetime
start_time=datetime.now()
import pandas as pd
import numpy as np
import math
import os
import csv


# with open("f_l.txt",'r') as f:
# 	line = f.readline() 

df_train=pd.read_csv('statementResultV5.csv')

#training output dataset
y = np.array([df_train['Result']]).T
y=y.tolist()
#print y

#training input dataset
df_train.drop(['Result'],1 , inplace=True)
t_in = df_train.values.tolist()
x = np.array(t_in)
x=x.tolist()
#print len(y[0])
total_failed=np.count_nonzero(y)
total_passed=len(y)-total_failed



suspicious=[]
csvfile=open("tarantulaResult5.csv", "w")
spamwriter1 = csv.writer(csvfile, delimiter=',')
for i in range(0,len(x[0])):
	nsuccess=0
	nfailure=0
	for j in range(0,len(y)):
		mylist=[]
		#print x[j][i],y[j][0]
		if x[j][i]==1 and y[j][0]==0:
			nsuccess=nsuccess+1
		elif x[j][i]==1 and y[j][0]==1:
			nfailure=nfailure+1
	try:
		#print nfailure,nsuccess
		cef=nfailure
		cep=nsuccess
		sus_score=float(float(cef)/float(total_failed)) / float((float(cef)/float(total_failed))+(float(cep)/float(total_passed)))
		mylist.append(i)
		mylist.append(sus_score)
		spamwriter1.writerow(mylist);
		# print(str(i)+"   "+str(sus_score))
	except ZeroDivisionError:
		sus_score=-999999
		suspicious.append(sus_score)
		mylist.append(i)
		mylist.append(sus_score)
		spamwriter1.writerow(mylist);
		# print(str(i)+"   "+str(sus_score))



