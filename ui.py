import operacoes as op


class Poligono:
    def __init__(self, canvas, altura_canvas, objeto):
        """

        :type altura_canvas: Integer
        :type canvas: tkinter.Canvas
        """
        self.canvas = canvas
        self.altura_canvas = altura_canvas
        self.matriz_objeto = objeto

        self.labels = ['A', 'B', 'C', 'D', 'E', 'F']
        self.id_objeto = None
        self.id_labels = []

    def desenhar(self):
        out = []
        pontos = op.mapear(self.matriz_objeto, self.altura_canvas).T

        for col in range(len(pontos)):
            out.append(pontos[col][0])
            out.append(pontos[col][1])

        self.id_objeto = self.canvas.create_polygon(*out, outline='black', fill='white', width=2)

        for col in range(len(pontos)):
            x = self.matriz_objeto.T[col][0]
            y = self.matriz_objeto.T[col][1]
            text = "(%d, %d)" % (x, y)
            id_label = self.canvas.create_text(pontos[col][0], pontos[col][1], text=text, fill='black')
            id_box = self.canvas.create_rectangle(self.canvas.bbox(id_label), fill="white")
            self.canvas.tag_lower(id_box, id_label)
            self.id_labels.append(id_label)
            self.id_labels.append(id_box)

    def transladar(self, tx, ty):
        self.matriz_objeto = op.translacao(self.matriz_objeto, tx, ty)
        self._resetar()
        self.desenhar()

    def escalar(self, ex, ey):
        self.matriz_objeto = op.escala(self.matriz_objeto, ex, ey)
        self._resetar()
        self.desenhar()

    def rotacionar(self, teta):
        self.matriz_objeto = op.rotacao(self.matriz_objeto, teta)
        self._resetar()
        self.desenhar()

    def _resetar(self):
        self.canvas.delete(self.id_objeto)

        for id_label in self.id_labels:
            self.canvas.delete(id_label)

        self.id_objeto = None
        self.id_labels = []
