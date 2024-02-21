import java.net.*;
import java.io.*;

class serverTCP{
    public static void main(String args[])
    {
        String message1,message2;

        try{
        ServerSocket ss = new ServerSocket(3000);
        System.out.println("Server waiting for connection ...");

        Socket s = ss.accept();       
        System.out.println("Client connection Established ! ");
  
        InputStream inp  = s.getInputStream();
        OutputStream out = s.getOutputStream();  

        InputStreamReader isr = new InputStreamReader(inp);
        BufferedReader read_message = new BufferedReader(isr);
        
        PrintWriter write = new PrintWriter(out, true);
        
        write.println("Hello there! This is the server.");
    
        message1 = read_message.readLine();
        System.out.println("Client : "+message1);
    
        message2 = read_message.readLine();
        System.out.println("Client : "+message2);

        ss.close();
        s.close();
        }
        catch (IOException e) 
        {
            e.printStackTrace();
        }
    }
} 
