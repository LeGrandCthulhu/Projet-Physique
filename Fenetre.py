import tkinter as tk
import Classes as cl

root = tk.Tk()

root.title("Physique")
root.geometry("800x800")
root.minsize(800, 800)
root.config(bg="#36393e")

canvas = tk.Canvas(root, height=800, width=800, bg="black", bd=0, highlightthickness=0)

canvas.pack()
root.mainloop()