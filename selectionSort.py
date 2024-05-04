import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            yield arr, j, min_idx, i  
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr, min_idx, i, i  
def update(data):
    bars, selected, min_idx, fixed = data
    ax.clear()
    bar_colors = ['#1f77b4' if x > fixed else 'orange' if x == min_idx else 'green' if x == selected else 'grey' for x in range(len(bars))]
    ax.bar(range(len(bars)), bars, color=bar_colors)
    ax.set_title("Selection Sort Visualization")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")

# Generate random data
data = np.random.randint(1, 100, 25)


fig, ax = plt.subplots()
bars = plt.bar(range(len(data)), data, color='grey')

ani = FuncAnimation(fig, func=update, frames=selection_sort(data), repeat=False, blit=False, interval=200)

plt.show()