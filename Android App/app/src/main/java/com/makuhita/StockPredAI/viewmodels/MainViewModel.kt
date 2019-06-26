package com.makuhita.StockPredAI.viewmodels

import android.content.Context
import android.util.Log
import android.widget.Toast
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.google.firebase.firestore.DocumentChange
import com.google.firebase.firestore.EventListener
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.QuerySnapshot
import com.makuhita.StockPredAI.entities.Price
import com.makuhita.StockPredAI.entities.Stock
import java.util.concurrent.ThreadLocalRandom
import kotlin.math.abs
import kotlin.math.max
import kotlin.math.min
import kotlin.math.round

class MainViewModel(private val context: Context, private val db: FirebaseFirestore) : ViewModel() {

    val stocks = MutableLiveData<MutableList<Stock>>()

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

    fun createFakeDataset() {
        stocks.value = mutableListOf()
        for (i in 0..3) {
            val prices = mutableListOf<Price>()
            for (j in 0..20) {
                val open = ThreadLocalRandom.current().nextDouble(500.0, 2000.0)
                val close = ThreadLocalRandom.current().nextDouble(500.0, 2000.0)
                val high = max(open, close) + ThreadLocalRandom.current().nextDouble(10.0, 100.0)
                val low = min(open, close) - ThreadLocalRandom.current().nextDouble(10.0, 100.0)
                val volume = ThreadLocalRandom.current().nextInt(10, 10000)
                prices.add(Price(open, close, high, low, volume))
            }
            val estimate = prices.last().open + ThreadLocalRandom.current().nextDouble(-500.0, 500.0)

            val name = when (i) {
                0 -> "Amazon"
                1 -> "Apple"
                2 -> "JPMorgan"
                3 -> "Intel Corp"
                else -> "Unknown"
            }

            stocks.value!!.add(
                Stock(
                    name,
                    prices,
                    prices.last().open.round(2),
                    estimate.round(2),
                    abs(estimate - prices.last().open).round(2)
                )
            )
        }
    }

    private fun Double.round(decimals: Int): Double {
        var multiplier = 1.0
        repeat(decimals) { multiplier *= 10 }
        return round(this * multiplier) / multiplier
    }


}
