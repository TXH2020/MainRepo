import numpy as np
a1=np.random.randint(1,100,10)
a2=np.random.randint(1,100,10)
with open('file1.txt','w') as file:
    for i in range(10):
        file.write(str(a1[i])+"\n")
with open('file2.txt','w') as file:
    for i in range(10):
        file.write(str(a2[i])+"\n")

def sortfile(file):
    l=[]
    with open(file,'r') as f:
        l1=f.readlines()
        for i in range(len(l1)):
            l.append(int(l1[i].rstrip('\n')))
        l.sort()
        for i in range(len(l)):
            l[i]=str(l[i])+"\n"
    with open(file,'w') as f:
        for i in range(len(l)):
            f.write(l[i])

def displayfile(file):
    with open(file, 'r') as f:
        print(f.read())

sortfile('file1.txt')
sortfile('file2.txt')

with open('file1.txt','r') as file1,open('file2.txt','r') as file2,\
        open('Result.txt','w') as file:
    l1=file1.readlines()
    l2=file2.readlines()
    for (i,j) in zip(l1,l2):
        file.write(i)
        file.write(j)

sortfile('Result.txt')
print("File 1 contents")
displayfile('file1.txt')
print("File 2 contents")
displayfile('file2.txt')
print("result file contents")
displayfile('Result.txt')
