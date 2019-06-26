package com.makuhita.StockPredAI

import android.app.Application
//import androidx.multidex.MultiDexApplication
import org.koin.android.ext.android.startKoin
import org.koin.standalone.StandAloneContext.startKoin

class KoinApp : Application() {
    override fun onCreate() {
        super.onCreate()
        startKoin(this, listOf(mainModule))
    }
}
