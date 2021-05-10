package com.example.socketapp;

import android.os.AsyncTask;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import java.io.IOException;
import java.net.Socket;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.navigation.fragment.NavHostFragment;

import com.example.socketapp.api.CrocoApi;
import com.example.socketapp.api.Requests;

public class FirstFragment extends Fragment {

    public static Socket socket;
    public static String ip = "77.223.97.149";
    public static int port = 9091;
    @Override
    public View onCreateView(
            LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState
    ) {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_first, container, false);
    }

    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        view.findViewById(R.id.button_first).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                CrocoApi api = new CrocoApi();
                Object n = api.allLobbies();
                LobbyCard lobby = new LobbyCard("TestLobby", 5, null);

                lobby = api.createLobby("lobby", null, 5);



                NavHostFragment.findNavController(FirstFragment.this)
                        .navigate(R.id.action_FirstFragment_to_SecondFragment);
            }
        });
    }
}

class ConnectionTask extends AsyncTask<Void, Void, Void> {
    @Override
    protected Void doInBackground(Void... params)
    {
        try {
            FirstFragment.socket = new Socket(FirstFragment.ip, FirstFragment.port);
            System.out.println("Connected");
        } catch (IOException e) {
            System.out.println("Connection Failed");
        }

        return null;
    }
}