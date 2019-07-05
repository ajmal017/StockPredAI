package com.makuhita.StockPredAI.entities

class Price {
    val open: Double = 0.0
    val close: Double = 0.0
    val high: Double = 0.0
    val low: Double = 0.0
    val volume: Int = 0
    override fun toString(): String {
        return "Price(open=$open, close=$close, high=$high, low=$low, volume=$volume)"
    }
}