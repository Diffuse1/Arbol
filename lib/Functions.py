
def linkHijo( modoPradre, modoHijoIzq=None, modoHijoDer=None):
    if modoHijoIzq is not None:
        modoPradre.izquierda =modoHijoIzq
    if modoHijoDer is not None:
        modoPradre.Derecha = modoHijoDer
    pass
def LVR(modo, inOrderArr):
    if modo is not None:
        modoPadre = modo
        LVR (modoPadre.izquierda, inOrderArr)
        inOrderArr.append(modoPadre.valor)
        LVR(modoPadre.Derecha,inOrderArr)
    return inOrderArr


