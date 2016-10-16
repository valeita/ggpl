from pyplasm import *


def gabbia((tx,tz),(px,py),altezzePilastri,larghezzeTravi):

    Pilastri = creaPilastri((tx,tz),(px,py),altezzePilastri,larghezzeTravi)
    Travi = creaTravi((tx,tz),(px,py),altezzePilastri,larghezzeTravi)
    
    return STRUCT([Pilastri,Travi])

def creaPilastri((tx,tz),(px,py),altezzePilastri,larghezzeTravi):
    
    ay = []
    ax = [px]
    az = []
    for i in larghezzeTravi:

        ay.append(py)
        ay.append(-i)
    ay.append(py)

    for elem in altezzePilastri:

        az.append(elem)
        az.append(-tz)
    
    pianoPilastri = PROD([QUOTE(ax),QUOTE(ay)])
    Pilastri = PROD([pianoPilastri,QUOTE(az)])

    return Pilastri


def creaTravi ((tx,tz),(px,py),altezzePilastri,larghezzeTravi):

    ay = []
    ax = [tx]
    az = []
    
    for i in larghezzeTravi:

        ay.append(py+i)

    for elem in altezzePilastri:

        az.append(-elem)
        az.append(tz)

    pianoTravi = PROD([QUOTE(ax),QUOTE(ay)])
    Travi = PROD([pianoTravi, QUOTE(az)])

    return Travi
    

VIEW(gabbia((10,100),(40,40),[1000,500,1000],[1000,500,1000]))


