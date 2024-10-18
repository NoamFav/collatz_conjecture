import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
import sympy as sp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def collatz_full_tree(n, depth):
    """
    Create the full decision tree for the Collatz conjecture using symbolic n.
    """
    G = nx.DiGraph()
    current_level = {n}  # Start at the root with symbolic n
    
    for _ in range(depth):
        next_level = set()
        for value in current_level:
            # Symbolically apply the Collatz transformations
            even_branch = value / 2
            G.add_edge(value, even_branch)
            next_level.add(even_branch)
            
            if not (value % 2 == 0):  # If odd, apply 3n + 1 transformation
                odd_branch = 3 * value + 1
                G.add_edge(value, odd_branch)
                next_level.add(odd_branch)
        
        current_level = next_level

    # Use graphviz for layout
    pos = nx.nx_agraph.graphviz_layout(G, prog="twopi")

    # Visualize the symbolic decision tree
    plt.figure(figsize=(12, 12))
    labels = {node: sp.pretty(node) for node in G.nodes()}  # Label with symbolic expressions
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=500, node_color="lightcoral", 
            font_size=10, font_weight='bold', arrows=True)
    plt.title(f"Collatz Full Tree for symbolic n up to depth {depth}", size=15)
    plt.show()

def update_graph():
    try:
        # Get the value for depth from the scale widget
        depth_value = scale.get()
        
        # Use symbolic n from sympy
        n_symbolic = sp.Symbol('n')
        
        # Generate and display the symbolic Collatz tree
        collatz_full_tree(n_symbolic, depth_value)
    
    except ValueError as e:
        print(f"Error: {e}")
        label_error.config(text="Invalid input. Ensure depth is a positive integer and <= 20.")
    
# Create the main window
window = tk.Tk()
window.title("Collatz Reverse Algebraic Tree")

# Slider for depth control (up to 20 million)
tk.Label(window, text="Select depth (max 20):").grid(row=0, column=0, padx=10, pady=5)
scale = tk.Scale(window, from_=1, to=20, orient=tk.HORIZONTAL, length=300)
scale.grid(row=0, column=1, padx=10, pady=5)
scale.set(5)  # Set default depth to 5

# Button to generate graph
generate_button = tk.Button(window, text="Generate Collatz Tree", command=update_graph)
generate_button.grid(row=1, column=1, padx=10, pady=10)

# Error message display
label_error = tk.Label(window, text="", fg="red")
label_error.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
