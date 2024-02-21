import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

public class client{
    public static void main(String Args[]) throws IOException
    {
        DatagramSocket ds = new DatagramSocket();
        
        while(true)
        {
            Scanner s = new Scanner(System.in);
            String message = s.nextLine();
            byte[] b1 = message.getBytes();
            InetAddress ia = InetAddress.getLocalHost();
            DatagramPacket dp = new DatagramPacket(b1, b1.length,ia,3000);
            ds.send(dp);
            System.out.println("Data Sent : \n");
        }
        
    }
}