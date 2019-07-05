package com.makuhita.StockPredAI.viewmodels.repository

import android.content.Context
import android.util.Log
import android.widget.Toast
import androidx.lifecycle.MutableLiveData
import com.google.firebase.firestore.DocumentChange
import com.google.firebase.firestore.EventListener
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.QuerySnapshot
import com.makuhita.StockPredAI.entities.Stock

class MainRepository(private val context: Context, private val db: FirebaseFirestore) {

    val stocks = MutableLiveData<MutableList<Stock>>()

    fun startingRequest() {
        db.collection("stocks")
            .get()
            .addOnCompleteListener {
                if (it.isSuccessful) {

                    val stocks = mutableListOf<Stock>()
                    for (item in it.result!!) {
                        stocks.add(item.toObject(Stock::class.java))
                    }

                    this.stocks.value = stocks
                } else {
                    Log.e("Error", it.exception.toString())
                }
            }
    }

    fun setupRealTimeListener() {
        db.collection("stocks")
            .addSnapshotListener(EventListener<QuerySnapshot> { value, e ->
                if (e != null) {
                    Toast.makeText(context, "Listening Error", Toast.LENGTH_SHORT).show()
                    return@EventListener
                }

                for (item in value!!.documentChanges) {
                    if (item.type == DocumentChange.Type.MODIFIED) {
                        Log.e("Error", "${item.document}")
                    }
                }
            })
    }


}