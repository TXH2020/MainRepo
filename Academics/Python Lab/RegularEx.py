import re
from datetime import datetime
import sys
string=""
while(True):
    i=sys.stdin.readline()
    if(i=='stop\n'):
        break;
    string=string+i
text=input("Enter C program")
import ast
text=str(ast.literal_eval(input("Enter text")))
key=input("Enter search word")
text.lower()
vowels=re.findall('[aeiou]',text)
consonants=re.findall('[^\d\saeiou]',text)
digits=re.findall('[\d]',text)
q1=re.findall('[Aa]b*',text)
q2=re.findall('[Aa]b?',text)
q3=re.findall('[Aa]b+',text)
q4=re.findall('[Aa]b{4}c',text)
q81=re.findall(r"\b\w{3,5}\b", text)
print(vowels,consonants,digits)
print(q1)
print(q2)
print(q3)
print(q4)
print(q81)
result = [_.start() for _ in re.finditer(key, text)]
print("Start indices are:",result)
rep=re.sub(key,'hello',text)
print(rep)
a3=re.search('^1MS.{6}0$',text)
if(a3):
    print("USN follows rules")
len2n=re.findall(r'\b\w{2}\b',text)
len4n=re.findall(r'\b\w{4}\b',text)
print("2 digit odd nos. are:")
k=0
for i in len2n:
    if(int(i)%2!=0):
        k=1;print(i)
if(k==0):
    print("None")
k=0
print("4 digit odd nos. are:")
for i in len4n:
    if(int(i)%2!=0):
        k=1
        print(i)
if(k==0):
    print("None")
print(string)

date = input("Enter date")

obj = datetime.strptime(date, '%Y/%m/%d')
date_time_str = obj.strftime("%d-%m-%Y")
print(date_time_str)