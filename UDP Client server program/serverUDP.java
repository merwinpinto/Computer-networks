import java.net.*;
import java.io.*;

public class serverUDP {
    public static void main(String args[]) {
        try {

            DatagramSocket ds = new DatagramSocket(4000);
            while (true) {
                byte[] b1 = new byte[1024];
                DatagramPacket dp = new DatagramPacket(b1, b1.length);

                ds.receive(dp);

                String str = new String(dp.getData());
                System.out.println("Message received from client: \n" + str);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}