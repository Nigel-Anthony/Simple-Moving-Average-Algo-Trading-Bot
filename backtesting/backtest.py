import matplotlib.pyplot as plt


def backtest_strategy(data):
    data["Returns"] = data["Close"].pct_change()
    data["Strategy_Returns"] = data["Returns"] * data["Signal"].shift(1)
    data["Cumulative_Returns"] = (1 + data["Strategy_Returns"]).cumprod()
    return data


def plot_backtest(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data["Cumulative_Returns"], label="Strategy Cumulative Returns")
    plt.title("Backtested Strategy Performance")
    plt.xlabel("Date")
    plt.ylabel("Cumulative_Returns")
    plt.legend()
    plt.show()
