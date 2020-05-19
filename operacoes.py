import numpy as np


def mapear(matriz_original, altura_canvas):
    matriz_transformacao = np.array([[1, 0], [0, -1]])
    return translacao(matriz_transformacao.dot(matriz_original), 0, altura_canvas)


def translacao(matriz_original, tx, ty):
    linha_x = matriz_original[0]
    linha_y = matriz_original[1]

    return np.array([linha_x + tx, linha_y + ty])


def escala(matriz_original, ex, ey):
    matriz_escala = np.array([[ex, 0],
                              [0, ey]])
    return matriz_escala.dot(matriz_original)


def rotacao(matriz_original, teta):
    teta = np.deg2rad(teta)
    matriz_rotacao = np.array([[np.cos(teta), -np.sin(teta)],
                               [np.sin(teta), np.cos(teta)]])

    return matriz_rotacao.dot(matriz_original)
