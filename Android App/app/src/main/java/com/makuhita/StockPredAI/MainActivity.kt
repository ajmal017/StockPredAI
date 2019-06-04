package com.makuhita.StockPredAI

import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import androidx.viewpager.widget.ViewPager.OnPageChangeListener
import com.google.android.material.bottomnavigation.BottomNavigationView
import com.makuhita.StockPredAI.components.ViewPagerAdapter
import com.makuhita.StockPredAI.viewmodels.MainViewModel
import kotlinx.android.synthetic.main.activity_main.*
import org.koin.androidx.viewmodel.ext.android.viewModel

class MainActivity : AppCompatActivity() {

    val viewModel by viewModel<MainViewModel>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        viewModel.realtimeRequest()

        viewPager.adapter = ViewPagerAdapter(this)
        viewPager.addOnPageChangeListener(object : OnPageChangeListener {
            override fun onPageScrollStateChanged(state: Int) {
                // none
            }

            override fun onPageScrolled(position: Int, positionOffset: Float, positionOffsetPixels: Int) {
                // none
            }

            override fun onPageSelected(position: Int) {
                nav_view.selectedItemId = when (position) {
                    1 -> R.id.navigation_second
                    2 -> R.id.navigation_third
                    3 -> R.id.navigation_fourth
                    else -> R.id.navigation_first
                }
            }
        })

        nav_view.setOnNavigationItemSelectedListener(onNavigationItemSelectedListener)
    }

    private val onNavigationItemSelectedListener = BottomNavigationView.OnNavigationItemSelectedListener { item ->
        when (item.itemId) {
            R.id.navigation_first -> {
                viewPager.currentItem = 0
                return@OnNavigationItemSelectedListener true
            }
            R.id.navigation_second -> {
                viewPager.currentItem = 1
                return@OnNavigationItemSelectedListener true
            }
            R.id.navigation_third -> {
                viewPager.currentItem = 2
                return@OnNavigationItemSelectedListener true
            }
            R.id.navigation_fourth -> {
                viewPager.currentItem = 3
                return@OnNavigationItemSelectedListener true
            }
        }

        false
    }
}
