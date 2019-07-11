package com.makuhita.StockPredAI.viewmodels

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.makuhita.StockPredAI.entities.Stock
import com.makuhita.StockPredAI.viewmodels.repository.MainRepository
import kotlin.math.round

class MainViewModel(repository: MainRepository) : ViewModel() {

    var stocks = MutableLiveData<MutableList<Stock>>()

    init {
        stocks = repository.stocks
        repository.startingRequest()
        repository.setupRealTimeListener()
    }
}
