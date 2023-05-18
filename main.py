import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Generar datos de ejemplo
x = np.linspace(-5, 5, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Crear la lista de gráficos
figs = []

# Gráfico 1
fig1, ax1 = plt.subplots()
ax1.plot(x, y1)
ax1.set_title('Gráfico de seno')
figs.append(fig1)

# Gráfico 2
fig2, ax2 = plt.subplots()
ax2.plot(x, y2)
ax2.set_title('Gráfico de coseno')
figs.append(fig2)

# Gráfico 3
fig3, ax3 = plt.subplots()
ax3.plot(x, y3)
ax3.set_title('Gráfico de tangente')
figs.append(fig3)

# Índice del gráfico actual
current_fig = 0

# Crear la ventana principal
root = tk.Tk()
root.title('Visualización Interactiva')
root.geometry('800x600')

# Función para cambiar el título del gráfico actual
def set_title(title):
    global figs, current_fig, canvas
    # Cambiar el título del gráfico actual
    figs[current_fig].axes[0].set_title(title)
    # Actualizar la ventana
    canvas.draw()
    root.title('Visualización Interactiva - Gráfico {}'.format(current_fig + 1))

# Crear el objeto FigureCanvasTkAgg para mostrar el gráfico en la ventana
canvas = FigureCanvasTkAgg(figs[current_fig], master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def switch_fig(event):
    global current_fig
    if event.keysym == 'Right':
        current_fig = (current_fig + 1) % len(figs)
    elif event.keysym == 'Left':
        current_fig = (current_fig - 1) % len(figs)
    
    # Actualizar el gráfico mostrado en la ventana
    canvas.figure = figs[current_fig]
    canvas.draw()
    root.title('Visualización Interactiva - Gráfico {}'.format(current_fig + 1))

root.bind('<Key>', switch_fig)

# Mostrar el primer gráfico
root.title('Visualización Interactiva - Gráfico {}'.format(current_fig + 1))

# Crear un campo de texto para ingresar el título del gráfico actual
title_entry = tk.Entry(master=root)
title_entry.pack(side=tk.LEFT, padx=10)

# Función para cambiar el título del gráfico actual
def update_title():
    title = title_entry.get()
    set_title(title)

# Crear un botón para actualizar el título
title_button = tk.Button(master=root, text='Cambiar título', command=update_title)
title_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
