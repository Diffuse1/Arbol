class modo():
    def __init__(self,valor):
        self.valor=valor
        self.izquierda = None
        self.Derercho= None
        pass
    def __str__(self):
        return f'Valor:  {self.valor}, izq: {self.izquierda}, der: {self.Derercho}'