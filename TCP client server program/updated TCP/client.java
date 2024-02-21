import java.io.*;
import java.net.*;
import java.util.Scanner;
class client{
    public static void main(String args[]) throws IOException
    {

        Socket s = new Socket("localhost",4000);
        System.out.println("Connected to server");

        InputStream inp = s.getInputStream();
        OutputStream out = s.getOutputStream();
        InputStreamReader ins = new InputStreamReader(inp);
        BufferedReader read_data = new BufferedReader(ins);
        Scanner scan = new Scanner(System.in);
        PrintWriter write_data = new PrintWriter(out,true);

        System.out.println("Send name : ");
        String name = scan.nextLine();
        write_data.println(name);
        //sent to server

        String msg = read_data.readLine();
        System.out.println("Message from server : "+msg);
        s.close();
        scan.close();
    }
}