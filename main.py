import tkinter as tk
import numpy as np
import ui
from tkinter import messagebox
import re


def handle(poligono, operacao, args):
    try:
        args = [float(arg) for arg in args if arg]
        pattern = re.compile('(\\w+?)\\((.+?)\\)')
        match = pattern.match(operacao)

        metodo = match.group(1)
        numargs = len(match.group(2).split(","))
        args = args[:numargs]

        getattr(poligono, metodo)(*args)
    except BaseException as e:
        messagebox.showerror('Um erro ocorreu', message=e)


if __name__ == '__main__':
    root = tk.Tk()

    frame = tk.Frame(root)
    frame.pack()

    operacoes_disponiveis = ["translacao(tx, ty)", "escala(ex, ey)", "rotacao(teta)",
                             "escala(ex, ey, ptx, pty)", "rotacao(teta, ptx, pty)"]

    operacao = tk.StringVar(frame)
    operacao.set(operacoes_disponiveis[0])
    operacoes = tk.OptionMenu(frame, operacao, *operacoes_disponiveis)
    operacoes.pack(side=tk.LEFT)

    args = [tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()]
    for arg in args:
        tk.Entry(frame, textvariable=arg).pack(side=tk.LEFT)

    button = tk.Button(frame, text="Aplicar", command=lambda: handle(poligono, operacao.get(), [arg.get() for arg in args]))
    button.pack(side=tk.LEFT)

    # Canvas
    canvas = tk.Canvas(root, bg="white", height=800, width=1200)
    canvas.winfo_height()
    canvas.pack()

    original = np.array([[100, 150, 150, 50, 50],
                         [200, 150, 50, 50, 150]])

    poligono = ui.Poligono(canvas, 800, original)
    poligono.desenhar()

    root.mainloop()
