from pyplasm import *
from workshop_10 import *

def model_of_suburban_neighborhood():

    """
    The main function, does not take any input
    parameter to be processed, and thus produces
    a totally static result.
    """
    
    house_4 = design_of_parametric_multistorey_house(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt","file_txt/terrace.txt"], 2, 7, 6.15,28,4)
    house_3 = design_of_parametric_multistorey_house(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt","file_txt/terrace.txt"], 2, 6, 6.15,24,4)
    house_2 = design_of_parametric_multistorey_house(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt","file_txt/terrace.txt"], 2, 5, 6.15,20,4)
    house_1 = design_of_parametric_multistorey_house(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt","file_txt/terrace.txt"], 2, 4, 6.15,16,4)
    
    #STREET:
    district = []
    little_s = []
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[-10,10],[10,10]],1.8,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[10,0],[10,10]],1.8,100]),Q(0.1)])))   
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[10,10],[45,10],[75,50]],1.8,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[46,24],[43,22],[40,85]],1.8,100]),Q(0.1)]))) #RETTA DI DESTRA VERSO L'ALTO  
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[41,50],[105,50]],1.8,100]),Q(0.1)]))) #RETTA   
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[10,10],[10,25],[20,45],[3,85]],1.8,100]),Q(0.1)]))) #RETTA DI SINISTRA DAL BASSO VERSO L'ALTO
    



    #LITTLE STREET:

    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[10,16.5],[12.5,16.5]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[10.5,20.5],[13,20.5]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[11,24.5],[13.5,24.5]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[11.5,28.5],[14,28.5]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[12,32.5],[14.5,32.5]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[12.5,36.5],[15,36.5]],1.3,100]),Q(0.1)])))



    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[12.2,42.7],[15.2,42.7]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[12,46.7],[15,46.7]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[11.6,50.7],[14.6,50.7]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[11,54.7],[14.2,54.7]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[10.5,58.7],[13.5,58.7]],1.3,100]),Q(0.1)])))



    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[9.2,63.6],[12.2,64.3]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[7.5,67.3],[10.5,68]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[6.5,71.3],[9.5,72]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[5.3,75.3],[8.3,76]],1.3,100]),Q(0.1)])))



    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[9.2,33.4],[11.8,33.2]],1.3,100]),Q(0.1)])))    
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[8.9,37.4],[11.8,37.2]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[8.4,41.4],[11.8,41.2]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[7.9,45.4],[11.8,45.2]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[7.5,49.4],[11.8,49.2]],1.3,100]),Q(0.1)])))


    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[7,57.6],[10.5,58.4]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[5.5,61.6],[9,62.4]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[4.5,65],[7.8,66.4]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[3.2,69],[6.5,70.4]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[1.7,73],[6.5,74.4]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[0.8,77],[5.6,78.4]],1.3,100]),Q(0.1)])))
    

    little_s.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[37.7,47.2],[41,47.2]],1.3,100]),Q(0.1)])))
    little_s.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[37.8,51.2],[41,51.2]],1.3,100]),Q(0.1)])))
    little_s.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[37.6,55.2],[41,55.2]],1.3,100]),Q(0.1)])))
    little_s.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[37.4,59.2],[41,59.2]],1.3,100]),Q(0.1)])))

    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[67.8,43.3],[70,41.2]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[70.8,46.3],[73,44.2]],1.3,100]),Q(0.1)])))




    
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[33,15],[35.5,11.2]],1.3,100]),Q(0.1)]))) 
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[37,17],[39.2,13.7]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[40.5,19],[42.5,16.2]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[44,21],[46,18.2]],1.3,100]),Q(0.1)])))  
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[47,24],[49.5,21]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[50.5,27],[52.5,23.5]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[53.6,29],[55.5,26]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[41.5,19.5],[42.5,26],[38.5,26]],1.3,100]),Q(0.1)])))   
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[38.5,28.7],[43,28.7]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[38.5,32.7],[42,32.7]],1.3,100]),Q(0.1)])))   
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[38,36.7],[42,36.7]],1.3,100]),Q(0.1)])))
    district.append(TEXTURE("images/asfalto.jpg")(PROD([BEZIERSTRIPE([[[38,40.7],[42,40.7]],1.3,100]),Q(0.1)])))
    
    
    little_s = STRUCT(little_s)
    district.append(little_s)

    district.append(T([1,2])([-1.9,21.3])(R([1,2])(-PI/2+(PI/4)+(PI/50))(little_s)))
    district.append(T([1,2])([144.8,10.9])(R([1,2])(PI/2)(little_s)))
    district.append(T([1,2])([148.8,10.9])(R([1,2])(PI/2)(little_s)))

    district.append(T([1,2])([144.8,12.5])(R([1,2])(PI/2)(little_s)))
    district.append(T([1,2])([148.8,12.5])(R([1,2])(PI/2)(little_s)))
    district.append(T([1,2])([115,12.5])(R([1,2])(PI/2)(little_s)))
    district.append(T([1,2])([119,12.5])(R([1,2])(PI/2)(little_s)))
    district.append(T([1,2])([123,12.5])(R([1,2])(PI/2)(little_s)))
    district.append(T([1,2])([1.7,8.5])(little_s))
    district.append(T([1,2])([1.3,16.5])(little_s)) 
    district.append(T([1,2])([-1,18])(little_s))
    district.append(T([1,2])([-1,22])(little_s))

    

    #HOUSE:
    
    district.append(T([1,2])([7,52])(R([1,2])(PI+PI/40)(house_2)))
    district.append(T([1,2])([-1,79])(R([1,2])(PI+PI/10)(house_3)))
    district.append(T([1,2])([13,15])(R([1,2])(-PI/30)(house_3)))
    district.append(T([1,2])([16,41])(R([1,2])(PI/40)(house_2)))
    district.append(T([1,2])([13,63])(R([1,2])(PI/10)(house_1)))
    district.append(T([1,2])([37,43])(R([1,2])(PI+PI/50)(house_2)))
    district.append(T([1,2])([36,62])(R([1,2])(PI+PI/50)(house_1)))
    district.append(T([1,2])([35,84])(R([1,2])(PI+PI/50)(house_2)))
    district.append(T([1,2])([44,54])(R([1,2])(PI/50)(house_3)))
    district.append(T([1,2])([78,54])(R([1,2])(PI/2)(house_3)))
    district.append(T([1,2])([103,54])(R([1,2])(PI/2)(house_2)))
    district.append(T([1,2])([83,48])(R([1,2])(-PI/2)(house_2)))   
    district.append(T([1,2])([59,28])(R([1,2])(-PI/2+(PI/4)+(PI/50))(house_3)))
    district.append(T([1,2])([35,10])(R([1,2])(-PI/2+(PI/4)-(PI/20))(house_4)))



    #TREE

    district.append(T([1,2])([7,3])(random_tree()))
    district.append(T([1,2])([7,12])(random_tree()))
    district.append(T([1,2])([10,8])(random_tree()))
    district.append(T([1,2])([1,6])(random_tree()))
    district.append(T([1,2])([10,2])(random_tree()))
    
    district.append(T([1,2])([2,2])(random_tree()))
    district.append(T([1,2])([3,3])(random_tree()))
    district.append(T([1,2])([-1,1])(random_tree()))
    district.append(T([1,2])([-2,4])(random_tree()))
    district.append(T([1,2])([-3,3])(random_tree()))
    district.append(T([1,2])([-2,12])(random_tree()))

    district.append(T([1,2])([-4,7])(random_tree()))
    district.append(T([1,2])([-5,1])(random_tree()))
    district.append(T([1,2])([-2,14])(random_tree()))
    district.append(T([1,2])([13,2])(random_tree()))
    district.append(T([1,2])([13,4])(random_tree()))
    district.append(T([1,2])([13,6])(random_tree()))
    district.append(T([1,2])([13,8])(random_tree()))

    district.append(T([1,2])([-2,14])(random_tree()))
    district.append(T([1,2])([-2,16])(random_tree()))
    district.append(T([1,2])([-2,14])(random_tree()))
    district.append(T([1,2])([-2,19])(random_tree()))
    district.append(T([1,2])([-4,13])(random_tree()))
    district.append(T([1,2])([-4,17])(random_tree()))
    district.append(T([1,2])([-4,21])(random_tree()))
    district.append(T([1,2])([-4,25])(random_tree()))
    district.append(T([1,2])([0,4])(random_tree()))
    district.append(T([1,2])([0,8])(random_tree()))
    district.append(T([1,2])([0,15])(random_tree()))
    district.append(T([1,2])([0,17])(random_tree()))

    district.append(T([1,2])([-6,1])(random_tree()))
    district.append(T([1,2])([-6,3])(random_tree()))
    district.append(T([1,2])([-7,5])(random_tree()))
    district.append(T([1,2])([-7,8])(random_tree()))
    district.append(T([1,2])([-9,2])(random_tree()))
    district.append(T([1,2])([-9,13])(random_tree()))
    district.append(T([1,2])([-9,15])(random_tree()))
    district.append(T([1,2])([-6,19])(random_tree()))
    

    #NEW TREE
    

    
    
    
    

    

























    
    plane = TEXTURE("images/legno.jpg")(CUBOID([160,140,2]))
    district = T([1,2,3])([30,20,2.2])(STRUCT(district))
    meadow = T([1,2,3])([20,20,2])(TEXTURE("images/prato.jpg")(CUBOID([120,100,0.2])))
    
    model = STRUCT([district,plane,meadow])
    
    VIEW(model)
    return model



def generate_tree(r_trunk,h_trunk):
    
    """
    This function takes as input respectively the
    radius of the trunk, the base, and its height.
    The tree trunk is instead built statically.
    The function returns the tree as hpc.
    """
    
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





def random_tree():

    """
    This function does not take any
    input parameter. It returns a random tree as a hpc.
    """
    
    n = randint(0,11)
    
    if(n < 3):

        tree = generate_tree(0.22,0.589)

    if(2 < n < 6):

        tree = generate_tree(0.22,0.9)

    if(5 < n < 9):

        tree = generate_tree(0.22,1.2)

    if(n > 8):

        tree = generate_tree(0.22,1.9)

    return tree
    




        
model_of_suburban_neighborhood()

