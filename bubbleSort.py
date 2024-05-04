import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield arr, j, j+1, i 
        

def update(data):
    bars, selected, min_idx, fixed = data
    ax.clear()
    bar_colors = ['grey' if x > len(bars)-fixed-1 else 'orange' if x == min_idx else 'green' if x == selected else '#1f77b4' for x in range(len(bars))]
    ax.bar(range(len(bars)), bars, color=bar_colors)
    ax.set_title("Bubble Sort Visualization")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")

# Generate random data
data = np.random.randint(1, 100, 25)

fig, ax = plt.subplots()
bars = plt.bar(range(len(data)), data, color='grey')

ani = FuncAnimation(fig, func=update, frames=bubble_sort(data), repeat=False, blit=False, interval=200)

plt.show()
