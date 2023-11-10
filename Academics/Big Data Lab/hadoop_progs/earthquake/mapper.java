package earthquake;
import java.util.*;
import java.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.io.*;
public class mapper extends MapReduceBase implements Mapper<LongWritable, Text,Text,DoubleWritable>
{
    public void map(LongWritable key , Text value , OutputCollector<Text,DoubleWritable> output, Reporter r) throws IOException
    {
   	 String[] line=value.toString().split(",");
   	 Double lat=Double.parseDouble(line[6]);
   	 Double lon=Double.parseDouble(line[7]);
   	 Double depth=Double.parseDouble(line[8]);
   	 Double mag=Double.parseDouble(line[9]);
   	 output.collect(new Text("Latitude "+line[11]), new DoubleWritable(lat));
   	 output.collect(new Text("Longitude "+line[11]), new DoubleWritable(lon));
   	 output.collect(new Text("Depth "+line[11]), new DoubleWritable(depth));
   	 output.collect(new Text("magnitude "+line[11]), new DoubleWritable(mag));
    }
}
