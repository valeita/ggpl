from pyplasm import *

def ggpl_my_roof_builder(hpc):
    """
    the following function has the task of managing
    and invoke all the functions described below.
    It takes as input a hpc, or a mkpol of vertices and cells.
    """
    
    BaseStructure = SKEL_1(hpc)
    BaseStructure = OFFSET([0.1,0.1,0.1])(BaseStructure)
    pointsList=[]
    pointsList = UKPOL(hpc)

    verts=pointsList[0]
    cells = pointsList[1]
    
    vertsDiversi = eliminateRedundance(verts)
    
    points = searchInternalPoints(vertsDiversi)
    internalPoints = points[0]
    basePoints = points[1]

    arg = generateSecondArgument(basePoints)
    plane = MKPOL([basePoints,[arg],1])
    plane = SKEL_2(plane)
    plane = OFFSET([0.1,0.1,0.1])(plane)
    
    correctedPoints = correctMKPOL(internalPoints,verts,cells)
    correctedVerts = correctedPoints[0]
    correctedCells = correctedPoints[1]
    
    
    planes = MKPOL([correctedVerts,correctedCells,1])
    planes = SKEL_2(planes)
    planes = OFFSET([0.1,0.1,0.1])(planes)
    
    roof = DIFFERENCE([planes,plane])
    roof = UNION([roof,BaseStructure])

    VIEW(roof)
    
    
    return roof


def correctMKPOL(internalPoints, verts, cells):
    """
    the following function has the task of, data Vertex
    and cells, and of the points to be deleted, deleted from the
    list of vertices, the leaders considered internal, and readjust
    the lists of the cells according to the points eliminated
    """
    listIndex = []
    cont = 1
    newVerts = []
    newCells = []
    finish = 0
    
    for i in verts:

        finish = 0
        
        for j in internalPoints:

            if(j==i):

                listIndex.append(cont)
                finish = 1
                
        if(finish == 0):

            newVerts.append(i)    
        cont = cont +1
    
    downCounter = 0
    
    for i in cells:
        newCell = []
        for j in i:

            if(research(listIndex,j) == 0):

                newCell.append(j-downCounter)
            else:
                downCounter = downCounter +1
                
        if(len(newCell)!=0):
            
            newCells.append(newCell)
          
    
    return [newVerts,newCells]


def research(list, x):
    """
    the following function has the task to return true if
    the given input element, is present within the list
    """
    for i in list:

        if(x==i):

            return 1
    return 0    



def create_mkpol_roof(x,y,z):
    """
    the following function has the task of creating
    an HPC or a MKPOL in which there will be the vertices
    and the cells that will form our roof
    """
    roof = MKPOL([ [[0,0,0],[0,y,0],[x/5,y/2.0,z],[(x/(5.0))*4,y/2.0,z],[x,y,0],[x,0,0],[x/5,y/2.0,0],[(x/(5.0))*4,y/2.0,0]],[[6,5,4,3,2,1],[7,2,3,1],[5,6,4,8],[7,8]],1])

    return roof




def searchInternalPoints(pointsList):
    """
    the following function has the task of searching the internal
    points within our structure. they will be the points having coordinates
    with respect to the axes x, y that are neither minimum nor maximum, and
    that have a different altitude than the maximum.
    """
    xMIN = 0
    yMIN = 0
    zMIN = 0
    
    listGood = []
    listBad = []
    listaBase = []
    listaMax = searchMax(pointsList)

    for i in pointsList:

        if(i[0] == xMIN or i[0] == listaMax[0]):

            listGood.append(i)
            listaBase.append(i)

        elif(i[1] == yMIN or i[1] == listaMax[1]):

            listGood.append(i)
            listaBase.append(i)
            
        elif(i[2] != zMIN):

            listGood.append(i)
            
        else:

            listBad.append(i)
    
    return [listBad,listaBase]







def searchMax(pointsList):
    """
    the following function has the task of finding the maximum coordinates of vertices
    """
    xMAX = 0
    yMAX = 0
    zMAX = 0

    for i in pointsList:

        if(i[0] > xMAX):

            xMAX=i[0]
            
        if(i[1] > yMAX):

            yMAX=i[1]

        if(i[2] > zMAX):

            zMAX=i[2]

    return [xMAX,yMAX,zMAX]




def eliminateRedundance(points):
    """
    the following function has the task
    to eliminate redundancies, because in
    fact dell'UKPOL, which returns a set of redundant points
    """
    
    list = []
    for i in points:

        if(research(list,i) == 0):

            list.append(i)
        
    return list



def generateSecondArgument(basePoints):
    """
    the following function has the task of generating the second
    argument of a MKPOL. This can be done statically and does not
    affect the program's dynamism
    """
    list = []
    i=1
    while(i<len(basePoints)+1):

        list.append(i)
        
        i=i+1
    return list
    
ggpl_my_roof_builder(create_mkpol_roof(10,4,2))
