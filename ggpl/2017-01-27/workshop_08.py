from pyplasm import *
from larlib import *

def ggpl_planimetry3D(file_list,lun_box_x, lun_box_y, lun_box_z,dim_beams):

    """
    the function takes into exactly 9 input file
    containing lists of useful numbers for the construction
    of the casa.l'input is static and must not be varied.
    """
    walls = []
    wind = []
    others = []
    coords = return_origin(file_list)
    x_ret = coords[0]
    y_ret = coords[1]
    perc = generate_percentual(coords,lun_box_x, lun_box_y,lun_box_z,dim_beams)

    walls.append(T(2)(coords[3]))
    walls.append(S(2)(-1))
    walls.append(PROD([create_walls([file_list[0],file_list[1],file_list[2]],x_ret,y_ret,perc),Q(lun_box_z)]))
    walls.append(PROD([create_walls([file_list[12]],x_ret,y_ret,perc),Q(lun_box_z/2.)]))
    wind.append(T(2)(coords[3]))
    wind.append(S(2)(-1)(T(3)((lun_box_z/100.)*38.4615)(PROD([create_glass_doors_windows(file_list[8],[14,14],x_ret,y_ret,perc),Q((lun_box_z/100.)*38.4615)]))))
    walls.append((T(3)((lun_box_z/100.)*76.923)(PROD([create_glass_doors_windows(file_list[9],[6,6],x_ret,y_ret,perc),Q((lun_box_z/100.)*23.0769)]))))
    walls.append((T(3)((lun_box_z/100.)*76.923)(PROD([create_glass_doors_windows(file_list[10],[20,20],x_ret,y_ret,perc),Q((lun_box_z/100.)*23.0769)]))))
    walls.append((T(3)((lun_box_z/100.)*76.923)(PROD([create_glass_doors_windows(file_list[11],[13,13],x_ret,y_ret,perc),Q((lun_box_z/100.)*23.0769)]))))
    house_part1 = TEXTURE("images/tint.jpg")(DIFFERENCE([STRUCT(walls),STRUCT(wind)]))

    others.append(T(2)(coords[3]))
    others.append(S(2)(-1))
    others.append(perc[2])
    others.append(create_floor(file_list[4],9,x_ret,y_ret,perc,lun_box_z))
    others.append(create_floor(file_list[5],6,x_ret,y_ret,perc,lun_box_z))
    others.append(create_floor(file_list[6],1,x_ret,y_ret,perc,lun_box_z))
    others.append(TEXTURE("images/glass.jpg")(PROD([create_glass_doors_windows(file_list[3],[2,2],x_ret,y_ret,perc),Q((lun_box_z/100.)*76.923)])))
    others.append(TEXTURE("images/glass.jpg")(PROD([create_glass_doors_windows(file_list[7],[13,13],x_ret,y_ret,perc),Q(lun_box_z)])))

    house_part2 = STRUCT(others)
    
    house_completed = STRUCT([house_part1,house_part2])
    house_completed = T([1,2])(dim_beams)(house_completed)
    house_completed = T(2)(-coords[3]+lun_box_y+dim_beams)(house_completed)
    #VIEW(house_completed)
    return house_completed


def create_walls(file_list,x_ret,y_ret,perc):

    """
    This function takes as input a list of files.
    it must contain exactly 3 files, two of which relate to
    the construction of the exterior walls, and the interior walls.
    """

    index = 0
    structure = []
    array_offset = [[(20/100.)*perc[0],(20/100.)*perc[1]],[(13/100.)*perc[0],(13/100.)*perc[1]],[(6/100.)*perc[0],(6/100.)*perc[1]]]

    xMIN = 100000000
    yMIN = 100000000
    xMAX = -1
    yMAX = -1
    for elem in file_list:
    
        file = open(elem)
        
        for single_line in file:
            
            num_list = single_line.split(',')
            structure.append(OFFSET([array_offset[index][0],array_offset[index][1]])(MKPOL([[[((float(num_list[0])-x_ret)/100.)*perc[0],((float(num_list[1])-y_ret)/100.)*perc[1]],[((float(num_list[2])-x_ret)/100.)*perc[0],((float(num_list[3])-y_ret)/100.)*perc[1]]],[[1,2]],1])))
            
        file.close()
        index = index+1

        structure.append
 
    return STRUCT(structure)




