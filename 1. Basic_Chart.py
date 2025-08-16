import matplotlib.pyplot as plt

# Sample data
categories = ["A", "B", "C", "D"]
values = [10, 15, 7, 12]

# 1. Bar Chart (Horizontal)
plt.figure(figsize=(6,4))
plt.barh(categories, values, color="skyblue")
plt.title("Bar Chart")
plt.show()

# 2. Column Chart (Vertical Bar)
plt.figure(figsize=(6,4))
plt.bar(categories, values, color="lightgreen")
plt.title("Column Chart")
plt.show()

# 3. Line Chart
plt.figure(figsize=(6,4))
plt.plot(categories, values, marker="o", color="blue")
plt.title("Line Chart")
plt.show()

# 4. Area Chart
plt.figure(figsize=(6,4))
plt.fill_between(categories, values, color="lightcoral", alpha=0.6)
plt.plot(categories, values, color="red")
plt.title("Area Chart")
plt.show()

# 5. Pie Chart
plt.figure(figsize=(6,6))
plt.pie(values, labels=categories, autopct="%1.1f%%", colors=["gold","lightblue","lightgreen","salmon"])
plt.title("Pie Chart")
plt.show()

# 6. Doughnut Chart (Pie with a hole)
plt.figure(figsize=(6,6))
wedges, texts, autotexts = plt.pie(values, labels=categories, autopct="%1.1f%%")
# Draw circle for doughnut
centre_circle = plt.Circle((0,0), 0.70, fc="white")
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()