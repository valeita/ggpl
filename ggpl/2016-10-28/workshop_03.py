from pyplasm import *

def ggpl_building_stairs_with_landings(dx, dy, dz):
    """i parametri in input sono:
    1)la dimensione su x del complesso totale
    2)la dimensione su y del complesso totale
    3)la dimensione su z del complesso totale
    """
    hHalved = dz/2.0
    xReduced = (dx/3.0)*2.0
    angle = check(hHalved,xReduced)
    
    if (angle != 100):
        print("dimensioni non valide.")
        print(" angolo " + str(angle) + " non compreso tra 30 gradi e 35 gradi")
        print("inserire delle dimensioni valide")
        return -1
    
    floorX = dx/3.0
    comparisonAP = hHalved/xReduced
    stepZ = (0.63*comparisonAP)/((2.0*comparisonAP)+1.0)
    numSteps= round(hHalved/stepZ)
    StepX = (0.63-(2.0*stepZ))
    stepY = (dy/7.0)*3.0

    
    ramp = generatesRamp(numSteps, StepX, stepY, stepZ)
    floor = generafloor(hHalved,xReduced,floorX,dy,stepZ)
    rampReflected = reflectRamp(ramp)
    ramp2 = movesRampReflected(rampReflected,xReduced, hHalved, dy)
    Reference = SKEL_1(CUBOID([dx,dy,dz]))  
    project = STRUCT([ramp,ramp2,Reference,floor]) 
    VIEW(project)
    return 1


def generatesRamp(numSteps,StepX, stepY, stepZ):
    
    i=0
    listSteps=[]
    traslx = 0
    traslz = 0

    while i<numSteps:

        listSteps.append(T([1,3])([traslx,traslz]))
        listSteps.append(CUBOID([StepX,stepY,stepZ]))
        traslx = StepX
        traslz = stepZ
        i=i+1
    return STRUCT(listSteps)



def generafloor(hHalved,xReduced,floorX,dy,stepZ):

    floorY=dy
    floorZ=stepZ

    floor = []
    floor.append(T([1,3])([(xReduced),hHalved-stepZ]))
    floor.append(CUBOID([floorX,floorY,floorZ]))
    return STRUCT(floor)



def reflectRamp(ramp):

    rampReflected = [S(1)(-1),ramp]
    
    return STRUCT(rampReflected)

def movesRampReflected(rampReflected, xReduced, hHalved, dy):

    ramp2 = []
    ramp2.append(T([1,2,3])([(xReduced),((dy*4)/7),hHalved]))
    ramp2.append(rampReflected)
    return STRUCT(ramp2)
    
    

def check(hHalved,xReduced):

    angle=ATAN(hHalved/xReduced)
    angle = (angle/3.14)*180
    
    if(30<angle<35):
        
        return 100
    return angle


ggpl_building_stairs_with_landings(4,4,3.5)
