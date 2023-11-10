package weather1;
import java.util.*;
import java.io.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.mapred.*;
public class mapper extends MapReduceBase implements Mapper<LongWritable,Text,Text,DoubleWritable>{
public void map(LongWritable key,Text text,OutputCollector<Text,DoubleWritable> output,Reporter r)throws IOException{
Double temp=Double.parseDouble(text.toString().substring(87,92));
String city=text.toString().substring(4,10);
String year=text.toString().substring(15,19);
if(year.equals("1950"))
output.collect(new Text(city),new DoubleWritable(temp));
}}
