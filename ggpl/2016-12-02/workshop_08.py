from pyplasm import *
from larlib import *

def ggpl_planimetry3D(file_list):

    """
    the function takes into exactly 9 input file
    containing lists of useful numbers for the construction
    of the casa.l'input is static and must not be varied.
    """

    walls = []
    wind = []
    others = []
    
    walls.append(S(2)(-1))
    walls.append(PROD([create_walls([file_list[0],file_list[1],file_list[2]]),Q(130)]))
    wind.append(S(2)(-1)(T(3)(40)(PROD([create_glass_doors_windows(file_list[8],[14,14]),Q(50)]))))
    walls.append((T(3)(100)(PROD([create_glass_doors_windows(file_list[9],[6,6]),Q(30)]))))
    walls.append((T(3)(100)(PROD([create_glass_doors_windows(file_list[10],[20,20]),Q(30)]))))
    walls.append((T(3)(100)(PROD([create_glass_doors_windows(file_list[11],[13,13]),Q(30)]))))
    house_part1 = TEXTURE("images/tint.jpg")(DIFFERENCE([STRUCT(walls),STRUCT(wind)]))
    
    others.append(S(2)(-1))
    others.append(create_floor(file_list[4],9))
    others.append(create_floor(file_list[5],6))
    others.append(create_floor(file_list[6],1))
    others.append(TEXTURE("images/glass.jpg")(PROD([create_glass_doors_windows(file_list[3],[2,2]),Q(100)])))
    others.append(TEXTURE("images/glass.jpg")(PROD([create_glass_doors_windows(file_list[7],[13,13]),Q(130)])))

    house_part2 = STRUCT(others)

    house_completed = STRUCT([house_part1,house_part2])
    
    VIEW(house_completed)

    return house_completed


def create_walls(file_list):

    """
    This function takes as input a list of files.
    it must contain exactly 3 files, two of which relate to
    the construction of the exterior walls, and the interior walls.
    """

    index = 0
    structure = []
    array_offset = [[20,20],[13,13],[6,6]]

    xMIN = 100000000
    yMIN = 100000000
    xMAX = -1
    yMAX = -1
    for elem in file_list:
    
        file = open(elem)
        
        for single_line in file:
            
            num_list = single_line.split(',')                
            structure.append(OFFSET([array_offset[index][0],array_offset[index][1]])(MKPOL([[[float(num_list[0]),float(num_list[1])],[float(num_list[2]),float(num_list[3])]],[[1,2]],1])))
            
        file.close()
        index = index+1

        structure.append
 
    return STRUCT(structure)




def create_floor(elem,divisor):

    """
    the function takes as input a file containing lists
    of numbers. the purpose is to take the minimum and the
    maximum with respect to x and y, and the build-up.
    """
    
    structure = []
    xMIN = 100000000
    yMIN = 100000000
    xMAX = -1
    yMAX = -1
    cont1=0
    cont2=0
    
    file = open(elem)
    
    for single_line in file:
            
         num_list = single_line.split(',')
            
         if(xMIN>float(num_list[0])):
             xMIN = float(num_list[0])
                
         if(xMIN>float(num_list[2])):
            xMIN = float(num_list[2])

         if(xMAX<float(num_list[0])):
            xMAX = float(num_list[0])
                
         if(xMAX<float(num_list[2])):
            xMAX = float(num_list[2])
                
         if(yMIN>float(num_list[1])):
            yMIN = float(num_list[1])
                
         if(yMIN>float(num_list[3])):
            yMIN = float(num_list[3])

         if(yMAX<float(num_list[1])):
            yMAX = float(num_list[1])
                
         if(yMAX<float(num_list[3])):
            yMAX = float(num_list[3])
            
    file.close()

    x = xMAX-xMIN
    y = yMAX-yMIN
    i = x/divisor
    j = y/divisor
    traslx = 0
    trasly = 0
    structure.append(S(3)(-1))
    while(cont1<divisor):

        cont2=0
        trasly = 0
        while(cont2<divisor):

            structure.append(TEXTURE("images/parquet.jpg")(T([1,2])([xMIN+traslx,yMIN+trasly])(CUBOID([i,j,1]))))
            trasly = trasly+ j
            cont2 = cont2+1
            
        cont1 = cont1+1
        traslx = traslx+i
        

    structure = (STRUCT(structure))
 
    return structure




def create_glass_doors_windows(elem,offset):

    """
    This function takes as input a file containing a list
    of numbers that deals with the construction of the house windows and doors, and the offset value that must configure.
    """
    
    structure = []
    file = open(elem)
        
    for single_line in file:
            
        num_list = single_line.split(',')        
        structure.append(OFFSET([offset[0],offset[1]])(MKPOL([[[float(num_list[0]),float(num_list[1])],[float(num_list[2]),float(num_list[3])]],[[1,2]],1])))
               
    file.close()
 
    return STRUCT(structure)


ggpl_planimetry3D(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt"])


