import tkinter as tk
import numpy as np
import operacoes as op
import ui

if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, bg="white", height=800, width=800)
    canvas.winfo_height()

    original = np.array([[100, 150, 150, 50, 50],
                         [200, 150, 50, 50, 150]])

    poligono = ui.Poligono(canvas, 800, original)
    poligono.desenhar()

    canvas.pack()
    root.mainloop()
