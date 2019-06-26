package com.makuhita.StockPredAI.entities

data class Stock(
    val name: String,
    val prices: List<Price>,
    val price: Double,
    val estimate: Double,
    val earning: Double
)