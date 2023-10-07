import tkinter as tk
import func as fc
import Classes as cl

root = tk.Tk()

root.title("Physique")
root.geometry("800x800")
root.minsize(800, 800)
root.config(bg="#36393e")

canvas = tk.Canvas(root, height=800, width=800, bg="black", bd=0, highlightthickness=0)

a1 = cl.Astre(5, 10, 400, 400)
while True:
    fc.draw(a1, canvas)
    a1.x += 1


canvas.pack()
root.mainloop()