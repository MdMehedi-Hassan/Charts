import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import networkx as nx

# -------------------------------
# 1. Radar (Spider) Chart
categories = ['Speed', 'Reliability', 'Comfort', 'Safety', 'Efficiency']
values = [4, 3, 5, 4, 2]

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
values_loop = values + values[:1]  # close the loop
angles_loop = angles + angles[:1]

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, polar=True)
ax.plot(angles_loop, values_loop, 'o-', linewidth=2)
ax.fill(angles_loop, values_loop, alpha=0.25)
ax.set_thetagrids(np.degrees(angles), categories)
ax.set_title("Radar Chart")
plt.show()

# -------------------------------
# 2. Polar Area Chart
values = np.array([5, 3, 6, 2, 4])
categories = ['A', 'B', 'C', 'D', 'E']
angles = np.linspace(0, 2 * np.pi, len(values), endpoint=False)
colors = plt.cm.viridis(values / values.max())

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, polar=True)
bars = ax.bar(angles, values, color=colors, alpha=0.7)
ax.set_xticks(angles)
ax.set_xticklabels(categories)
ax.set_title("Polar Area Chart")
plt.show()

# -------------------------------
# 3. Gantt Chart (Plotly)
df = pd.DataFrame([
    dict(Task="Task A", Start='2025-08-01', Finish='2025-08-05'),
    dict(Task="Task B", Start='2025-08-03', Finish='2025-08-09'),
    dict(Task="Task C", Start='2025-08-07', Finish='2025-08-12')
])
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", title="Gantt Chart")
fig.update_yaxes(autorange="reversed")
fig.show()

# -------------------------------
# 4. Sankey Diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(label=["Input A", "Input B", "Output X", "Output Y"], color=["blue","green","orange","red"]),
    link=dict(source=[0, 1, 0], target=[2, 3, 3], value=[8, 4, 2])
)])
fig.update_layout(title="Sankey Diagram", font_size=12)
fig.show()

# -------------------------------
# 5. Funnel Chart
fig = go.Figure(go.Funnel(
    y=["Stage 1", "Stage 2", "Stage 3", "Stage 4"],
    x=[1000, 800, 500, 200]
))
fig.update_layout(title="Funnel Chart")
fig.show()

# -------------------------------
# 6. Network Graph
G = nx.Graph()
G.add_edges_from([("A","B"),("A","C"),("B","C"),("C","D"),("D","E")])
plt.figure(figsize=(6,6))
nx.draw(G, with_labels=True, node_color="skyblue", edge_color="gray", node_size=1000)
plt.title("Network Graph")
plt.show()

# -------------------------------
# 7. Chord Diagram (Approximation using Sankey)
labels = ["Group 1", "Group 2", "Group 3", "Group 4"]
fig = go.Figure(data=[go.Sankey(
    arrangement="fixed",
    node=dict(label=labels, color=["#FF5733","#33FF57","#3357FF","#F3FF33"]),
    link=dict(source=[0,0,1,2], target=[1,2,3,3], value=[8,4,2,6])
)])
fig.update_layout(title="Chord Diagram (Approx.)")
fig.show()

# -------------------------------
# 8. Parallel Coordinates Plot
df = pd.DataFrame({
    'Var1': np.random.rand(10),
    'Var2': np.random.rand(10),
    'Var3': np.random.rand(10),
    'Var4': np.random.rand(10)
})
fig = px.parallel_coordinates(df, title="Parallel Coordinates Plot")
fig.show()