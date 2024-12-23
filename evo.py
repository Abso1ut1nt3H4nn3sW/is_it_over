import yfinance as yf
from time import strftime, localtime, sleep

def get_new_price(stock):
    """
    Get current stock price
    """
    ticker = yf.Ticker(stock)
    current_price = ticker.fast_info['lastPrice']
    return round(current_price, 2)

def main():
    """
    Check if it is over or if we won, every ten seconds.
    """
    evo_low = get_new_price("EVO.ST")
    evo_high = evo_low
    current_time = strftime('%H:%M:%S', localtime())
    print(f"[{current_time}] Tjena Jojje! EVO just nu på: {evo_low}\n")
    while True:
        evo_new = get_new_price("EVO.ST")
        if evo_new < evo_low:
            current_time = strftime('%H:%M:%S', localtime())
            print(f"[{current_time}] Jojje bros... It's over")
            print(f"EVO just nu på: {evo_new}\n")
            evo_low = evo_new
        elif evo_new > evo_high:
            current_time = strftime('%H:%M:%S', localtime())
            print(f"[{current_time}] Jojje bros... We won!")
            print(f"EVO just nu på: {evo_new}\n")
            evo_high = evo_new
        sleep(10)

if __name__ == "__main__":
    main()
