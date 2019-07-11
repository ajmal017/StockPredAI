package com.makuhita.StockPredAI.views.adapters

import android.content.Context
import android.graphics.Paint
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.github.mikephil.charting.charts.CandleStickChart
import com.github.mikephil.charting.data.CandleData
import com.github.mikephil.charting.data.CandleDataSet
import com.github.mikephil.charting.data.CandleEntry
import com.makuhita.StockPredAI.R
import com.makuhita.StockPredAI.entities.Stock
import kotlin.math.abs

class ListViewAdapter internal constructor(private val context: Context) :
    RecyclerView.Adapter<ListViewAdapter.ViewHolder>() {

    private var layoutInflater = LayoutInflater.from(context)
    private var list = mutableListOf<Stock>()

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val itemView = layoutInflater.inflate(R.layout.list_view_item, parent, false)
        return ViewHolder(itemView, context)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.setData(list[position])
    }

    override fun getItemCount(): Int {
        return list.size
    }

    fun setList(list: MutableList<Stock>) {
        Log.e("List in adapter", list.toString())
        this.list = list
        notifyDataSetChanged()
    }

    class ViewHolder(itemView: View, val context: Context) : RecyclerView.ViewHolder(itemView) {
        fun setData(stock: Stock) {

            itemView.findViewById<TextView>(R.id.tvTitle).text = stock.symbol
            itemView.findViewById<TextView>(R.id.tvCurrent).text = "$${stock.price}"
            itemView.findViewById<TextView>(R.id.tvPrediction).text = "$${stock.estimate.round(2)}"
            itemView.findViewById<TextView>(R.id.tvEarning).text = "$${abs(stock.estimate - stock.price).round(2)}"

            val chart = itemView.findViewById<CandleStickChart>(R.id.chart)
            chart.isHighlightPerTapEnabled = true
            chart.setViewPortOffsets(0f, 0f, 0f, 0f)
            chart.description = null

            val yAxis = chart.axisLeft
            val rightAxis = chart.axisRight
            chart.requestDisallowInterceptTouchEvent(true)

            val xAxis = chart.xAxis
            rightAxis.textColor = android.R.color.white
            yAxis.setDrawLabels(false)
            xAxis.granularity = 1f
            xAxis.isGranularityEnabled = true
            xAxis.setAvoidFirstLastClipping(true)

            val legend = chart.legend
            legend.isEnabled = false

            val chartValues = mutableListOf<CandleEntry>()

            for (i in 0 until stock.prices.size) {
                val prices = stock.prices[i]
                chartValues.add(
                    CandleEntry(
                        i.toFloat(), prices.high.toFloat(),
                        prices.low.toFloat(), prices.open.toFloat(), prices.close.toFloat()
                    )
                )
            }

            val candleDataSet = CandleDataSet(chartValues, "DataSet")
            candleDataSet.color = context.resources.getColor(R.color.colorDarkGray)
            candleDataSet.shadowColor = context.resources.getColor(R.color.colorLightGray)
            candleDataSet.shadowWidth = 0.8f
            candleDataSet.decreasingColor = context.resources.getColor(R.color.colorRed)
            candleDataSet.decreasingPaintStyle = Paint.Style.FILL
            candleDataSet.increasingColor = context.resources.getColor(R.color.colorGreen)
            candleDataSet.increasingPaintStyle = Paint.Style.FILL
            candleDataSet.neutralColor = context.resources.getColor(R.color.colorLightGray)
            candleDataSet.setDrawValues(false)

            chart.data = CandleData(candleDataSet)
            chart.invalidate()

            chart.animateX(1000)
        }

        private fun Double.round(decimals: Int): Double {
            var multiplier = 1.0
            repeat(decimals) { multiplier *= 10 }
            return kotlin.math.round(this * multiplier) / multiplier
        }

    }
}
