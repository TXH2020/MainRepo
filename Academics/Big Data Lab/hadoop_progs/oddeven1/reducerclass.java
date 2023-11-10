package oddeven1;
import java.io.*;
import java.util.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.io.*;
public class reducerclass extends MapReduceBase implements Reducer<Text,IntWritable,Text,IntWritable>{
public void reduce(Text text,Iterator<IntWritable> values,OutputCollector<Text,IntWritable> output, Reporter r) throws IOException{
int n=0,sum=0;
while(values.hasNext()){
sum+=values.next().get();
n++;
}
output.collect(new Text("Sum of all "+text+" numbers="), new IntWritable(sum));
output.collect(new Text("Count of all "+text+" numbers="), new IntWritable(n));
}
}
