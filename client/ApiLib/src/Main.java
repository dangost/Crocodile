import java.util.Scanner;
import java.io.*;
import java.net.*;

import java.io.IOException;


public class Main {
    public static void main(String[] args) throws IOException {
        // var ip = "77.223.97.149";
        var ip = "192.168.100.5";
        int port = 9090;

        Scanner in = new Scanner(System.in);

        Socket socket = new Socket(ip, port);

        Client client = new Client();
        client.startConnection(socket);

        System.out.println("Input Your Name!\n");
        client.sendMessage("IDEA");
        while (true)
        {
            System.out.println("\nwrite\n");
            String message = in.nextLine();

            client.sendMessage(message);
        }

    }
}