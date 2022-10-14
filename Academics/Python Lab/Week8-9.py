1.
import numpy as np
def fun1(a,shape):
    arr=a.reshape(shape)
    return arr
def fun2(a,n):
    arr=np.split(a,n)
    return arr
a1=np.array(list(map(int,input("enter array 1:").split())))
a2=np.array(list(map(int,input("enter array 2:").split())))
print("1 D Array:",a1)
print("Common elements in array1 and array2:")
for i in a1:
    if(not(i not in a2)):
        print(i)
a3=np.random.randint(low=1,high=100,size=12)
print("a3 before reshape:",a3)
print("a3 after reshape(2,6):",fun1(a3,(2,6)))
print("a3 after reshape(3,4):",fun1(a3,(3,4)))
print("a3 as 3D array:",fun1(a3,(3,4,1)))
print("a3 after splitting into 2 parts",fun2(a3,2))
print("a3 after splitting into 3 parts",fun2(a3,3))
print("a3 after splitting into 4 parts",fun2(a3,4))
print("array 1 and array 2 concatenated:",np.concatenate((a1,a2)))
a1=np.array(sorted(list(a1)))
print("array1 after sort in ascending order:",a1)
a1=np.array(sorted(list(a1),reverse=True))
print("array1 after sort in descending order:",a1)
print("Even nos. in array1:")
for i in a1:
    if(i%2==0):
        print(i)

2.
import numpy as np
def fun1(a,shape):
    arr=a.reshape(shape)
    return arr
a3=np.random.randint(low=1,high=100,size=(2,6))
print("a3 before reshape:",a3)
print("a3 as 1D array:",fun1(a3,(12)))
print("a3 as 3D array:",fun1(a3,(3,2,2)))
print("Sum of elements of a3:",a3.sum())
a4=np.random.randint(low=1,high=100,size=(4,4))
print("a4 array:",a4)
print("Principal diagonal elements of a")
for i in range(4):
 for j in range(4):
    if(i==j):
        print(a4[i][i])
a1=np.random.randint(low=1,high=100,size=12)
print('reverse of a1 without for loop',a1[-1::-1])
a2=a1.copy()
for i,j in zip(a2,range(len(a1)-1,-1,-1)):
    a1[j]=i
print('reverse of a1 with for loop',a1)

3,4,5:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return n
    return np.NAN

#create a random dataset
a1=np.random.randint(low=1,high=100,size=100)
a2=100+np.random.randint(low=1,high=100,size=100)
a3=4*a1+3*a2+np.random.randint(low=1,high=100,size=100)
df=pd.DataFrame({'column1':a1,'column2':a2,'column3':a3})

#Make some values of column 3 as null values
df['column3']=df['column3'].apply(prime)

print("First five rows of dataset:\n",df.head())
print("Last five rows of dataset:\n",df.tail())
print("Dataset information:\n",df.info())
print("Description of all columns:\n",df.describe())
print("Dataset without empty values:\n",df[df.isna().any(axis=1)!=True])
#Plug na values with mean
df.fillna(value=df['column3'].mean(),inplace=True)
#Plug na values with median
df.fillna(value=df['column3'].median(),inplace=True)
#Create two duplicate rows
r1=pd.DataFrame({'column1':[df['column1'].mean()],'column2':[df['column2'].mean()],'column3':[df['column3'].mean()]})
r2=pd.DataFrame({'column1':[df['column1'].mean()],'column2':[df['column2'].mean()],'column3':[df['column3'].mean()]})
df=pd.concat([df,r1,r2],axis=0)
df.reset_index(inplace=True)
#Include this line to remove extra 'index' column
df.drop(columns=['index'],inplace=True)
print("Duplicate entries:\n",df[df.duplicated()])
plt.subplot(5,1,1)
plt.plot()
plt.plot(np.arange(0,102),df['column1'])
plt.plot(np.arange(0,102),df['column2'])
plt.plot(np.arange(0,102),df['column3'])
plt.title("Plot of dataset")
plt.subplot(5,1,2)
plt.title("Scatter plots with different colors")
plt.scatter(df['column1'],df['column3'],c='b')
plt.subplot(5,1,3)
plt.scatter(df['column1'],df['column3'],c='r')
plt.subplot(5,1,4)
plt.scatter(df['column1'],df['column3'],c='g')
plt.subplot(5,1,5)
plt.title("Histogram on column3")
plt.hist(df['column2'])
plt.show()
