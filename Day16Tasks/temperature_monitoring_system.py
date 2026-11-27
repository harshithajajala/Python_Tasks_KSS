# Temperature Monitoring System .temps = np.array([28, 30, 32, 35, 33, 31, 29]) .days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]. Create DataFrame Plot: 
# Line graph → daily temperature trend.Bar chart → day-wise temperature.Pie chart → proportion of high (>30) vs low temps.Histogram → temperature frequency 
# Scatter plot → day index vs temperature.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

print("Temperature Monitoring Data:")
print(df)
df["Category"] = np.where(
    df["Temperature"] > 30, "High", "Low"
)

print("\nTemperature Categories:")
print(df)
plt.figure(figsize=(7, 5))
plt.plot(days, temps, 'ro-', label="Temperature")
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid()
plt.show()
plt.figure(figsize=(7, 5))
plt.bar(days, temps, color='blue')
plt.title("Day-wise Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.show()
temp_count = df["Category"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    temp_count.values,
    labels=temp_count.index,
    autopct="%1.1f%%",
    explode=(0.1, 0),
    shadow=True,
    startangle=90
)
plt.title("High vs Low Temperature")
plt.axis("equal")
plt.show()
plt.figure(figsize=(7, 5))
plt.hist(temps, bins=5, color='green', edgecolor='black')
plt.title("Temperature Frequency")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()
plt.figure(figsize=(7, 5))
plt.scatter(range(len(temps)), temps, color='purple')
plt.title("Day Index vs Temperature")
plt.xlabel("Day Index")
plt.ylabel("Temperature (°C)")
plt.show()
print("\nTemperature Summary:")
print("Average Temperature:", np.mean(temps))
print("Highest Temperature:", np.max(temps))
print("Lowest Temperature:", np.min(temps))
print("\nTemperature Monitoring Completed!")
