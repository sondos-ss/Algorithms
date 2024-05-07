import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr, j  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr, i + 1  
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = yield from partition(arr, low, high)
        yield from quick_sort(arr, low, pi - 1)
        yield from quick_sort(arr, pi + 1, high)

def update(frame):
    ax.clear()
    bars, idx = frame
    colors = ['orange' if i == idx else 'gray' if i < idx else 'green' for i in range(len(bars))]
    ax.bar(range(len(bars)), bars, color=colors)

# Generate a random array
arr = np.random.randint(1, 100, size=20)

fig, ax = plt.subplots()
ax.bar(range(len(arr)), arr, color='blue')

ani = FuncAnimation(fig, update, frames=quick_sort(arr, 0, len(arr) - 1), blit=False, repeat=False, cache_frame_data=False)

plt.show()
