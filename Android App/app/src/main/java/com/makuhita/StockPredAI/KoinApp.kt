package com.makuhita.StockPredAI

import androidx.multidex.MultiDexApplication
import org.koin.android.ext.android.startKoin

class KoinApp : MultiDexApplication() {
    override fun onCreate() {
        super.onCreate()
        startKoin(this, listOf(mainModule))
    }
}
