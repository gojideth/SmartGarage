import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('temperature_data.csv', header=None, names=['Temperature'])

# Data Analysis
# You can perform various data analysis tasks here if needed

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Temperature'], marker='o', linestyle='-')
plt.title('Temperature Data')
plt.xlabel('Sample')
plt.ylabel('Temperature (°C)')
plt.grid(True)

# Display the graph
plt.show()
