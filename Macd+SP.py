
//@version=3
study("Support & Resistance", overlay=true)
 
left = 50
right = 25
quick_right = 5 
 
pivot_high = pivothigh(high,left,right)
pivot_lows = pivotlow(low, left,right)
 
quick_pivot_high = pivothigh(high,left,quick_right)
quick_pivot_lows = pivotlow(low, left,quick_right)
 
level1 = valuewhen(quick_pivot_high, high[quick_right], 0)
level2 = valuewhen(quick_pivot_lows, low[quick_right], 0)
level3 = valuewhen(pivot_high, high[right], 0)
level4 = valuewhen(pivot_lows, low[right], 0)
level5 = valuewhen(pivot_high, high[right], 1)
level6 = valuewhen(pivot_lows, low[right], 1)
level7 = valuewhen(pivot_high, high[right], 2)
level8 = valuewhen(pivot_lows, low[right], 2)
 
level1_col = close >= level1 ? green : red
level2_col = close >= level2 ? green : red
level3_col = close >= level3 ? green : red
level4_col = close >= level4 ? green : red
level5_col = close >= level5 ? green : red
level6_col = close >= level6 ? green : red
level7_col = close >= level7 ? green : red
level8_col = close >= level8 ? green : red
 
plot(level1, style=circles, color=level1_col, show_last=1, linewidth=1, trackprice=true)
plot(level2, style=circles, color=level2_col, show_last=1, linewidth=1, trackprice=true)
plot(level3, style=circles, color=level3_col, show_last=1, linewidth=1, trackprice=true)
plot(level4, style=circles, color=level4_col, show_last=1, linewidth=1, trackprice=true)
plot(level5, style=circles, color=level5_col, show_last=1, linewidth=1, trackprice=true)
plot(level6, style=circles, color=level6_col, show_last=1, linewidth=1, trackprice=true)
plot(level7, style=circles, color=level7_col, show_last=1, linewidth=1, trackprice=true)
plot(level8, style=circles, color=level8_col, show_last=1, linewidth=1, trackprice=true)

source = close
smd = input(true, title="Show MacD & Signal Line? Also Turn Off Dots Below")
sd = input(true, title="Show Dots When MacD Crosses Signal Line?")
sh = input(true, title="Show Histogram?")
macd_colorChange = input(true,title="Change MacD Line Color-Signal Line Cross?")
hist_colorChange = input(true,title="MacD Histogram 4 Colors?")


fastLength = input(12, minval=1), slowLength=input(26,minval=1)
signalLength=input(9,minval=1)

fastMA = ema(source, fastLength)
slowMA = ema(source, slowLength)

macd = fastMA - slowMA
signal = sma(macd, signalLength)
hist = macd - signal

outMacD = macd
outSignal = signal
outHist = hist

histA_IsUp = outHist > outHist[1] and outHist > 0
histA_IsDown = outHist < outHist[1] and outHist > 0
histB_IsDown = outHist < outHist[1] and outHist <= 0
histB_IsUp = outHist > outHist[1] and outHist <= 0


macd_IsAbove = outMacD >= outSignal
macd_IsBelow = outMacD < outSignal

plot_color = hist_colorChange ? histA_IsUp ? aqua : histA_IsDown ? blue : histB_IsDown ? red : histB_IsUp ? maroon :yellow :gray
macd_color = macd_colorChange ? macd_IsAbove ? lime : red : red
signal_color = macd_colorChange ? macd_IsAbove ? yellow : yellow : lime

circleYPosition = outSignal
 
plot(smd and outMacD ? outMacD : na, title="MACD", color=macd_color, linewidth=4)
plot(smd and outSignal ? outSignal : na, title="Signal Line", color=signal_color, style=line ,linewidth=2)
plot(sh and outHist ? outHist : na, title="Histogram", color=plot_color, style=histogram, linewidth=4)
plot(sd and cross(outMacD, outSignal) ? circleYPosition : na, title="Cross", style=circles, linewidth=4, color=macd_color)
hline(0, '0 Line', linestyle=solid, linewidth=2, color=white)