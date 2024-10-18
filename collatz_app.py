import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def update_graph(*args):
    n = int(scale.get())
    sequence = collatz_sequence(n)
    x = range(len(sequence))
    line.set_data(x, sequence)
    ax.relim()
    ax.autoscale_view()
    canvas.draw()

def search_number():
    number = int(entry.get())
    scale.set(number)
    update_graph()

def log_bool():
    if log_button['text'] == 'Log':
        log_button['text'] = 'Linear'
        ax.set_yscale('log')
    else:
        log_button['text'] = 'Log'
        ax.set_yscale('linear')
    update_graph()

# Create the main window
window = tk.Tk()
window.title("Collatz Conjecture")

# Create a figure and axes for the plot
fig, ax = plt.subplots()
ax.set_xlabel('Iteration')
ax.set_ylabel('Value')
ax.set_title('Collatz Sequence')
line, = ax.plot([], [])
plt.grid(True)

# Create a canvas to display the plot
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().grid(row=0, column=0, columnspan=2, sticky="nsew")

# Create a scroll bar to change the number
scale = tk.Scale(window, from_=1, to=100000, orient=tk.HORIZONTAL, command=update_graph)
scale.set(500)  # Set initial value
scale.grid(row=1, column=0, sticky="ew")

# Create a search bar
entry = tk.Entry(window)
entry.grid(row=1, column=1, padx=5, pady=5)
search_button = tk.Button(window, text="Search", command=search_number)
search_button.grid(row=1, column=2, padx=5)

log_button = tk.Button(window, text="Log", command=lambda: log_bool())
log_button.grid(row=1, column=3, padx=5)

# Configure row and column weights
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Initial graph update
update_graph()

# Function to update graph when mouse is dragged
def on_drag(event):
    update_graph()

# Bind the update function to the mouse drag event
scale.bind("<B1-Motion>", on_drag)

# Run the Tkinter event loop
tk.mainloop()
