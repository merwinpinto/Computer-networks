import java.net.*;
import java.io.*;
import java.util.Scanner;

class clientTCP {
    public static void main(String args[]) {
        try {
            Socket s = new Socket("localhost", 3000);

            Scanner scanner = new Scanner(System.in);
            
            InputStream inp = s.getInputStream();
            OutputStream out = s.getOutputStream();

            InputStreamReader isr = new InputStreamReader(inp);
            BufferedReader readMessage = new BufferedReader(isr);

            PrintWriter write = new PrintWriter(out, true);
            

            System.out.print("Enter the first name ");
            String message1 = scanner.nextLine();
            write.println(message1);

            System.out.print("Enter the last name  ");
            String message2 = scanner.nextLine();
            write.println(message2);      

            String serverResponse = readMessage.readLine();
            System.out.println("Server: " + serverResponse);

            scanner.close();
            s.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}