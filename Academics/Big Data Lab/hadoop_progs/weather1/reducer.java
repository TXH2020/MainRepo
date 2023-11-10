package weather1;
import java.util.*;
import java.io.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.mapred.*;
public class reducer extends MapReduceBase implements Reducer<Text,DoubleWritable,Text,DoubleWritable>{
public void reduce(Text text,Iterator<DoubleWritable> list,OutputCollector<Text,DoubleWritable> output,Reporter r)throws IOException{
double max=-9999.0;
double min=9999.0;
while(list.hasNext()){
double temp=list.next().get();
if(temp>max)
max=temp;
if(temp<min)
min=temp;
}
output.collect(new Text("maximum temperature found at city: "+text+" ="),new DoubleWritable(max));
output.collect(new Text("minimum temperature found at city: "+text+" ="),new DoubleWritable(min));
}}
