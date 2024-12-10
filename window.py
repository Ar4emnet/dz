import random
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

def numbers():
    numbers = [random.randint(-100,100)+10 for n in range(int(w.get()))]
    negative_nubers = [n for n in numbers if n < 0]
    return(numbers, negative_nubers)

def window():
    global root
    root = Tk(className="Uloha")
    root.configure(bg="lightblue")
    global graph_window
    graph_window = tk.Frame(root)
    graph_window.pack()
    global label
    label = tk.Label(root, font=('Arial', 12, "bold"), bg="lightblue",
                     text="Programovacie techniky \n Artem Koliesnik\n Vygenerujte pole 18 náhodných celých čísiel z intervalu -100 až 100,\n ku každému z nich pripočítajte hodnotu 10, vypíšte iba záporné čísla, a zobrazte graf hodnôt. Max cislo 50")
    root.geometry("800x300")
    label.pack()
    global w
    w = Spinbox(root, from_=0, to_=40)
    w.pack(pady=20)
    global button
    button = Button(root, text="start", bg="blue", fg="white", font=('Arial', 12, "bold"), width=20, command=graph)
    button.pack(pady=20)
    root.mainloop()

def graph():
    root.geometry("1440x600")

    fig, ax = plt.subplots(figsize=(30, 6))
    num_y, num2 = numbers()
    num_x = [n for n in range(1, int(w.get()) + 1, 1)]
    ax.plot(num_x, num_y, marker="o")
    plt.xticks(range(1, int(w.get()) + 1, 1))
    plt.title(f"Numbers {num_y} \n negative numbers {num2}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    button.pack_forget()


