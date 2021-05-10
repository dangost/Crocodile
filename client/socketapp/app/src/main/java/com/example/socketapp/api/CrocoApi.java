package com.example.socketapp.api;

import androidx.annotation.Nullable;

import com.example.socketapp.LobbyCard;
import com.example.socketapp.User;
import com.google.gson.Gson;

import java.util.ArrayList;

public class CrocoApi {

    String ip = "http://127.0.0.1:5000";
    int port = 8080;

    // <routes>
    Gson gson;

    public CrocoApi()
    {
        gson = new Gson();
    }

    public ArrayList<LobbyCard> allLobbies()
    {
        String route = "/api/lobbies/";

        Requests requests = new Requests();
        requests.url = ip + route;
        requests.method = "GET";

        requests.start();
        try {
            requests.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        String json = requests.response;

        return null;
    }

    public ArrayList<User> allUsers()
    {
        String route = "/api/users/";

        Requests requests = new Requests();
        requests.url = ip + route;
        requests.method = "GET";

        requests.start();
        try {
            requests.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        String json = requests.response;

        return null;
    }

    public LobbyCard lobbyById(String lobbyId)
    {

        String route = "/api/lobbies/" + lobbyId + "/";

        Requests requests = new Requests();
        requests.url = ip + route;
        requests.method = "GET";

        requests.start();
        try {
            requests.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        String json = requests.response;

        return null;
    }

    public User userById(String userId)
    {
        String route = "/api/users/" + userId + "/";

        Requests requests = new Requests();
        requests.url = ip + route;
        requests.method = "GET";

        requests.start();
        try {
            requests.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        String json = requests.response;

        return null;
    }

    public Integer userJoin(String userId, String lobbyId)
    {
        String route = "/api/lobbies/"+ lobbyId + "/players/" + userId + "/join";

        Requests requests = new Requests();
        requests.url = ip + route;
        requests.method = "GET";

        requests.start();
        try {
            requests.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        String json = requests.response;

        return null;
    }

    public Integer userQuit(String userId, String lobbyId)
    {
        String route = "/api/lobbies/"+ lobbyId + "/players/" + userId + "/quit";

        Requests requests = new Requests();
        requests.url = ip + route;
        requests.method = "GET";

        requests.start();
        try {
            requests.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        String json = requests.response;

        return null;
    }

    public User createUser(User user)
    {
        String route = "/api/users/new/" + user.nickname + "/" + user.avatarId + "/";
        Requests requests = new Requests();
        requests.url = ip + route;
        requests.method = "GET";


        requests.start();
        try {
            requests.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        String json = requests.response;

        return null;
    }

    public LobbyCard createLobby(String lobbyName, @Nullable String lobbyPass, Integer maxPlayers)
    {
        if(lobbyPass == null)
        {
            lobbyPass = "null";
        }
        String route = "/api/lobbies/"+ lobbyName+ "/"  + lobbyPass + "/"  + maxPlayers+ "/";
        Requests requests = new Requests();
        requests.url = ip + route;
        requests.method = "GET";

        requests.start();
        try {
            requests.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        String json = requests.response;

        return null;
    }

    public ArrayList<String> lobbyPlayers(String lobbyId)
    {
        String route = "/api/lobbies/" + lobbyId + "/players";
        Requests requests = new Requests();
        requests.url = ip + route;
        requests.method = "GET";

        requests.start();
        try {
            requests.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        String json = requests.response;

        return null;
    }


    // </routes>

    public void initApi(String _ip, Integer _port)
    {
        this.ip = _ip != null ? _ip : ip;
        this.port = _port != null ? _port : _port;
    }

}
