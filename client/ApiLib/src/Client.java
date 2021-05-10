import java.net.*;
import java.io.*;


public class Client {
    private Socket clientSocket;
    private DataOutputStream out;
    private DataInputStream in;

    public void startConnection(Socket socket) throws IOException {
        clientSocket = socket;
        out = new DataOutputStream(clientSocket.getOutputStream());
        in = new DataInputStream(clientSocket.getInputStream());
    }

    public void sendMessage(String message) throws IOException {
        out.writeUTF(message);
        out.flush();
    }

    public String getMessage() throws IOException {
        return in.readUTF();
    }

    public void stopConnection() throws IOException {
        in.close();
        out.close();
        clientSocket.close();
    }
}
