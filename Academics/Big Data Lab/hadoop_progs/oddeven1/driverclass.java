package oddeven1;
import java.io.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.io.*;
public class driverclass
{
public static void main(String args[]) throws IOException
{
JobConf config=new JobConf(driverclass.class);
config.setMapperClass(mapperclass.class);
config.setReducerClass(reducerclass.class);
config.setOutputKeyClass(Text.class);
config.setOutputValueClass(IntWritable.class);
FileInputFormat.setInputPaths(config,new Path(args[0]));
FileOutputFormat.setOutputPath(config,new Path(args[1]));
JobClient.runJob(config);
}
}
