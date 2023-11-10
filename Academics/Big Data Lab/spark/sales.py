import sys
if(len(sys.argv)!=4):
   print("Provide Input File and Output Directory")
   sys.exit(0)
from pyspark import SparkContext
sc =SparkContext()
f = sc.textFile(sys.argv[1])
temp1=f.map(lambda x: (x.split(',')[7],int(x.split(',')[2])))
temp2=f.map(lambda x: (x.split(',')[7],1))
red1=temp1.reduceByKey(lambda x,y: x+y)
red2=temp2.reduceByKey(lambda x,y: x+y)
def to_list(a):
    return [a]
def append(a,b):
    a.append(b)
    return a
def extend(a,b):
    a.extend(b)
    return a

red=red1.union(red2).combineByKey(to_list,append,extend)
red.saveAsTextFile(sys.argv[2])
temp=f.map(lambda x: ((x.split(',')[7],x.split(',')[1]),int(x.split(',')[2])))
red=temp.reduceByKey(lambda x,y: x+y)
red.saveAsTextFile(sys.argv[3])
