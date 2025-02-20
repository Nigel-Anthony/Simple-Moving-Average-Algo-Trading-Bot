import yfinance as yf
import matplotlib.pyplot as plt
from strategy import moving_average
from backtesting import backtest


def main():
    ticker = "MSFT"
    data = yf.download(ticker, start="2020-01-01", end="2021-01-01")

    data = moving_average.calculate_moving_averages(data)
    data = moving_average.generate_signals(data)

    plt.figure(figsize=(12, 6))
    plt.plot(data["Close"], label="Close Price", alpha=0.5)
    plt.plot(data["SMA_short"], label="40 day Moving Average", alpha=0.75)
    plt.plot(data["SMA_long"], label="100 day Moving Average", alpha=0.75)
    plt.plot(
        data.loc[data["Position"] == 1].index,
        data["SMA_short"][data["Position"] == 1],
        "^",
        markersize=10,
        color="g",
        label="Buy Signal",
    )
    plt.plot(
        data.loc[data["Position"] == -1].index,
        data["SMA_short"][data["Position"] == -1],
        "v",
        markersize=10,
        color="r",
        label="Sell Signal",
    )

    plt.title("Moving Average Crossover Startegy")
    plt.xlabel("Date")
    plt.legend()
    plt.show()

    data = backtest.backtest_strategy(data)
    backtest.plot_backtest(data)


if __name__ == "__main__":
    main()
