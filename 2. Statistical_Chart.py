import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=200)  # Normal distribution

# 1. Histogram
plt.figure(figsize=(6,4))
plt.hist(data, bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 2. Box Plot (Whisker Plot)
plt.figure(figsize=(6,4))
sns.boxplot(x=data, color="lightgreen")
plt.title("Box Plot")
plt.show()

# 3. Violin Plot
plt.figure(figsize=(6,4))
sns.violinplot(x=data, color="lightcoral")
plt.title("Violin Plot")
plt.show()

# 4. Density Plot (KDE)
plt.figure(figsize=(6,4))
sns.kdeplot(data, fill=True, color="purple", alpha=0.5)
plt.title("Density Plot")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()