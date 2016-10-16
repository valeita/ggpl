from pyplasm import *
from larlib import *

def gabbia((tx,tz),(px,py),altezzePilastri,larghezzeTravi):

    Pilastri = creaPilastri((px,py),(altezzePilastri))
    Travi = creaTravi ((tx,tz),larghezzeTravi
    pianoPilastri = copiaPilastri(Pilastri,larghezzeTravi)
    pianoTravi = copiaTravi(Travi,altezzePilastri)
    
    gabbia = STRUCT([pianoPilastri,pianoTravi])
        
    return gabbia



def copiaPilastri(Pilastri, larghezzeTravi):

    listaPilastri = []
    listaPilastri.append(T(2)(0))
    listaPilastri.append(Pilastri)
    
    for elem in larghezzeTravi:

        listaPilastri.append(T(2)(elem))
        listaPilastri.append(Pilastri)
            
    return STRUCT(listaPilastri)



def copiaTravi(Travi, altezzePilastri):

    listaTravi = []
    
    for elem in altezzePilastri:
            
         listaTravi.append(T(3)(elem))
         listaTravi.append(Travi)
            
    return STRUCT(listaTravi)




def creaPilastri ((px,py),altezzePilastri):

    prec=0
    listaPilastri=[]
    
    for i in altezzePilastri:

        listaPilastri.append(T(3)(prec))
        listaPilastri.append(CUBOID([px,py,i]))
        prec = i
        
        return STRUCT(listaPilastri)



def creaTravi ((tx,tz),larghezzeTravi):

    prec=0
    listaTravi=[]
    
    for i in larghezzeTravi:

        listaTravi.append(T(2)(prec))
        listaTravi.append(CUBOID([tx,i,tz]))
        prec = i
        
        return STRUCT(listaTravi)


