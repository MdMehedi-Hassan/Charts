import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# Make Plotly open in browser instead of Jupyter
pio.renderers.default = "browser"

# Sample data
categories = ["A", "B", "C", "D"]
group1 = [3, 5, 7, 6]
group2 = [4, 6, 2, 5]
group3 = [2, 3, 5, 4]

# 1. Stacked Bar Chart
plt.figure(figsize=(6,4))
plt.bar(categories, group1, label="Group 1")
plt.bar(categories, group2, bottom=group1, label="Group 2")
plt.bar(categories, group3, bottom=np.array(group1)+np.array(group2), label="Group 3")
plt.title("Stacked Bar Chart")
plt.legend()
plt.show()

# 2. Stacked Area Chart
x = np.arange(1,6)
y1 = [1, 2, 3, 4, 5]
y2 = [2, 2, 3, 2, 3]
y3 = [1, 3, 2, 4, 1]

plt.figure(figsize=(6,4))
plt.stackplot(x, y1, y2, y3, labels=["y1","y2","y3"], alpha=0.8)
plt.title("Stacked Area Chart")
plt.legend()
plt.show()

# DataFrame for Treemap & Sunburst
df = pd.DataFrame({
    "labels": ["World", "Asia", "Europe", "China", "India", "Germany", "France"],
    "parents": ["", "World", "World", "Asia", "Asia", "Europe", "Europe"],
    "values": [100, 60, 40, 30, 30, 20, 20]
})

# 3. Treemap (Plotly)
fig = px.treemap(df, names="labels", parents="parents", values="values", title="Treemap")
fig.show()

# 4. Sunburst Chart (Plotly)
fig = px.sunburst(df, names="labels", parents="parents", values="values", title="Sunburst Chart")
fig.show()

# 5. Waterfall Chart (Plotly)
fig = go.Figure(go.Waterfall(
    name="Financials",
    orientation="v",
    x=["Sales", "Expenses", "Tax", "Profit"],
    y=[1000, -400, -200, 400]
))
fig.update_layout(title="Waterfall Chart")
fig.show()