def create_floor(elem,divisor,x_ret,y_ret,perc,lun_box_z):

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

            structure.append(TEXTURE("images/parquet.jpg")(T([1,2])([((xMIN+traslx-x_ret)/100.)*perc[0],((yMIN+trasly-y_ret)/100.)*perc[1]])(CUBOID([((i)/100.)*perc[0],((j)/100.)*perc[1],lun_box_z/100.]))))
            trasly = trasly+ j
            cont2 = cont2+1
            
        cont1 = cont1+1
        traslx = traslx+i
        
    return STRUCT(structure)




def create_glass_doors_windows(elem,offset,x_ret,y_ret,perc):

    """
    This function takes as input a file containing a list
    of numbers that deals with the construction of the house windows and doors, and the offset value that must configure.
    """
    
    structure = []
    file = open(elem)
        
    for single_line in file:
            
        num_list = single_line.split(',')        
        structure.append(OFFSET([((offset[0])/100.)*perc[0],((offset[1])/100.)*perc[1]])(MKPOL([[[((float(num_list[0])-x_ret)/100.)*perc[0],((float(num_list[1])-y_ret)/100.)*perc[1]],[((float(num_list[2])-x_ret)/100.)*perc[0],((float(num_list[3])-y_ret)/100.)*perc[1]]],[[1,2]],1])))
               
    file.close()
 
    return STRUCT(structure)



def return_origin(file_list):

    xMIN = 100000000
    yMIN = 100000000
    xMAX = -1
    yMAX = -1

    for elem in file_list:
          
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

    return [xMIN,yMIN,xMAX,yMAX]
    



