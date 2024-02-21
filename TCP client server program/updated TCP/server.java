import java.io.*;
import java.net.*;

class server{
    public static void main(String args[]) throws IOException
    {
        System.out.println("hello welcome to TCP Program");
        ServerSocket ss = new ServerSocket(4000);
        System.out.println("Waiting . . .");
        
        Socket s = ss.accept();
        System.out.println("Connection estb !");

        InputStream inp = s.getInputStream();
        OutputStream out = s.getOutputStream();
        InputStreamReader ins = new InputStreamReader(inp);
        BufferedReader read_data = new BufferedReader(ins);
        PrintWriter write_data = new PrintWriter(out,true);

        //sent to client
        write_data.println("server here !");

        String msg = read_data.readLine();
        System.out.println("Message from client : "+msg);
        ss.close();
        s.close();
    }
}