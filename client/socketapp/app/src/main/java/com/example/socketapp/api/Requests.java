package com.example.socketapp.api;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.*;
import java.util.Scanner;

public class Requests extends Thread {

    // GET, POST, PUT, DELETE
    public String method = "GET";

    public String url = null;

    public String inJson = null;

    public String response = null;

    public Integer statusCode = null;

    public String get(String url) throws IOException {
        URL obj = new URL(url);

        HttpURLConnection connection = (HttpURLConnection) obj.openConnection();

        try {
            connection.setRequestMethod("GET");

            InputStream in = connection.getInputStream();

            Scanner scanner = new Scanner(in);
            scanner.useDelimiter("\\A");

            boolean hasInput = scanner.hasNext();

            if (hasInput) {
                StringBuilder response = new StringBuilder();

                while(scanner.hasNext()) {
                    response.append(scanner.next());
                }


                return response.toString();
            }
            else {
                return null;
            }
        }
        finally {
            connection.disconnect();
        }

    }

    public static String post(String url, String json) throws IOException
    {
        URL obj = new URL(url);

        HttpURLConnection connection = (HttpURLConnection) obj.openConnection();
        try {
            byte[] out = json.getBytes("utf-8");
            int length = out.length;
            connection.setRequestMethod("POST");

            connection.setFixedLengthStreamingMode(length);
            connection.setRequestProperty("Content-Type", "application/json; charset=UTF-8");

            connection.setDoOutput(true);
            connection.connect();

            OutputStream os = connection.getOutputStream();
            os.write(out);

            connection.setRequestProperty("Accept", "application/json");
            InputStream in = connection.getInputStream();

            Scanner scanner = new Scanner(in);
            scanner.useDelimiter("\\A");

            boolean hasInput = scanner.hasNext();

            if (hasInput) {
                StringBuilder response = new StringBuilder();

                while(scanner.hasNext()) {
                    response.append(scanner.next());
                }

                return response.toString();
            }
            else {
                return null;
            }
        }
        finally {
            connection.disconnect();
        }
    }

    public static String put(String url, String json) throws IOException
    {
        URL obj = new URL(url);

        HttpURLConnection connection = (HttpURLConnection) obj.openConnection();
        try {
            byte[] out = json.getBytes();
            int length = out.length;
            connection.setRequestMethod("PUT");

            connection.setFixedLengthStreamingMode(length);
            connection.setRequestProperty("Content-Type", "application/json; charset=UTF-8");
            connection.connect();

            OutputStream os = connection.getOutputStream();
            os.write(out);

            InputStream in = connection.getInputStream();

            Scanner scanner = new Scanner(in);
            scanner.useDelimiter("\\A");

            boolean hasInput = scanner.hasNext();

            if (hasInput) {
                StringBuilder response = new StringBuilder();

                while(scanner.hasNext()) {
                    response.append(scanner.next());
                }

                return response.toString();
            }
            else {
                return null;
            }
        }
        finally {
            connection.disconnect();
        }
    }

    public String delete(String url) throws IOException
    {
        URL obj = new URL(url);

        HttpURLConnection connection = (HttpURLConnection) obj.openConnection();

        try {
            connection.setRequestMethod("DELETE");

            InputStream in = connection.getInputStream();

            Scanner scanner = new Scanner(in);
            scanner.useDelimiter("\\A");

            boolean hasInput = scanner.hasNext();

            if (hasInput) {
                StringBuilder response = new StringBuilder();

                while(scanner.hasNext()) {
                    response.append(scanner.next());
                }


                return response.toString();
            }
            else {
                return null;
            }
        }
        finally {
            connection.disconnect();
        }
    }

    public void run() {
        try {
            if ("GET".equals(method)) {
                this.response = get(this.url);
            }
            else if ("POST".equals(method)) {
                this.response = post(this.url, this.inJson);
            }

            else if ("PUT".equals(method)) {
                this.response = put(this.url, this.inJson);
            }

            else if ("DELETE".equals(method)) {
                this.response = delete(this.url);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
