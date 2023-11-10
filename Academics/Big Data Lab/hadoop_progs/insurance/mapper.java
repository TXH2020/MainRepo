package insurance;
import java.io.*;
import java.util.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.io.*;

public class mapper extends MapReduceBase implements Mapper<LongWritable , Text , Text , IntWritable>
{
    public void map(LongWritable key,Text value,OutputCollector<Text,IntWritable> output,Reporter r) throws IOException
    {
   	 String[] line=value.toString().split(",");
   	 output.collect(new Text(line[16]),new IntWritable(1));
   	 output.collect(new Text("County="+line[2]),new IntWritable(Integer.parseInt(line[17])));
    }
}
