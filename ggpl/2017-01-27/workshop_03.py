from pyplasm import *

def ggpl_building_stairs_with_landings(dx, dy, dz,bool):
    """i parametri in input sono:
    1)la dimensione su x del complesso totale
    2)la dimensione su y del complesso totale
    3)la dimensione su z del complesso totale
    """
    hHalved = (dz/2.0)
    hHalved = hHalved -(hHalved/60.)
    xReduced = (dx/4.0)*2

    angle = check(hHalved,xReduced)
    
    if (angle != 100):
        print("dimensioni non valide.")
        print(" angolo " + str(angle) + " non compreso tra 30 gradi e 35 gradi")
        print("inserire delle dimensioni valide")
        return -1
    
    comparisonAP = hHalved/xReduced
    stepZ = (0.63*comparisonAP)/((2.0*comparisonAP)+1.0)
    numSteps= round(hHalved/stepZ)
    stepX = (0.63-(2.0*stepZ))
    stepY = (dy/7.0)*3.0

    
    values = generatesRamp(numSteps, stepX, stepY, stepZ,dx)
    floor = generafloor(values[1],values[2],dx,dy,dz,stepX,stepZ)
    ramp2 = movesRampReflected(values[0],values[1],values[2],dx,dy,dz,stepY,stepZ)
    second_floor = generate_second_floor(values[1],values[2],dx,dy,dz,stepX,stepZ)
    pillars = generate_pillars(stepX,stepY,stepZ,dx,dy,dz,bool)
    project = TEXTURE("images/ramp.jpg")(STRUCT([values[0],ramp2,floor,second_floor,pillars]))
    #VIEW(project)
    return project


def generate_pillars(stepX,stepY,stepZ,dx,dy,dz,bool):

    stepX = stepX/2.
    stepY = stepY/2.
    stepZ = stepZ/2.
    
    pillars = []
    pillars.append(T(2)(-stepX)(CUBOID([stepX,stepX,dz])))
    pillars.append(T([1,2])([(dx/4)-stepX,-stepX])(CUBOID([stepX,stepX,dz])))
    pillars.append(T([1,2])([(dx/4)-stepX,dy])(CUBOID([stepX,stepX,dz])))
    pillars.append(T(2)(dy)(CUBOID([stepX,stepX,dz])))

    pillars = STRUCT(pillars)
    
    pill = []
    pill.append(T(2)(-stepX)(CUBOID([stepX,stepX,dz/2.])))
    pill.append(T([1,2])([(dx/4)-stepX,-stepX])(CUBOID([stepX,stepX,dz/2.])))
    pill.append(T([1,2])([(dx/4)-stepX,dy])(CUBOID([stepX,stepX,dz/2.])))
    pill.append(T(2)(dy)(CUBOID([stepX,stepX,dz/2.])))

    pill = T(1)((dx/4)*3)(STRUCT(pill))
    
    if(bool != 1):

        temp = T(3)(dz/2.)(pill)
        pill = STRUCT([pill,temp])
        
        

    return STRUCT([pillars,pill])


def generatesRamp(numSteps,stepX, stepY, stepZ,dx):
    
    i=0
    listSteps=[]
    complete = []
    floorX = 0
    floorZ = 0
    traslx = 0
    traslz = 0

    while i<numSteps:

        listSteps.append(T([1,3])([traslx,traslz]))
        listSteps.append(CUBOID([stepX,stepY,stepZ]))
        if(i<numSteps-1):
            complete.append(MKPOL([[[traslx+stepX,0,traslz],[traslx+stepX,0,traslz+stepZ],[traslx+(2*stepX),0,traslz+stepZ],[traslx+stepX,stepY,traslz],[traslx+stepX,stepY,traslz+stepZ],[traslx+(2*stepX),stepY,traslz+stepZ]],[[1,2,3,4,5,6]],[1]]))
            complete.append(T([1,3])([traslx,traslz]))
        traslx = stepX
        traslz = stepZ
        floorX = floorX + stepX
        floorZ = floorZ + stepZ
        i=i+1
    
    return [T(1)(dx/4.)(STRUCT([STRUCT(listSteps),STRUCT(complete)])),floorX,floorZ]



def generafloor(traslx,traslz,dx,dy,dz,stepX,stepZ):

    floor = []

    floor.append(T([1,3])([traslx+(dx/4.),traslz-stepZ]))
    floor.append(CUBOID([dx-(traslx+(dx/4.)),dy,stepZ]))
    return STRUCT(floor)


def movesRampReflected(ramp,traslx,traslz,dx,dy,dz,stepY,stepZ):
    
    rampReflected = []
    rampReflected.append(S(1)(-1))
    rampReflected.append(T([1,2,3])([-traslx-(2*(dx/4.)),dy-stepY,dz/2.-(stepZ/2.)]))
    rampReflected.append(ramp)
    return STRUCT(rampReflected)

def generate_second_floor(traslx,traslz,dx,dy,dz,stepX,stepZ):


    floor = []
    floor.append(T(3)(dz-stepZ))                        
    floor.append(CUBOID([dx-(((dx/4.)*2)+(dx/4.)),dy,stepZ]))
                        
    return STRUCT(floor)


def check(hHalved,xReduced):

    angle=ATAN(hHalved/xReduced)
    angle = (angle/3.14)*180
    
    if(30<angle<35):
        
        return 100
    return angle



#ggpl_building_stairs_with_landings(3.6,4,2.5,1)
