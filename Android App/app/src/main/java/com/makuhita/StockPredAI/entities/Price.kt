package com.makuhita.StockPredAI.entities

data class Price(
    val open: Double,
    val close: Double,
    val high: Double,
    val low: Double,
    val volume: Int
)