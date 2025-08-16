import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Sample data
np.random.seed(42)
data = np.random.randn(50)  # 50 random values
categories = ['A', 'B', 'C']
cat_data = pd.DataFrame({
    "Category": np.random.choice(categories, size=50),
    "Value": np.random.randn(50)
})

# 1. Histogram
plt.figure(figsize=(6,4))
plt.hist(data, bins=10, color="skyblue", edgecolor="black")
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 2. Dot Plot
plt.figure(figsize=(6,4))
plt.plot(data, np.zeros_like(data), 'o', color='green')
plt.title("Dot Plot")
plt.xlabel("Value")
plt.yticks([])
plt.show()

# 3. Strip Plot (for categories)
plt.figure(figsize=(6,4))
sns.stripplot(x="Category", y="Value", data=cat_data, jitter=True, palette="Set2", size=8)
plt.title("Strip Plot")
plt.show()

# 4. ECDF (Empirical Cumulative Distribution Function)
sorted_data = np.sort(data)
ecdf = np.arange(1, len(sorted_data)+1) / len(sorted_data)

plt.figure(figsize=(6,4))
plt.step(sorted_data, ecdf, where="post", color="purple")
plt.scatter(sorted_data, ecdf, color="purple")
plt.title("ECDF Plot")
plt.xlabel("Value")
plt.ylabel("ECDF")
plt.show()