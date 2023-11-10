package sales;
import java.io.*;
import java.util.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.io.*;

public class mapper extends MapReduceBase implements Mapper<LongWritable , Text , Text , IntWritable>
{
    public void map(LongWritable key,Text value,OutputCollector<Text,IntWritable> output,Reporter r) throws IOException
    {
   	 String[] line=value.toString().split(",");
   	 int price=Integer.parseInt(line[2]);
   	 String cardtype=line[3];
   	 String Country=line[7];
   	 String product=line[1];
   	 output.collect(new Text("("+Country+","+product+")"),new IntWritable(price));
   	 output.collect(new Text("("+Country+","+cardtype+")"),new IntWritable(price));
    }
}
