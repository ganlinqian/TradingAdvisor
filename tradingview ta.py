from tradingview_ta import TA_Handler, Interval, Exchange

import PySimpleGUI as sg
#reference to https://tvdb.brianthe.dev/ for list of symbols on tradingview
symbols = ["BTCUSDT","ETHUSDT"]
SCREENER = "crypto"
EXCHANGE = "COINBASE"
def TA(symbol, screener, exchange):
    result = ""
    for item in ["1m","5m","15m","1h","4h"]:
        stock = TA_Handler(
            symbol=symbol,
            screener=screener,
            exchange=exchange,
            interval=item
        )
        temp  = stock.get_analysis().summary
        suggest = temp.get("RECOMMENDATION")
        buy = temp.get("BUY")
        sell = temp.get("SELL")
        neutral = temp.get("NEUTRAL")
        result = result + item+ ": "+suggest +", "+ str(buy) +", "+str(sell) +", "+ str(neutral) +"; "
    return result

def crypto(text):
    return [sg.Text(text), sg.Text(TA(text,SCREENER,EXCHANGE),key=text)]

layout = []
for item in symbols:
    layout.append(crypto(item))
# Create the window

window = sg.Window("TA", layout)
while (True):
    # --------- Read and update window --------
    
    event, values = window.read(timeout=5000)
    for i in symbols:
        window[i].update(TA(i,SCREENER,EXCHANGE))
event, values = window.read()

