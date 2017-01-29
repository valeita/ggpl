from pyplasm import *
from workshop_03 import *
from workshop_08 import *
from workshop_09 import *


def design_of_parametric_multistorey_house(files_folder, num_planes, num_appartment,house_x, house_y, house_z):
    """
    this function takes a list of files to build the planimetry,
    the number of planes of the building, the number of appartment
    for every plane, and the dimension of the house x,y and z.
    It return the hpc of the completed building
    """
    building = []
    h_roof = house_z/5.
    house_z = house_z-h_roof

    
    appartment_x = house_x
    appartment_z = house_z/num_planes
    appartment_y = house_y/num_appartment
    dim_beams = (appartment_x + appartment_y)/50.
    appartment_x = appartment_x - (2*(dim_beams))
    appartment_z = appartment_z - (dim_beams)
    appartment_y = appartment_y - (dim_beams)
    appartment = ggpl_planimetry3D([files_folder[0],files_folder[1],files_folder[2],files_folder[3],files_folder[4],files_folder[5],files_folder[6],files_folder[7],files_folder[8],files_folder[9],files_folder[10],files_folder[11],files_folder[12]],appartment_x,appartment_y,appartment_z,dim_beams)
    i=0
    trasly = 0

    if(appartment_y < appartment_z*2):
        exit("put in the correct data input. The house must be more large.")
    while(i<num_appartment):
                
        appartments_stack = generate_planes(num_planes,num_appartment,appartment_z,dim_beams,appartment)
                
        if(num_planes>1):
            ramp = generate_ramps(appartment_x,appartment_y,appartment_z,num_planes,dim_beams)
            appartments_stack = STRUCT([ramp,appartments_stack])
        building.append(T(2)(trasly)(STRUCT([appartments_stack])))
        i=i+1

        trasly = trasly+appartment_y + dim_beams
                
    roof = generate_roof(house_x,house_y,house_z,h_roof)
    project = T(1)(appartment_y/8.)(STRUCT([roof,STRUCT(building)]))
    #VIEW(project)
    return project
        



def generate_planes(num_planes, num_appartment,z_appartment,dim_beams,appartment):

    """
    this function takes the number of planes of the building, the number of appartment
    for every plane, and the dimension of the single appartment about z, the beam's dimension,
    and the appartment hpc.
    It return the hpc of the appartment's stack.
    """
    i=0
    house = []
    trasl_1 = 0
    trasl_2 = 0
    while(i<num_planes):

        house.append(T(3)(trasl_1+trasl_2)(appartment))
        trasl_1 = trasl_1+z_appartment
        trasl_2 = trasl_2+dim_beams
        i=i+1
    return STRUCT(house)


def generate_roof(house_x,house_y,house_z,h_roof):

    """
    this function takes the house's dimension about x,y,z and the quote of the roof.
    It return the hpc of the completed roof.
    """
    
    roof = ggpl_geometric_building_roof([[[0,0,0],[0,house_y,0]],[[0,house_y,0],[house_x,house_y,0]],[[house_x,house_y,0],[house_x,0,0]],[[house_x,0,0],[0,0,0]]],h_roof)  
    return T(3)(house_z)(roof)




def generate_ramps(appartment_x,appartment_y,appartment_z,num_planes,dim_beams):

    """
    this function takes the dimension of the single appartment about x,y,z,
    the number of planes and the beam's dimension.
    It return the hpc of the completed ramp.
    """
    
    ramp_x = appartment_x/2.5
    ramp_y = appartment_y/10.
    ramp_z = appartment_z+dim_beams
    i=0
    trasl = 0
    ramps = []
    bool = 0
    while(i<num_planes-1):

        if(i==num_planes-2):
            bool = 1
            
        ramp = ggpl_building_stairs_with_landings(ramp_x,ramp_y,ramp_z,bool)
        ramps.append(T([2,3])([(appartment_y/2.)-(appartment_y/40.),trasl])(R([1,2])(PI/2)(ramp)))
        i=i+1
        trasl = trasl+appartment_z+dim_beams
  
        
    return T(1)(-0.09)(STRUCT(ramps))
    

    
    
#design_of_parametric_multistorey_house(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt","file_txt/terrace.txt"], 4, 3,8,30,9)
