from pyplasm import *
from workshop_10 import *

def model_of_suburban_neighborhood():

    tree_1 = generate_tree(0.22,0.589)
    #tree_2 = generate_tree(0.22,0.9)
    #tree_3 = generate_tree(0.22,1.2)
    house_4 = design_of_parametric_multistorey_house(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt","file_txt/terrace.txt"], 2, 7, 6.15,28,4)
    house_3 = design_of_parametric_multistorey_house(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt","file_txt/terrace.txt"], 2, 6, 6.15,24,4)
    house_2 = design_of_parametric_multistorey_house(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt","file_txt/terrace.txt"], 2, 5, 6.15,20,4)
    house_1 = design_of_parametric_multistorey_house(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt","file_txt/terrace.txt"], 2, 4, 6.15,16,4)
    #model_plane = generate_model_plane()


    district = []
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[0,10],[10,10]],1.8,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[10,0],[10,10]],1.8,100]),Q(0.1)])))   
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[10,10],[45,10],[75,50]],1.8,100]),Q(0.1)])))
    
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[46,24],[43,22],[40,85]],1.8,100]),Q(0.1)]))) #RETTA DI DESTRA VERSO L'ALTO
    
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[41,50],[105,50]],1.8,100]),Q(0.1)]))) #RETTA
    
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[10,10],[10,25],[20,45],[3,85]],1.8,100]),Q(0.1)]))) #RETTA DI SINISTRA DAL BASSO VERSO L'ALTO
    
    district.append(T([1,2])([7,52])(R([1,2])(PI+PI/40)(house_2)))
    district.append(T([1,2])([-1,79])(R([1,2])(PI+PI/10)(house_3)))
    district.append(T([1,2])([13,15])(R([1,2])(-PI/30)(house_3)))
    district.append(T([1,2])([16,41])(R([1,2])(PI/40)(house_2)))
    district.append(T([1,2])([13,63])(R([1,2])(PI/10)(house_1)))

    district.append(T([1,2])([37,41])(R([1,2])(PI+PI/50)(house_2)))
    district.append(T([1,2])([36,60])(R([1,2])(PI+PI/50)(house_1)))
    district.append(T([1,2])([35,82])(R([1,2])(PI+PI/50)(house_2))) 
    district.append(T([1,2])([44,54])(R([1,2])(PI/50)(house_3)))
    district.append(T([1,2])([78,54])(R([1,2])(PI/2)(house_3)))
    district.append(T([1,2])([103,54])(R([1,2])(PI/2)(house_2)))
    district.append(T([1,2])([83,48])(R([1,2])(-PI/2)(house_2)))   
    district.append(T([1,2])([59,28])(R([1,2])(-PI/2+(PI/4)+(PI/50))(house_3)))
    
    district.append(T([1,2])([35,10])(R([1,2])(-PI/2+(PI/4)-(PI/20))(house_4)))




    
    district.append(T([1,2])([15,30])(tree_1))
    VIEW(STRUCT(district))
    return 1



def generate_tree(r_trunk,h_trunk):

    tree2D = MKPOL([[[0.5,0.3,0],[0.9,0.3,0],[0,0.3,0],[1.4,0.3,0],[0.5,0.8,0],[0.9,0.8,0],[0.1,0.8,0],[1.3,0.8,0],[0.5,1.2,0],[0.9,1.2,0],
                     [0.2,1.2,0],[1.2,1.2,0],[0.5,1.5,0],[0.9,1.5,0],[0.3,1.5,0],[1.1,1.5,0],[0.5,1.7,0],[0.9,1.7,0],[0.4,1.7,0],[1.0,1.7,0],
                     [0.6,1.9,0],[0.8,1.9,0],[0.5,1.9,0],[0.9,1.9,0],[0.7,2.1,0]],[[1,2,3,4,5,6],[5,6,7,8,9,10],
                     [9,10,11,12,13,14],[13,14,15,16,17,18],[17,18,19,20,21,22],[21,22,23,24,25]],[[1]]])
    
    tree2D = T([1,2])([-0.7,h_trunk-0.3])(tree2D)
    angle = 1
    tree3D = []
    trunk3D = []
    while(angle<37):
        tree3D.append(R([1,3])(PI/13))
        tree3D.append(tree2D)
        angle = angle+1

    tree3D = TEXTURE("images/tree.jpg")(OFFSET([0.05,0.05,0.05])(STRUCT(tree3D)))
    tree3D = R([2,3])(PI/2)(tree3D)
    trunk3D = TEXTURE("images/trunk.jpg")(CYLINDER([r_trunk,h_trunk])(50))

    tree = T([1,2])([0.7,0.7])(STRUCT([tree3D, trunk3D]))
    return tree


def generate_model_plane():


    plane = TEXTURE("images/legno.jpg")(CUBOID([100,100,3]))
    meadow = T(3)(3)(TEXTURE("images/legno.jpg")(CUBOID([100,100,0.2])))


    return STRUCT([plane,meadow])








        
model_of_suburban_neighborhood()

