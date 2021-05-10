package com.example.socketapp;

import androidx.annotation.Nullable;

import java.util.List;

public class LobbyCard {
    public String lobbyId;
    public String lobbyName;
    public String lobbyPass;
    public List<String> lobbyPlayers;
    public int maxPlayers;
    public int currentPlayers;


    public LobbyCard(String lobbyName, int maxPlayers, @Nullable String password){
        this.lobbyName = lobbyName;
        this.lobbyPass = password;
        this.maxPlayers = maxPlayers;
        this.currentPlayers = 0;
    }

    public String getLobbyName() {
        return lobbyName;
    }

    public String getPlayersCount(){
        return  Integer.toString(currentPlayers) + "/" + Integer.toString(maxPlayers);
    }

    public boolean isPrivate(){
        return lobbyPass != null;
    }

    public boolean checkPassword(String input){
        return input == lobbyPass || lobbyPass == null;
    }
}
