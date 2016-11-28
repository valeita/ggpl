from pyplasm import *
from larlib import *

def generates_door(X,Y,Z,occupancy):

    """
    Following the function takes three input parameters of list,
    a three-dimensional matrix, and 3 real. Processes the data and
    products after appropriate controls an HPC, the door/doors.
    """
    list = []
    cont1 = 0
    cont2 = 0
    cont3 = 0
    sum1=0
    sum2=0
    sum3=0
    
    for elem_z in occupancy:

        cont2=0
        sum2=0
        for elem_y in elem_z:

            cont1=0
            sum1=0
            for elem_x in elem_y:

                if(elem_x == 1):
                    
                    list.append(T([1,2,3])([sum1,sum2,sum3])(COLOR(Color4f([126/255., 78/255., 40/255., 1]))(CUBOID([X[cont1],Y[cont2],Z[cont3]]))))
                    cont1 = cont1+1
                    sum1=sum1+X[cont1-1]
                    
                elif(elem_x == -1):

                    list.append(T([1,2,3])([sum1,sum2,sum3])(COLOR(Color4f([96/255., 144/255., 170/255., 1]))(CUBOID([X[cont1],Y[cont2],Z[cont3]]))))
                    cont1 = cont1+1
                    sum1=sum1+X[cont1-1]
                
            cont2=cont2+1
            sum2=sum2+Y[cont2-1]
        cont3=cont3+1
        sum3=sum3+Z[cont3-1]

        structure = STRUCT(list)
        structure = S(1)(-1)(structure)
        structure = T(1)(sum1)(structure)
    
    def check(dx,dy,dz):

        list_s = []
        alfa = 0.03        
        xMAX = 0
        yMAX = 0
        zMAX = 0

        for i in X:

            xMAX = xMAX+i
            
        for i in Y:

            yMAX = yMAX+i
            
        for i in Z:

            zMAX = zMAX+i

        if(xMAX+alfa>dx or yMAX+alfa>dy or zMAX+alfa>dz):

            print("size not enough to hold the door / window")
    
        list_s.append(OFFSET([0.02,0.02,0.02])(SKEL_1(CUBOID([dx,dy,dz]))))                    
        list_s.append(T([1,2,3])([0.015,0.015,0.015]))                     
        list_s.append(structure)
        
        space_occuped = yMAX + alfa
        while(dy-space_occuped>yMAX+alfa):
            
            list_s.append(T(2)(yMAX+(alfa/2.0)))
            list_s.append(structure)
            space_occuped = space_occuped + yMAX + alfa
            

        return STRUCT(list_s)

    return check
        



def generates_window(X,Y,Z,occupancy):
    """
    Following the function takes three input parameters of list,
    a three-dimensional matrix, and 3 real. Processes the data and
    products after appropriate controls an HPC, the window/windows.
    """
    list = []
    cont1 = 0
    cont2 = 0
    cont3 = 0
    sum1=0
    sum2=0
    sum3=0
    
    for elem_z in occupancy:

        cont2=0
        sum2=0
        for elem_y in elem_z:

            cont1=0
            sum1=0
            for elem_x in elem_y:

                if(elem_x == 1):
                    
                    list.append(T([1,2,3])([sum1,sum2,sum3])(CUBOID([X[cont1],Y[cont2],Z[cont3]])))
                    cont1 = cont1+1
                    sum1=sum1+X[cont1-1]
                    
                elif(elem_x == -1):

                    list.append(T([1,2,3])([sum1,sum2,sum3])(COLOR(Color4f([96/255., 144/255., 170/255., 1]))(CUBOID([X[cont1],Y[cont2],Z[cont3]]))))
                    cont1 = cont1+1
                    sum1=sum1+X[cont1-1]
                
            cont2=cont2+1
            sum2=sum2+Y[cont2-1]
        cont3=cont3+1
        sum3=sum3+Z[cont3-1]

        structure = STRUCT(list)
        structure = S(1)(-1)(structure)
        structure = T(1)(sum1)(structure)
    
    def check(dx,dy,dz):

        list_s = []
        alfa = 0.03        
        xMAX = 0
        yMAX = 0
        zMAX = 0

        for i in X:

            xMAX = xMAX+i
            
        for i in Y:

            yMAX = yMAX+i
            
        for i in Z:

            zMAX = zMAX+i

        if(xMAX+alfa>dx or yMAX+alfa>dy or zMAX+alfa>dz):

            print("size not enough to hold the door / window")
    
        list_s.append(OFFSET([0.02,0.02,0.02])(SKEL_1(CUBOID([dx,dy,dz]))))                    
        list_s.append(T([1,2,3])([0.015,0.015,0.015]))                     
        list_s.append(structure)
        
        space_occuped = yMAX + alfa
        while(dy-space_occuped>yMAX+alfa):
            
            list_s.append(T(2)(yMAX+(alfa/2.0)))
            list_s.append(structure)
            space_occuped = space_occuped + yMAX + alfa
            

        return STRUCT(list_s)

    return check
        



                      
   