def generate_percentual(coords,lun_box_x, lun_box_y,lun_box_z,l_independent):

    structure = []
    beams = []
    lun_x_plane = coords[2]-coords[0]
    lun_y_plane = coords[3]-coords[1]
    
    perc_x = (100/lun_x_plane)*lun_box_x
    perc_y = (100/lun_y_plane)*lun_box_y

    xMIN = ((coords[0])/100.)*perc_x
    yMIN = ((coords[1])/100.)*perc_y
    xMAX = ((coords[2])/100.)*perc_x
    yMAX = ((coords[3])/100.)*perc_y

    structure.append(T(3)(-(lun_box_z)/40.)(TEXTURE("images/rock.jpg")(OFFSET([(lun_box_z/100.),(lun_box_z/100.),(lun_box_z/100.)])(CUBOID([xMAX,yMAX,lun_box_z/100])))))

    structure.append(TEXTURE("images/pillars.jpg")(MKPOL([[[xMIN,yMIN,0],[xMIN-l_independent,yMIN,0],[xMIN,yMIN-l_independent,0],[xMIN-l_independent,yMIN-l_independent,0],[xMIN,yMIN,lun_box_z],[xMIN-l_independent,yMIN,lun_box_z],[xMIN,yMIN-l_independent,lun_box_z],[xMIN-l_independent,yMIN-l_independent,lun_box_z]],[[1,2,3,4,5,6,7,8]],[1]])))    
    structure.append(TEXTURE("images/pillars.jpg")(MKPOL([[[xMAX,yMIN,0],[xMAX+l_independent,yMIN,0],[xMAX,yMIN-l_independent,0],[xMAX+l_independent,yMIN-l_independent,0],[xMAX,yMIN,lun_box_z],[xMAX+l_independent,yMIN,lun_box_z],[xMAX,yMIN-l_independent,lun_box_z],[xMAX+l_independent,yMIN-l_independent,lun_box_z]],[[1,2,3,4,5,6,7,8]],[1]])))    
    structure.append(TEXTURE("images/pillars.jpg")(MKPOL([[[xMIN,yMAX,0],[xMIN-l_independent,yMAX,0],[xMIN,yMAX+l_independent,0],[xMIN-l_independent,yMAX+l_independent,0],[xMIN,yMAX,lun_box_z],[xMIN-l_independent,yMAX,lun_box_z],[xMIN,yMAX+l_independent,lun_box_z],[xMIN-l_independent,yMAX+l_independent,lun_box_z]],[[1,2,3,4,5,6,7,8]],[1]])))
    structure.append(TEXTURE("images/pillars.jpg")(MKPOL([[[xMAX,yMAX,0],[xMAX+l_independent,yMAX,0],[xMAX,yMAX+l_independent,0],[xMAX+l_independent,yMAX+l_independent,0],[xMAX,yMAX,lun_box_z],[xMAX+l_independent,yMAX,lun_box_z],[xMAX,yMAX+l_independent,lun_box_z],[xMAX+l_independent,yMAX+l_independent,lun_box_z]],[[1,2,3,4,5,6,7,8]],[1]])))

    beams.append(TEXTURE("images/beams.jpg")(MKPOL([[[xMIN-l_independent,yMIN-l_independent,0],[xMIN-l_independent,yMIN,0],[xMIN-l_independent,yMIN-l_independent,-l_independent],[xMIN-l_independent,yMIN,-l_independent],[xMAX+l_independent,yMIN-l_independent,0],[xMAX+l_independent,yMIN,0],[xMAX+l_independent,yMIN-l_independent,-l_independent],[xMAX+l_independent,yMIN,-l_independent]],[[1,2,3,4,5,6,7,8]],[1]])))
    beams.append(TEXTURE("images/beams.jpg")(MKPOL([[[xMIN-l_independent,yMIN-l_independent,0],[xMIN,yMIN-l_independent,0],[xMIN-l_independent,yMIN-l_independent,-l_independent],[xMIN,yMIN-l_independent,-l_independent],[xMIN,yMAX+l_independent,0],[xMIN-l_independent,yMAX+l_independent,0],[xMIN,yMAX+l_independent,-l_independent],[xMIN-l_independent,yMAX+l_independent,-l_independent]],[[1,2,3,4,5,6,7,8]],[1]])))
    beams.append(TEXTURE("images/beams.jpg")(MKPOL([[[xMAX,yMIN,0],[xMAX+l_independent,yMIN,0],[xMAX+l_independent,yMAX+l_independent,0],[xMAX,yMAX+l_independent,0],[xMAX,yMIN,-l_independent],[xMAX+l_independent,yMIN,-l_independent],[xMAX+l_independent,yMAX+l_independent,-l_independent],[xMAX,yMAX+l_independent,-l_independent]],[[1,2,3,4,5,6,7,8]],[1]])))
    beams.append(TEXTURE("images/beams.jpg")(MKPOL([[[xMIN-l_independent,yMAX+l_independent,0],[xMIN-l_independent,yMAX,0],[xMIN-l_independent,yMAX,-l_independent],[xMIN-l_independent,yMAX+l_independent,-l_independent],[xMAX+l_independent,yMAX+l_independent,0],[xMAX+l_independent,yMAX,0],[xMAX+l_independent,yMAX+l_independent,-l_independent],[xMAX+l_independent,yMAX,-l_independent]],[[1,2,3,4,5,6,7,8]],[1]])))

    down = STRUCT(beams)
    up = []
    up.append(T(3)(lun_box_z+l_independent)(STRUCT(beams)))
    up = STRUCT(up)
    structure = STRUCT(structure)

    return [perc_x,perc_y,STRUCT([structure,up])]

#ggpl_planimetry3D(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt","file_txt/terrace.txt"],30,30,7,1)


