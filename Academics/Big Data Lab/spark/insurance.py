import sys
if(len(sys.argv)!=4):
   print("Provide Input File and Output Directory")
   sys.exit(0)
from pyspark import SparkContext
sc =SparkContext()
f = sc.textFile(sys.argv[1])
temp=f.map(lambda x: (x.split(',')[16],1))
data=temp.countByKey()
dd1=sc.parallelize(data.items())
dd1.saveAsTextFile(sys.argv[2])

temp=f.map(lambda x: (x.split(',')[2],int(x.split(',')[17])))
data=temp.reduceByKey(lambda x,y: x+y)
data.saveAsTextFile(sys.argv[3])
