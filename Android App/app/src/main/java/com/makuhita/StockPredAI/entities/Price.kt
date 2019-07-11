package com.makuhita.StockPredAI.entities

class Price {
    var open: Double = 0.0
    var close: Double = 0.0
    var high: Double = 0.0
    var low: Double = 0.0
    var volume: Int = 0
    override fun toString(): String {
        return "Price(open=$open, close=$close, high=$high, low=$low, volume=$volume)"
    }
}