def generate_X(string):

    """
    given a string, returns the input examples values with respect to the x axis.
    It is the first parameter of generates_window / door function
    """
    
    if(string == "door"):
        
        return [0.04,0.04]
    
    if(string == "window"):
        
        return [0.05]

    
def generate_Y(string):

    """
    given a string, returns the input examples values with respect to the y axis.
    It is the second parameter of generates_window / door function
    """
    
    if(string == "door"):
        
        return [0.1,0.03,0.1,0.075,0.03,0.075,0.03,0.075,0.03,0.075,0.0975,0.015,0.015,0.0975,0.075,0.03,0.075,0.03,0.075,0.03,0.075,0.1,0.03,0.1]
    
    elif(string == "window"):
        
        return [0.1,0.5,0.1,0.1,0.5,0.1]
    else:
        print("Error In typing the string. I can only generate doors or windows")
        exit()

        
def generate_Z(string):
     
    """
    given a string, returns the input examples values with respect to the z axis.
    It is the third parameter of generates_window / door function
    """
    
    if(string == "door"):
        
         return [0.15,0.1,0.1,0.3,0.03,0.3,0.03,0.3,0.1,0.1,0.03,0.25,0.03,0.1]
    
    elif(string == "window"):
        
        return [0.05,1,0.05]
    else:
        print("Error In typing the string. I can only generate doors or windows")
        exit()

        
def generate_occupancy(string):

    """
    given a string, returns the input examples values of a 3D boolean matrix (-1 is accepted too).
    It is the fourth parameter of generates_window / door function
    """
    
    if(string == "door"):    
    
        return [ [[1,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[1,1]],
                 [[1,1],[0,1],[0,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[0,1],[0,1],[0,1],[0,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[0,1],[0,1],[1,1]],
                 [[1,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[1,1]],           
                 [[1,1],[0,1],[0,1],[0,-1],[0,-1],[0,-1],[0,1],[0,-1],[0,-1],[0,-1],[0,1],[0,1],[0,1],[0,1],[0,-1],[0,-1],[0,-1],[0,1],[0,-1],[0,-1],[0,-1],[0,1],[0,1],[1,1]],             
                 [[1,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[1,1]],
                 [[1,1],[0,1],[0,1],[0,-1],[0,-1],[0,-1],[0,1],[0,-1],[0,-1],[0,-1],[0,1],[0,1],[0,1],[0,1],[0,-1],[0,-1],[0,-1],[0,1],[0,-1],[0,-1],[0,-1],[0,1],[0,1],[1,1]],
                 [[1,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[1,1]],
                 [[1,1],[0,1],[0,1],[0,-1],[0,-1],[0,-1],[0,1],[0,-1],[0,-1],[0,-1],[0,1],[0,1],[0,1],[0,1],[0,-1],[0,-1],[0,-1],[0,1],[0,-1],[0,-1],[0,-1],[0,1],[0,1],[1,1]],
                 [[1,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[1,1]],
                 [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]],
                 [[1,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[1,1]],            
                 [[1,1],[0,1],[0,-1],[0,-1],[0,1],[0,-1],[0,-1],[0,-1],[0,1],[0,-1],[0,-1],[0,1],[0,1],[0,-1],[0,-1],[0,1],[0,-1],[0,-1],[0,-1],[0,1],[0,-1],[0,-1],[0,1],[1,1]],          
                 [[1,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[1,1]],             
                 [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]] ]
    
    elif(string == "window"):

        return [[[1],[1],[1],[1],[1],[1]],[[1],[-1],[1],[1],[-1],[1]],[[1],[1],[1],[1],[1],[1]]]
    
    else:
        print("Error In typing the string. I can only generate doors or windows")
        exit()

        
    
mydoor = generates_door(generate_X("door"),generate_Y("door"),generate_Z("door"),generate_occupancy("door"))(0.2,2,2)
VIEW(mydoor)

mywindow = generates_window(generate_X("window"),generate_Y("window"),generate_Z("window"),generate_occupancy("window"))(0.2,1.5,1.3)
VIEW(mywindow)




