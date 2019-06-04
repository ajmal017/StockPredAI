package com.makuhita.StockPredAI.components

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.viewpager.widget.PagerAdapter
import com.makuhita.StockPredAI.R

class ViewPagerAdapter(private val context: Context) : PagerAdapter() {

    override fun instantiateItem(container: ViewGroup, position: Int): Any {
        val inflater = LayoutInflater.from(context)
        val layout = inflater.inflate(R.layout.adapter_page, container, false) as ViewGroup
        container.addView(layout)
        return layout
    }

    override fun isViewFromObject(view: View, objct: Any): Boolean {
        return view == objct
    }

    override fun getCount(): Int {
        return 4
    }

    override fun destroyItem(container: ViewGroup, position: Int, objct: Any) {
        container.removeView(objct as View)
    }

}
