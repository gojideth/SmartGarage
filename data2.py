import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('temp.csv', header=None, names=['Temperature'])

statistics = data.describe()

# Create the main GUI window
root = tk.Tk()
root.title("Temperature Data Analysis")
root.geometry("800x600")

# Create a Canvas widget for scrolling
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

# Create a frame inside the canvas to contain all elements
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Create a scrollbar for the canvas
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a function to display statistics in the GUI
def display_statistics():
    stats_text.config(state=tk.NORMAL)
    stats_text.delete(1.0, tk.END)  # Clear any previous content
    stats_text.insert(tk.END, "1. Descriptive Statistics:\n")
    stats_text.insert(tk.END, statistics.to_string())
    stats_text.config(state=tk.DISABLED)

# Create a scrolled text widget to display statistics
stats_text = tk.Text(frame, wrap=tk.NONE, state=tk.DISABLED)
stats_text.pack()

# Create a button to trigger the statistics display
display_button = tk.Button(frame, text="Display Statistics", command=display_statistics)
display_button.pack()

# Create Matplotlib figures and canvas for the plots
fig1 = plt.figure(figsize=(8, 4))
ax1 = fig1.add_subplot(111)
ax1.plot(data.index, data['Temperature'], marker='o', linestyle='-')
ax1.set_title('Temperature Data')
ax1.set_xlabel('Sample')
ax1.set_ylabel('Temperature (°C)')
ax1.grid(True)

canvas1 = FigureCanvasTkAgg(fig1, master=frame)
canvas1_widget = canvas1.get_tk_widget()
canvas1_widget.pack()

# Additional plots can be added here
# Example: Plotting rolling mean
fig2 = plt.figure(figsize=(8, 4))
ax2 = fig2.add_subplot(111)
rolling_mean = data['Temperature'].rolling(window=5).mean()
ax2.plot(data.index, rolling_mean, color='red')
ax2.set_title('Rolling Mean of Temperature')
ax2.set_xlabel('Sample')
ax2.set_ylabel('Temperature (°C)')
ax2.grid(True)

canvas2 = FigureCanvasTkAgg(fig2, master=frame)
canvas2_widget = canvas2.get_tk_widget()
canvas2_widget.pack()

# Function to close the GUI
def close_gui():
    root.quit()
    root.destroy()

# Create a button to close the GUI
close_button = tk.Button(frame, text="Close", command=close_gui)
close_button.pack()

# Update the canvas scroll region
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Start the GUI event loop
root.mainloop()
