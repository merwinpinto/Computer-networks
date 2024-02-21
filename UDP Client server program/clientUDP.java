import java.net.*;
import java.io.*;
import java.util.*;

public class clientUDP {
    public static void main(String args[]) {
        try {
            DatagramSocket ds = new DatagramSocket();

            Scanner scanner = new Scanner(System.in);
            
            while (true) {
                System.out.print("Enter message to send (type 'exit' to quit): ");
                String message = scanner.nextLine();

                if (message.equalsIgnoreCase("exit")) {
                    break;
                }

                byte[] b = message.getBytes();
                InetAddress ia = InetAddress.getLocalHost();
                DatagramPacket dp = new DatagramPacket(b, b.length, ia, 4000);
                ds.send(dp);

                System.out.println("Message sent to server: " + message);
            }

            System.out.println("Exit !");
            scanner.close();
            ds.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
