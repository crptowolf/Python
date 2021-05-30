import java.io.*;
import java.text.*;
import java.util.*;
public class LesenSchreibenTextdatei
{
public static void main( String[] args )
{
final String[] KEYS = { "user.name", "user.language", "user.home", "os.name", "java.version" };
Vector vec = new Vector();
String s;
try {
BufferedReader in = new BufferedReader(
new InputStreamReader(
new FileInputStream( "MeineTextDatei.txt" ) ) );
while( null != (s = in.readLine()) ) {
vec.add( s );
}
}
catch( FileNotFoundException ex ) {
}
catch( Exception ex ) {
System.out.println( ex );
}
finally {
if( in != null ) in.close();
}
if( 0 >= vec.size() ) {
for( int i=0; i<KEYS.length; i++ ) {
vec.add( KEYS[i] + " = " + System.getProperty( KEYS[i] ) );
}
}
vec.add( "Zeitstempel = " + new SimpleDateFormat("yyyy-MM-dd HH:mm:ss,SSS" ).format( new Date() ) );
try {
BufferedWriter out = new BufferedWriter(
new OutputStreamWriter(
new FileOutputStream( "MeineTextDatei.txt" ) ) );
for( int i=0; i<vec.size(); i++ ) {
s = vec.get( i ).toString();
System.out.println( s );
out.write( s, 0, s.length() );
out.newLine();
}
} catch( IOException ex ) {
System.out.println( ex );
} finally {
if( out != null ) out.close();
}
}
}
