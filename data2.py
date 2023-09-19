import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('temp.csv', header=None, names=['Temperatura'])

statistics = data.describe()

# Create the main GUI window
root = tk.Tk()
root.title("Análisis de datos de Temperatura")
root.geometry("800x600")

canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)


# Create a Label widget to display statistics
statistics_label = tk.Label(frame, text="Estadísticas:\n" + statistics.to_string(), justify=tk.LEFT, padx=10)
statistics_label.pack()


#Plot 1
fig1 = plt.figure(figsize=(8, 4))
ax1 = fig1.add_subplot(111)
ax1.plot(data.index, data['Temperatura'], marker='o', linestyle='-')
ax1.set_title('Datos de la Temperatura ')
ax1.set_xlabel('Frecuencia')
ax1.set_ylabel('Temperature (°C)')
ax1.grid(True)

canvas1 = FigureCanvasTkAgg(fig1, master=frame)
canvas1_widget = canvas1.get_tk_widget()
canvas1_widget.pack()

#Plot 2: Plotting rolling mean
fig2 = plt.figure(figsize=(8, 4))
ax2 = fig2.add_subplot(111)
rolling_mean = data['Temperatura'].rolling(window=5).mean()
ax2.plot(data.index, rolling_mean, color='red')
ax2.set_title('Media móvil de la Temperatura')
ax2.set_xlabel('Frecuencia')
ax2.set_ylabel('Temperatura (°C)')
ax2.grid(True)

canvas2 = FigureCanvasTkAgg(fig2, master=frame)
canvas2_widget = canvas2.get_tk_widget()
canvas2_widget.pack()

#Plot  3: Histogram
fig3= plt.figure(figsize=(8, 4))
ax3 = fig3.add_subplot(111)
ax3.hist(data['Temperatura'], bins=15, color='blue', alpha=0.7)
ax3.set_title('Temperatura Histograma')
ax3.set_xlabel('Temperatura (°C)')
ax3.set_ylabel('Frecuencia')
ax3.grid(True)

canvas3 = FigureCanvasTkAgg(fig3, master=frame)
canvas3_widget = canvas3.get_tk_widget()
canvas3_widget.pack()






def close_gui():
    root.quit()
    root.destroy()

close_button = tk.Button(frame, text="Cerrar", command=close_gui)
close_button.pack()

frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
