import tkinter as tk
import Classes as cl

def draw(astre: cl.Astre, canvas: tk.Canvas) -> None:
    canvas.create_oval((astre.x - astre.r, astre.y - astre.r), (astre.x + astre.r, astre.y + astre.r), fill="white")