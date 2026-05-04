import tkinter as tk
import random
import time

# Generate random data
def generate_data():
    global data
    data = [random.randint(10, 100) for _ in range(30)]
    draw_data(data, ["blue"] * len(data))

# Draw bars
def draw_data(data, color_array):
    canvas.delete("all")
    canvas_height = 300
    canvas_width = 600
    bar_width = canvas_width / len(data)

    for i, value in enumerate(data):
        x0 = i * bar_width
        y0 = canvas_height - value * 2
        x1 = (i + 1) * bar_width
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        canvas.create_text(x0 + 10, y0, anchor=tk.SW, text=str(value))

    root.update_idletasks()

# Bubble Sort
def bubble_sort():
    global data
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            colors = ["red" if x == j or x == j+1 else "blue" for x in range(len(data))]
            draw_data(data, colors)
            time.sleep(0.05)

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    draw_data(data, ["green"] * len(data))

# Selection Sort
def selection_sort():
    global data
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            colors = ["yellow" if x == j else "blue" for x in range(len(data))]
            draw_data(data, colors)
            time.sleep(0.05)

            if data[j] < data[min_idx]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]

    draw_data(data, ["green"] * len(data))

# UI
root = tk.Tk()
root.title("Sorting Visualizer")

canvas = tk.Canvas(root, width=600, height=300, bg="white")
canvas.pack()

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Generate Data", command=generate_data).grid(row=0, column=0)
tk.Button(frame, text="Bubble Sort", command=bubble_sort).grid(row=0, column=1)
tk.Button(frame, text="Selection Sort", command=selection_sort).grid(row=0, column=2)

data = []

root.mainloop()