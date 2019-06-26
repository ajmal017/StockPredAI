package com.makuhita.StockPredAI.views

import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.lifecycle.Observer
import androidx.recyclerview.widget.GridLayoutManager
import com.makuhita.StockPredAI.R
import com.makuhita.StockPredAI.viewmodels.MainViewModel
import com.makuhita.StockPredAI.views.adapters.ListViewAdapter
import kotlinx.android.synthetic.main.fragment_main.*
import kotlinx.android.synthetic.main.list_view_item.*
import org.koin.androidx.viewmodel.ext.android.viewModel

class MainFragment : Fragment() {

    private val viewModel by viewModel<MainViewModel>()
    private var adapter: ListViewAdapter? = null

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_main, container, false)
    }


    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        adapter = ListViewAdapter(context!!)
        lvStocks.adapter = adapter

        lvStocks.setHasFixedSize(true)
        val layoutManager = GridLayoutManager(context!!, 1)
        lvStocks.layoutManager = layoutManager

        viewModel.stocks.observe(this, Observer {
            adapter!!.setList(viewModel.stocks.value!!)
        })

        viewModel.createFakeDataset()
    }

}
