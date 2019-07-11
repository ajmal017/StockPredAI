package com.makuhita.StockPredAI.viewmodels.repository

import android.content.Context
import android.util.Log
import android.widget.Toast
import androidx.lifecycle.MutableLiveData
import com.google.firebase.firestore.DocumentChange
import com.google.firebase.firestore.EventListener
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.QuerySnapshot
import com.makuhita.StockPredAI.entities.Price
import com.makuhita.StockPredAI.entities.Stock
import java.util.*

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


                        val stocks = mutableListOf<Stock>()
                        val stock = Stock()

                        stock.symbol = item.document.data["symbol"] as String
                        stock.price = smartCastToDouble(item.document.data["price"])
                        Log.e("asd", stock.price.toString())
                        stock.estimate = smartCastToDouble(item.document.data["estimate"])

                        val prices = mutableListOf<Price>()
                        Log.e("azaza", "got here")
                        for (price in item.document.data["prices"]!! as SortedMap<String, Any>) {
                            val priceMap = price as SortedMap<String, Any>
                            val newPrice = Price()
                            newPrice.open = smartCastToDouble(priceMap["open"])
                            newPrice.close = smartCastToDouble(priceMap["close"])
                            newPrice.high = smartCastToDouble(priceMap["high"])
                            newPrice.low = smartCastToDouble(priceMap["low"])
                            newPrice.volume = (priceMap["volume"] as Long).toInt()
                            prices.add(newPrice)
                            Log.e("azaza", newPrice.toString())
                        }
                        stock.prices = prices

                        stocks.add(stock)
                        this.stocks.value = stocks

                    }
                }
            })
    }

    fun smartCastToDouble(number: Any?): Double {
        return if (number is Long) {
            number.toDouble()
        } else {
            number as Double
        }

    }


}