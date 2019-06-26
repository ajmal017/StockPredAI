package com.makuhita.StockPredAI.views.adapters

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.makuhita.StockPredAI.R
import com.makuhita.StockPredAI.entities.Stock

class ListViewAdapter internal constructor(context: Context) :
    RecyclerView.Adapter<ListViewAdapter.ViewHolder>() {

    private var layoutInflater = LayoutInflater.from(context)
    private var list = mutableListOf<Stock>()

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val itemView = layoutInflater.inflate(R.layout.list_view_item, parent, false)
        return ViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.setData(list[position])
    }

    override fun getItemCount(): Int {
        return list.size
    }

    fun setList(list: MutableList<Stock>) {
        this.list = list
        notifyDataSetChanged()
    }

    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        fun setData(stock: Stock) {

            itemView.findViewById<TextView>(R.id.tvTitle).text = stock.name
            itemView.findViewById<TextView>(R.id.tvCurrent).text = "$${stock.price}"
            itemView.findViewById<TextView>(R.id.tvPrediction).text = "$${stock.estimate}"
            itemView.findViewById<TextView>(R.id.tvEarning).text = "$${stock.earning}"
        }
    }
}
