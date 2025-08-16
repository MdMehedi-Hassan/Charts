import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Make Plotly open in browser
pio.renderers.default = "browser"

# Sample time-series data
np.random.seed(42)
dates = pd.date_range("2023-01-01", periods=20)
values = np.cumsum(np.random.randn(20))

# 1. Time Series Line Chart
plt.figure(figsize=(8,4))
plt.plot(dates, values, marker="o", color="blue")
plt.title("Time Series Line Chart")
plt.xlabel("Date")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Candlestick Chart (Plotly, with consistent OHLC data)
open_prices = np.random.randint(80, 100, 20)
close_prices = open_prices + np.random.randint(-10, 10, 20)
high_prices = np.maximum(open_prices, close_prices) + np.random.randint(1, 10, 20)
low_prices = np.minimum(open_prices, close_prices) - np.random.randint(1, 10, 20)

candlestick = go.Figure(data=[go.Candlestick(
    x=dates,
    open=open_prices,
    high=high_prices,
    low=low_prices,
    close=close_prices
)])
candlestick.update_layout(title="Candlestick Chart")
candlestick.show()

# 3. Sparkline (tiny line chart, no axes)
plt.figure(figsize=(4,1))
plt.plot(values, color="red", linewidth=2)
plt.axis("off")
plt.title("Sparkline", fontsize=10)
plt.show()

# 4. Streamgraph (stacked area over time)
t = np.arange(20)
y1 = np.sin(t/3) + 2
y2 = np.cos(t/3) + 2
y3 = np.random.rand(20) + 1

plt.figure(figsize=(8,4))
plt.stackplot(t, y1, y2, y3, labels=["Series A", "Series B", "Series C"], alpha=0.8)
plt.legend(loc="upper left")
plt.title("Streamgraph (Stacked Area)")
plt.show()