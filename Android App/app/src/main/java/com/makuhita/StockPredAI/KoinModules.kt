package com.makuhita.StockPredAI

import com.google.firebase.firestore.FirebaseFirestore
import com.makuhita.StockPredAI.viewmodels.MainViewModel
import org.koin.android.ext.koin.androidContext
import org.koin.androidx.viewmodel.ext.koin.viewModel
import org.koin.dsl.module.module

val mainModule = module {
    viewModel { MainViewModel(androidContext(), FirebaseFirestore.getInstance()) }
}
