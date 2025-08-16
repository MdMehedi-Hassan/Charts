import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Sample data
np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.randint(50, 500, 50)

# 1. Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(x, y, color="blue", alpha=0.7)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# 2. Bubble Chart (Scatter + size)
plt.figure(figsize=(6,4))
plt.scatter(x, y, s=sizes, alpha=0.5, color="green")
plt.title("Bubble Chart")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# 3. Heatmap (matrix of values)
data = np.random.rand(6,6)
plt.figure(figsize=(6,4))
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("Heatmap")
plt.show()

# 4. Pair Plot (Scatterplot Matrix)
df = sns.load_dataset("iris")  # iris dataset with multiple features
sns.pairplot(df, hue="species")
plt.show()