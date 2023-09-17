import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('temp.csv', header=None, names=['Temperature'])

# Data Analysis

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Temperature'], marker='o', linestyle='-')
plt.title('Temperature Data')
plt.xlabel('Sample')
plt.ylabel('Temperature (°C)')
plt.grid(True)

plt.show()
