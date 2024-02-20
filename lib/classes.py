class modo():
    def __init__(self,valor):
        self.valor=valor
        self.izquierda = None
        self.Derecha= None
        pass
    def __str__(self):
        return f'Valor:  {self.valor}'
    
    def getArbol(self):
        strOut = ""
        strOut += f" NP [{self.valor}]"
        if type(self.izquierda) != type(None):
            strOut += f"[{self.valor}]->[{self.izquierda}]"
        elif self.Derecha is not None:
            strOut += f"[{self.valor}]->[{self.Derecha}]"
            return strOut
pass        