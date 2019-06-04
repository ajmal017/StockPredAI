package com.makuhita.StockPredAI.viewmodels

import android.content.Context
import android.util.Log
import android.widget.Toast
import androidx.lifecycle.ViewModel
import com.google.firebase.firestore.DocumentChange
import com.google.firebase.firestore.EventListener
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.QuerySnapshot

class MainViewModel(private val context: Context, private val db: FirebaseFirestore) : ViewModel() {

    fun request() {
        db.collection("alerts")
            .get()
            .addOnCompleteListener {
                if (it.isSuccessful) {
                    for (item in it.result!!) {
                        Log.e("Success", item.id + " " + item.data)
                    }
                } else {
                    Log.e("Error", it.exception.toString())
                }
            }
    }

    fun realtimeRequest() {
        db.collection("alerts")
            .addSnapshotListener(EventListener<QuerySnapshot> { value, e ->
                if (e != null) {
                    Toast.makeText(context, "Listening Error", Toast.LENGTH_SHORT).show()
                    return@EventListener
                }

                for (item in value!!.documentChanges) {
                    if (item.type == DocumentChange.Type.MODIFIED) {
                        Toast.makeText(context, "${item.document.data["name"]}", Toast.LENGTH_SHORT).show()
                    }
                }
            })
    }

}
