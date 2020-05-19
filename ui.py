import operacoes as op


class Poligono:
    def __init__(self, canvas, altura_canvas, objeto, pontos_label):
        """

        :type altura_canvas: Integer
        :type canvas: tkinter.Canvas
        """
        self.canvas = canvas
        self.altura_canvas = altura_canvas
        self.matriz_objeto = objeto
        self.matriz_labels = pontos_label

        self.labels = ['A', 'B', 'C', 'D', 'E', 'F']
        self.id_objeto = None
        self.id_labels = []

    def desenhar(self):
        out = []
        pontos = op.mapear(self.matriz_objeto, self.altura_canvas).T
        pontos_textos = op.mapear(self.matriz_labels, self.altura_canvas).T

        for col in range(len(pontos)):
            out.append(pontos[col][0])
            out.append(pontos[col][1])

            id_label = self.canvas.create_text(pontos_textos[col][0], pontos_textos[col][1], text=self.labels[col])
            self.id_labels.append(id_label)

        self.id_objeto = self.canvas.create_polygon(*out, outline='black', fill='white', width=2)

    def transladar(self, tx, ty):
        self.matriz_labels = op.translacao(self.matriz_labels, tx, ty)
        self.matriz_objeto = op.translacao(self.matriz_objeto, tx, ty)
        self._resetar()
        self.desenhar()

    def _resetar(self):
        self.canvas.delete(self.id_objeto)

        for id_label in self.id_labels:
            self.canvas.delete(id_label)

        self.id_objeto = None
        self.id_labels = []
