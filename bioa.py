import yfinance as yf
import time

bioa_old = yf.Ticker("BIOA-B.ST")
print(f"[{time.strftime('%H:%M:%S', time.localtime())}] Tjena Hannes! BIOA ligger just nu på {round(bioa_old.fast_info['lastPrice'], 2)}")
while True:
    bioa_new = yf.Ticker("BIOA-B.ST")
    if round(bioa_new.fast_info['lastPrice'], 2) < round(bioa_old.fast_info['lastPrice'], 2):
        print(f"[{time.strftime('%H:%M:%S', time.localtime())}] Tjena Hannes, din cp idiot till världens sämsta sparare! BIOA har nu gått ner till {round(bioa_new.fast_info['lastPrice'], 2)}")
        bioa_old = bioa_new
    time.sleep(10)