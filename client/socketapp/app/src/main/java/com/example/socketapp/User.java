package com.example.socketapp;

import android.content.SharedPreferences;

public class User {
    public String nickname;
    public String id;
    public int avatarId;

    public void setAvatarId(int id1, SharedPreferences.Editor editor){
        avatarId = id1;

        editor.putInt("AvatarId", id1);
    }

    public void setNickname(String nickname1, SharedPreferences.Editor editor){
        nickname = nickname1;

        editor.putString("Nickname", nickname1);
    }
}
