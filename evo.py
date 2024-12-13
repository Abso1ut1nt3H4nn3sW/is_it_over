import yfinance as yf
import time

evo_old = yf.Ticker("EVO.ST")
print(f"[{time.strftime('%H:%M:%S', time.localtime())}] Tjena Jojje! EVO ligger just nu på {round(evo_old.fast_info['lastPrice'], 2)}")
while True:
    evo_new = yf.Ticker("EVO.ST")
    if round(evo_new.fast_info['lastPrice'], 2) < round(evo_old.fast_info['lastPrice'], 2):
        print(f"[{time.strftime('%H:%M:%S', time.localtime())}] Tjena Jojje! EVO har nu gått ner till {round(evo_new.fast_info['lastPrice'], 2)}")
        evo_old = evo_new
    time.sleep(10)