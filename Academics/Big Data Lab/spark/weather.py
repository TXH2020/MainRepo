import sys
if(len(sys.argv)!=3):
    print("Specify input and output")
    sys.exit(0)
from pyspark import SparkContext
sc=SparkContext()
original_file=sc.textFile(sys.argv[1])
narrow_file=original_file.filter(lambda x:x if(x[15:19]=="1950") else None)
temp=narrow_file.map(lambda x:(int(x[4:10]),float(x[87:92])))
maxtemp=temp.reduceByKey(lambda x,y:x if x>y else y)
mintemp=temp.reduceByKey(lambda x,y:x if x<y else y)
temps=maxtemp.union(mintemp)
temps.saveAsTextFile(sys.argv[2])
