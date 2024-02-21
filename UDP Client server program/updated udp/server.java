import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class server{
    public static void main(String Args[]) throws IOException
    {
        DatagramSocket ds = new DatagramSocket(3000);
        byte[] b1 = new byte[1024];
        DatagramPacket dp = new DatagramPacket(b1, b1.length);
        while(true)
        {
        ds.receive(dp);
        String str  = new String(dp.getData());
        System.out.println("Data received : \n"+str);
        }
    }
}