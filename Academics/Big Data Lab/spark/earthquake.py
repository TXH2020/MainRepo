import sys
if(len(sys.argv)!=3):
    file.write("Provide Input File and Output Directory")
    sys.exit(0)
from pyspark import SparkContext
sc =SparkContext()
f = sc.textFile(sys.argv[1])
map1=f.map(lambda x: (x.split(',')[11],float(x.split(',')[8])))
red1=map1.reduceByKey(lambda a,b:a if a>b else b)
map2=f.map(lambda x: (x.split(',')[11],float(x.split(',')[9])))
red2=map2.reduceByKey(lambda a,b:a if a>b else b)
map3=f.map(lambda x: (x.split(',')[11],float(x.split(',')[6])))
red3=map3.reduceByKey(lambda a,b:a if a>b else b)
map4=f.map(lambda x: (x.split(',')[11],float(x.split(',')[7])))
red4=map4.reduceByKey(lambda a,b:a if a>b else b)
with open('results.txt','w') as file:   
    file.write("Statistics by magnitude:\n"+str(red1.collect())+"\n")
    file.write("Statistics by depth:\n"+str(red2.collect())+"\n")
    file.write("Statistics by latitude:\n"+str(red3.collect())+"\n")
    file.write("Statistics by longitude:\n"+str(red4.collect())+"\n")


