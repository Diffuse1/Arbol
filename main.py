from lib import *
inOrderArr=[]
modo1 = modo(1)
modo2 = modo(2)
modo3 = modo(3)
modo4 =  modo(4)
modo5 = modo(5)
modo6 = modo(6)
modo7 = modo (7)
linkHijo(modo1,modo2,modo3)
linkHijo(modo2,modo4,modo5)
linkHijo(modo3,modo6,modo7)
LVR (modo1,inOrderArr)
print( inOrderArr )
print( modo1.getArbol())
