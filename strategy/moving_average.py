import pandas as pd


def calculate_moving_averages(data, short_window=40, long_window=100):
    data["SMA_short"] = data["Close"].rolling(window=short_window, min_periods=1).mean()
    data["SMA_long"] = data["Close"].rolling(window=long_window, min_periods=1).mean()
    return data


def generate_signals(data, short_window=40):
    data.loc[data.index[short_window:], "Signal"] = (
        data.loc[data.index[short_window:], "SMA_short"]
        > data.loc[data.index[short_window:], "SMA_long"]
    ).astype(int)
    data["Signal"].fillna(0, inplace=True)
    data["Position"] = data["Signal"].diff()
    return data
