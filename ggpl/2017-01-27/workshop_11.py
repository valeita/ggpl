from pyplasm import *
from workshop_10 import *

def model_of_suburban_neighborhood():

    """
    The main function, does not take any input
    parameter to be processed, and thus produces
    a totally static result.
    """
    
    house_4 = design_of_parametric_multistorey_house(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt","file_txt/terrace.txt"], 1, 7, 6.15,28,4)
    house_3 = design_of_parametric_multistorey_house(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt","file_txt/terrace.txt"], 2, 6, 6.15,24,6)
    house_2 = design_of_parametric_multistorey_house(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt","file_txt/terrace.txt"], 3, 5, 6.15,20,8)
    house_1 = design_of_parametric_multistorey_house(["file_txt/external_walls.txt","file_txt/external_walls2.txt","file_txt/internal_walls.txt","file_txt/glass_doors.txt","file_txt/floor1.txt","file_txt/floor2.txt","file_txt/floor3.txt","file_txt/glass_windows.txt","file_txt/windows.txt","file_txt/up_doors1.txt","file_txt/up_doors2.txt","file_txt/up_doors3.txt","file_txt/terrace.txt"], 5, 4, 6.15,16,10)

    #STREET:
    #[![house_1.png](https://s20.postimg.org/61nncuv9p/house_1.png)](https://postimg.org/image/aasdf0yix/)
    #[![house_2.png](https://s20.postimg.org/kyw4dv8i5/house_2.png)](https://postimg.org/image/br3vx61ft/)
    #[![house_3.png](https://s20.postimg.org/uxh30chxp/house_3.png)](https://postimg.org/image/chwm2y3t5/)
    #[![house_4.png](https://s20.postimg.org/6v095h1al/house_4.png)](https://postimg.org/image/dlgqewog9/)
    
    street = []
    little_s = []
    house = []
    trees = []
    street.append((PROD([BEZIERSTRIPE([[[-10,10],[10,10]],1.8,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[10,0],[10,10]],1.8,100]),Q(0.1)])))   
    street.append((PROD([BEZIERSTRIPE([[[10,10],[45,10],[75,50]],1.8,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[46,24],[43,22],[40,85]],1.8,100]),Q(0.1)]))) #RETTA DI DESTRA VERSO L'ALTO  
    street.append((PROD([BEZIERSTRIPE([[[41,50],[105,50]],1.8,100]),Q(0.1)]))) #RETTA   
    street.append((PROD([BEZIERSTRIPE([[[10,10],[10,25],[20,45],[3,85]],1.8,100]),Q(0.1)]))) #RETTA DI SINISTRA DAL BASSO VERSO L'ALTO

    #LITTLE STREET:

    street.append((PROD([BEZIERSTRIPE([[[10,16.5],[12.5,16.5]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[10.5,20.5],[13,20.5]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[11,24.5],[13.5,24.5]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[11.5,28.5],[14,28.5]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[12,32.5],[14.5,32.5]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[12.5,36.5],[15,36.5]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[12.2,42.7],[15.2,42.7]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[12,46.7],[15,46.7]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[11.6,50.7],[14.6,50.7]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[11,54.7],[14.2,54.7]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[10.5,58.7],[13.5,58.7]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[9.2,63.6],[12.2,64.3]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[7.5,67.3],[10.5,68]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[6.5,71.3],[9.5,72]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[5.3,75.3],[8.3,76]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[9.2,33.4],[11.8,33.2]],1.3,100]),Q(0.1)])))    
    street.append((PROD([BEZIERSTRIPE([[[8.9,37.4],[11.8,37.2]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[8.4,41.4],[11.8,41.2]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[7.9,45.4],[11.8,45.2]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[7.5,49.4],[11.8,49.2]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[7,57.6],[10.5,58.4]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[5.5,61.6],[9,62.4]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[4.5,65],[7.8,66.4]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[3.2,69],[6.5,70.4]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[1.7,73],[6.5,74.4]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[0.8,77],[5.6,78.4]],1.3,100]),Q(0.1)])))
    little_s.append((PROD([BEZIERSTRIPE([[[37.7,47.2],[41,47.2]],1.3,100]),Q(0.1)])))
    little_s.append((PROD([BEZIERSTRIPE([[[37.8,51.2],[41,51.2]],1.3,100]),Q(0.1)])))
    little_s.append((PROD([BEZIERSTRIPE([[[37.6,55.2],[41,55.2]],1.3,100]),Q(0.1)])))
    little_s.append((PROD([BEZIERSTRIPE([[[37.4,59.2],[41,59.2]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[67.8,43.3],[70,41.2]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[70.8,46.3],[73,44.2]],1.3,100]),Q(0.1)])))    
    street.append((PROD([BEZIERSTRIPE([[[33,15],[35.5,11.2]],1.3,100]),Q(0.1)]))) 
    street.append((PROD([BEZIERSTRIPE([[[37,17],[39.2,13.7]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[40.5,19],[42.5,16.2]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[44,21],[46,18.2]],1.3,100]),Q(0.1)])))  
    street.append((PROD([BEZIERSTRIPE([[[47,24],[49.5,21]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[50.5,27],[52.5,23.5]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[53.6,29],[55.5,26]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[41.5,19.5],[42.5,26],[38.5,26]],1.3,100]),Q(0.1)])))   
    street.append((PROD([BEZIERSTRIPE([[[38.5,28.7],[43,28.7]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[38.5,32.7],[42,32.7]],1.3,100]),Q(0.1)])))   
    street.append((PROD([BEZIERSTRIPE([[[38,36.7],[42,36.7]],1.3,100]),Q(0.1)])))
    street.append((PROD([BEZIERSTRIPE([[[38,40.7],[42,40.7]],1.3,100]),Q(0.1)]))) 
    little_s = STRUCT(little_s)
    street.append(little_s)
    street.append(T([1,2])([-1.9,21.3])(R([1,2])(-PI/2+(PI/4)+(PI/50))(little_s)))
    street.append(T([1,2])([144.8,10.9])(R([1,2])(PI/2)(little_s)))
    street.append(T([1,2])([148.8,10.9])(R([1,2])(PI/2)(little_s)))
    street.append(T([1,2])([144.8,12.5])(R([1,2])(PI/2)(little_s)))
    street.append(T([1,2])([148.8,12.5])(R([1,2])(PI/2)(little_s)))
    street.append(T([1,2])([115,12.5])(R([1,2])(PI/2)(little_s)))
    street.append(T([1,2])([119,12.5])(R([1,2])(PI/2)(little_s)))
    street.append(T([1,2])([123,12.5])(R([1,2])(PI/2)(little_s)))
    street.append(T([1,2])([1.7,8.5])(little_s))
    street.append(T([1,2])([1.3,16.5])(little_s)) 
    street.append(T([1,2])([-1,18])(little_s))
    street.append(T([1,2])([-1,22])(little_s))


    #HOUSE:
    
    house.append(T([1,2])([7,52])(R([1,2])(PI+PI/40)(house_2)))
    house.append(T([1,2])([-1,79])(R([1,2])(PI+PI/10)(house_3)))
    house.append(T([1,2])([13,15])(R([1,2])(-PI/30)(house_3)))
    house.append(T([1,2])([16,41])(R([1,2])(PI/40)(house_2)))
    house.append(T([1,2])([13,63])(R([1,2])(PI/10)(house_1)))
    house.append(T([1,2])([37,43])(R([1,2])(PI+PI/50)(house_2)))
    house.append(T([1,2])([36,62])(R([1,2])(PI+PI/50)(house_1)))
    house.append(T([1,2])([35,84])(R([1,2])(PI+PI/50)(house_2)))
    house.append(T([1,2])([44,54])(R([1,2])(PI/50)(house_3)))
    house.append(T([1,2])([78,54])(R([1,2])(PI/2)(house_3)))
    house.append(T([1,2])([103,54])(R([1,2])(PI/2)(house_2)))
    house.append(T([1,2])([83,48])(R([1,2])(-PI/2)(house_2)))   
    house.append(T([1,2])([59,28])(R([1,2])(-PI/2+(PI/4)+(PI/50))(house_3)))
    house.append(T([1,2])([35,10])(R([1,2])(-PI/2+(PI/4)-(PI/20))(house_4)))


    #TREE
    
    trees.append(T([1,2])([7,3])(random_tree()))
    """
    trees.append(T([1,2])([7,12])(random_tree()))
    trees.append(T([1,2])([10,8])(random_tree()))
    trees.append(T([1,2])([1,6])(random_tree()))
    trees.append(T([1,2])([10,2])(random_tree()))
    
    trees.append(T([1,2])([2,2])(random_tree()))
    trees.append(T([1,2])([3,3])(random_tree()))
    trees.append(T([1,2])([-1,1])(random_tree()))
    trees.append(T([1,2])([-2,4])(random_tree()))
    trees.append(T([1,2])([-3,3])(random_tree()))
    trees.append(T([1,2])([-2,12])(random_tree()))

    trees.append(T([1,2])([-4,7])(random_tree()))
    trees.append(T([1,2])([-5,1])(random_tree()))
    trees.append(T([1,2])([-2,14])(random_tree()))
    trees.append(T([1,2])([13,2])(random_tree()))
    trees.append(T([1,2])([13,4])(random_tree()))
    trees.append(T([1,2])([13,6])(random_tree()))
    trees.append(T([1,2])([13,8])(random_tree()))

    trees.append(T([1,2])([-2,14])(random_tree()))
    trees.append(T([1,2])([-2,16])(random_tree()))
    trees.append(T([1,2])([-2,14])(random_tree()))
    trees.append(T([1,2])([-2,19])(random_tree()))
    trees.append(T([1,2])([-4,13])(random_tree()))
    trees.append(T([1,2])([-4,17])(random_tree()))
    trees.append(T([1,2])([-4,21])(random_tree()))
    trees.append(T([1,2])([-4,25])(random_tree()))
    trees.append(T([1,2])([0,4])(random_tree()))
    trees.append(T([1,2])([0,8])(random_tree()))
    trees.append(T([1,2])([0,15])(random_tree()))
    trees.append(T([1,2])([0,17])(random_tree()))

    trees.append(T([1,2])([-6,1])(random_tree()))
    trees.append(T([1,2])([-6,3])(random_tree()))
    trees.append(T([1,2])([-7,5])(random_tree()))
    trees.append(T([1,2])([-7,8])(random_tree()))
    trees.append(T([1,2])([-9,2])(random_tree()))
    trees.append(T([1,2])([-9,13])(random_tree()))
    trees.append(T([1,2])([-9,15])(random_tree()))
    trees.append(T([1,2])([-6,19])(random_tree()))
    
    

    #NEW TREE
    

    trees.append(T([1,2])([13,13])(random_tree()))
    trees.append(T([1,2])([5,13])(random_tree()))
    trees.append(T([1,2])([5,16])(random_tree()))
    trees.append(T([1,2])([7,19])(random_tree()))
    trees.append(T([1,2])([7,23])(random_tree()))
    trees.append(T([1,2])([7,25])(random_tree()))
    trees.append(T([1,2])([8,27])(random_tree()))

    
    trees.append(T([1,2])([5,19])(random_tree()))
    trees.append(T([1,2])([5,21])(random_tree()))
    trees.append(T([1,2])([4,12])(random_tree()))
    trees.append(T([1,2])([4,14])(random_tree()))
    trees.append(T([1,2])([4,16])(random_tree()))
    trees.append(T([1,2])([4,18])(random_tree()))
    trees.append(T([1,2])([3,24])(random_tree()))
    trees.append(T([1,2])([3,27])(random_tree()))
    trees.append(T([1,2])([3,20])(random_tree()))

    
    trees.append(T([1,2])([12,12])(random_tree()))
    trees.append(T([1,2])([21,15])(random_tree()))
    trees.append(T([1,2])([21,17])(random_tree()))
    trees.append(T([1,2])([21,20])(random_tree()))




    trees.append(T([1,2])([23,18])(random_tree()))
    trees.append(T([1,2])([23,20])(random_tree()))
    trees.append(T([1,2])([23,22])(random_tree()))
    
    trees.append(T([1,2])([25,19])(random_tree()))
    trees.append(T([1,2])([25,23])(random_tree()))
    trees.append(T([1,2])([25,25])(random_tree()))
    trees.append(T([1,2])([25,27])(random_tree()))
    
    trees.append(T([1,2])([28,15])(random_tree()))
    trees.append(T([1,2])([28,17])(random_tree()))
    trees.append(T([1,2])([28,28])(random_tree()))
    trees.append(T([1,2])([28,20])(random_tree()))
    trees.append(T([1,2])([28,24])(random_tree()))
    trees.append(T([1,2])([28,22])(random_tree()))
    trees.append(T([1,2])([28,32])(random_tree()))




 
    trees.append(T([1,2])([25,22])(random_tree()))
    trees.append(T([1,2])([27,24])(random_tree()))
    trees.append(T([1,2])([29,26])(random_tree()))
    
    

    trees.append(T([1,2])([27,32])(random_tree()))
    trees.append(T([1,2])([28,35])(random_tree()))
    trees.append(T([1,2])([27,39])(random_tree()))
    trees.append(T([1,2])([28,43])(random_tree()))
    trees.append(T([1,2])([27,47])(random_tree()))
    trees.append(T([1,2])([28,49])(random_tree()))
    trees.append(T([1,2])([28,51])(random_tree()))
    trees.append(T([1,2])([26,55])(random_tree()))
    trees.append(T([1,2])([28,57])(random_tree()))
    trees.append(T([1,2])([26,59])(random_tree()))
    trees.append(T([1,2])([27,65])(random_tree()))
    trees.append(T([1,2])([28,67])(random_tree()))
    trees.append(T([1,2])([28,70])(random_tree()))
    trees.append(T([1,2])([26,74])(random_tree()))
    trees.append(T([1,2])([27,76])(random_tree()))
    trees.append(T([1,2])([26,79])(random_tree()))
    trees.append(T([1,2])([27,82])(random_tree()))
    trees.append(T([1,2])([27,85])(random_tree()))
    
    trees.append(T([1,2])([25,32])(random_tree()))
    trees.append(T([1,2])([23,35])(random_tree()))
    trees.append(T([1,2])([25,39])(random_tree()))
    trees.append(T([1,2])([23,43])(random_tree()))
    trees.append(T([1,2])([25,47])(random_tree()))
    trees.append(T([1,2])([23,49])(random_tree()))
    trees.append(T([1,2])([23,51])(random_tree()))
    trees.append(T([1,2])([25,55])(random_tree()))
    trees.append(T([1,2])([23,57])(random_tree()))
    trees.append(T([1,2])([25,59])(random_tree()))
    trees.append(T([1,2])([25,65])(random_tree()))
    trees.append(T([1,2])([23,67])(random_tree()))
    trees.append(T([1,2])([23,70])(random_tree()))
    trees.append(T([1,2])([25,74])(random_tree()))
    trees.append(T([1,2])([25,76])(random_tree()))
    trees.append(T([1,2])([25,79])(random_tree()))
    trees.append(T([1,2])([23,82])(random_tree()))
    trees.append(T([1,2])([23,85])(random_tree()))
    
    trees.append(T([1,2])([20,62])(random_tree()))
    trees.append(T([1,2])([18,63])(random_tree()))
    trees.append(T([1,2])([16,62])(random_tree()))
    trees.append(T([1,2])([14,62])(random_tree()))
    trees.append(T([1,2])([11,60])(random_tree()))

    trees.append(T([1,2])([19,39])(random_tree()))
    trees.append(T([1,2])([21,40])(random_tree()))
    trees.append(T([1,2])([19,38])(random_tree()))
    trees.append(T([1,2])([16,38])(random_tree()))
    trees.append(T([1,2])([17,40])(random_tree()))
    


    
    trees.append(T([1,2])([0,87])(random_tree()))
    trees.append(T([1,2])([-1,90])(random_tree()))
    trees.append(T([1,2])([-2,93])(random_tree()))
    trees.append(T([1,2])([2,98])(random_tree()))
    trees.append(T([1,2])([2,96])(random_tree()))

    trees.append(T([1,2])([2,87])(random_tree()))
    trees.append(T([1,2])([-4,90])(random_tree()))
    trees.append(T([1,2])([-5,93])(random_tree()))
    trees.append(T([1,2])([2,98])(random_tree()))
    trees.append(T([1,2])([3,96])(random_tree()))
    
    trees.append(T([1,2])([4,87])(random_tree()))
    trees.append(T([1,2])([4,90])(random_tree()))
    trees.append(T([1,2])([5,93])(random_tree()))
    trees.append(T([1,2])([4,98])(random_tree()))
    trees.append(T([1,2])([5,96])(random_tree()))

    trees.append(T([1,2])([6,87])(random_tree()))
    trees.append(T([1,2])([5,90])(random_tree()))
    trees.append(T([1,2])([6,93])(random_tree()))
    trees.append(T([1,2])([7,98])(random_tree()))
    trees.append(T([1,2])([6,96])(random_tree()))

    trees.append(T([1,2])([7,87])(random_tree()))
    trees.append(T([1,2])([8,90])(random_tree()))
    trees.append(T([1,2])([7,93])(random_tree()))
    trees.append(T([1,2])([7,98])(random_tree()))
    trees.append(T([1,2])([8,96])(random_tree()))




    trees.append(T([1,2])([10,91])(random_tree()))
    trees.append(T([1,2])([10,89])(random_tree()))
    trees.append(T([1,2])([10,87])(random_tree()))
    trees.append(T([1,2])([10,84])(random_tree()))
    trees.append(T([1,2])([10,83])(random_tree()))
    
    trees.append(T([1,2])([12,90])(random_tree()))
    trees.append(T([1,2])([12,88])(random_tree()))
    trees.append(T([1,2])([12,85])(random_tree()))
    trees.append(T([1,2])([12,93])(random_tree()))
    trees.append(T([1,2])([12,95])(random_tree()))
    
    trees.append(T([1,2])([14,96])(random_tree()))
    trees.append(T([1,2])([14,89])(random_tree()))
    trees.append(T([1,2])([14,85])(random_tree()))
    trees.append(T([1,2])([14,84])(random_tree()))
    trees.append(T([1,2])([14,91])(random_tree()))
    
    trees.append(T([1,2])([16,91])(random_tree()))
    trees.append(T([1,2])([16,89])(random_tree()))
    trees.append(T([1,2])([16,87])(random_tree()))
    trees.append(T([1,2])([16,84])(random_tree()))
    trees.append(T([1,2])([16,83])(random_tree()))
    
    trees.append(T([1,2])([18,90])(random_tree()))
    trees.append(T([1,2])([18,88])(random_tree()))
    trees.append(T([1,2])([18,85])(random_tree()))
    trees.append(T([1,2])([18,93])(random_tree()))
    trees.append(T([1,2])([18,95])(random_tree()))
    
    trees.append(T([1,2])([21,96])(random_tree()))
    trees.append(T([1,2])([21,89])(random_tree()))
    trees.append(T([1,2])([21,85])(random_tree()))
    trees.append(T([1,2])([21,84])(random_tree()))
    trees.append(T([1,2])([21,91])(random_tree()))
    
    trees.append(T([1,2])([28,91])(random_tree()))
    trees.append(T([1,2])([28,89])(random_tree()))
    trees.append(T([1,2])([28,87])(random_tree()))
    trees.append(T([1,2])([28,84])(random_tree()))
    trees.append(T([1,2])([28,83])(random_tree()))
    
    trees.append(T([1,2])([30,90])(random_tree()))
    trees.append(T([1,2])([30,88])(random_tree()))
    trees.append(T([1,2])([30,85])(random_tree()))
    trees.append(T([1,2])([30,93])(random_tree()))
    trees.append(T([1,2])([30,95])(random_tree()))
    
    trees.append(T([1,2])([25,96])(random_tree()))
    trees.append(T([1,2])([25,89])(random_tree()))
    trees.append(T([1,2])([25,85])(random_tree()))
    trees.append(T([1,2])([25,84])(random_tree()))
    trees.append(T([1,2])([25,91])(random_tree()))
    
    speech = []
    speech.append(T([1,2])([34,91])(random_tree()))
    speech.append(T([1,2])([34,89])(random_tree()))
    speech.append(T([1,2])([34,87])(random_tree()))
    speech.append(T([1,2])([34,84])(random_tree()))
    speech.append(T([1,2])([34,83])(random_tree()))
    
    speech.append(T([1,2])([32,90])(random_tree()))
    speech.append(T([1,2])([32,88])(random_tree()))
    speech.append(T([1,2])([32,85])(random_tree()))
    speech.append(T([1,2])([32,93])(random_tree()))
    speech.append(T([1,2])([32,95])(random_tree()))
    
    speech.append(T([1,2])([37,96])(random_tree()))
    speech.append(T([1,2])([37,89])(random_tree()))
    speech.append(T([1,2])([37,85])(random_tree()))
    speech.append(T([1,2])([37,84])(random_tree()))
    speech.append(T([1,2])([37,91])(random_tree()))
    
    speech.append(T([1,2])([41,91])(random_tree()))
    speech.append(T([1,2])([41,89])(random_tree()))
    speech.append(T([1,2])([41,87])(random_tree()))
    speech.append(T([1,2])([41,84])(random_tree()))
    speech.append(T([1,2])([41,83])(random_tree()))
    
    speech.append(T([1,2])([44,90])(random_tree()))
    speech.append(T([1,2])([44,88])(random_tree()))
    speech.append(T([1,2])([44,85])(random_tree()))
    speech.append(T([1,2])([44,93])(random_tree()))
    speech.append(T([1,2])([44,95])(random_tree()))
    
    speech.append(T([1,2])([37,96])(random_tree()))
    speech.append(T([1,2])([37,89])(random_tree()))
    speech.append(T([1,2])([37,85])(random_tree()))
    speech.append(T([1,2])([37,84])(random_tree()))
    speech.append(T([1,2])([37,91])(random_tree()))

    speech.append(T([1,2])([46,91])(random_tree()))
    speech.append(T([1,2])([46,89])(random_tree()))
    speech.append(T([1,2])([46,87])(random_tree()))
    speech.append(T([1,2])([46,84])(random_tree()))
    speech.append(T([1,2])([46,83])(random_tree()))
    
    speech.append(T([1,2])([48,90])(random_tree()))
    speech.append(T([1,2])([48,88])(random_tree()))
    speech.append(T([1,2])([48,85])(random_tree()))
    speech.append(T([1,2])([48,93])(random_tree()))
    speech.append(T([1,2])([48,95])(random_tree()))
    
    speech.append(T([1,2])([50,96])(random_tree()))
    speech.append(T([1,2])([50,89])(random_tree()))
    speech.append(T([1,2])([50,85])(random_tree()))
    speech.append(T([1,2])([50,84])(random_tree()))
    speech.append(T([1,2])([50,91])(random_tree()))

    speech.append(T([1,2])([53,91])(random_tree()))
    speech.append(T([1,2])([53,89])(random_tree()))
    speech.append(T([1,2])([53,87])(random_tree()))
    speech.append(T([1,2])([53,84])(random_tree()))
    speech.append(T([1,2])([53,83])(random_tree()))
    
    speech.append(T([1,2])([55,90])(random_tree()))
    speech.append(T([1,2])([55,88])(random_tree()))
    speech.append(T([1,2])([55,85])(random_tree()))
    speech.append(T([1,2])([55,93])(random_tree()))
    speech.append(T([1,2])([55,95])(random_tree()))
    
    speech.append(T([1,2])([58,96])(random_tree()))
    speech.append(T([1,2])([58,89])(random_tree()))
    speech.append(T([1,2])([58,85])(random_tree()))
    speech.append(T([1,2])([58,84])(random_tree()))
    speech.append(T([1,2])([58,91])(random_tree()))

    speech.append(T([1,2])([61,91])(random_tree()))
    speech.append(T([1,2])([61,89])(random_tree()))
    speech.append(T([1,2])([61,87])(random_tree()))
    speech.append(T([1,2])([61,84])(random_tree()))
    speech.append(T([1,2])([61,83])(random_tree()))
    
    speech.append(T([1,2])([63,90])(random_tree()))
    speech.append(T([1,2])([63,88])(random_tree()))
    speech.append(T([1,2])([63,85])(random_tree()))
    speech.append(T([1,2])([63,93])(random_tree()))
    speech.append(T([1,2])([63,95])(random_tree()))
    
    speech.append(T([1,2])([65,96])(random_tree()))
    speech.append(T([1,2])([65,89])(random_tree()))
    speech.append(T([1,2])([65,85])(random_tree()))
    speech.append(T([1,2])([65,84])(random_tree()))
    speech.append(T([1,2])([65,91])(random_tree()))
    
    trees.append(STRUCT(speech))
    trees.append(T(1)(35)(STRUCT(speech)))
    trees.append(T([1,2])([35,-20])(STRUCT(speech)))
    trees.append(T([1,2])([20,-20])(STRUCT(speech)))
    trees.append(T([1,2])([40,-80])(STRUCT(speech)))
    trees.append(T([1,2])([40,-65])(STRUCT(speech)))
    
    trees.append(T([1,2])([22,-83])(STRUCT(speech)))
    
    trees.append(T([1,2])([48,35])(random_tree()))
    trees.append(T([1,2])([49,38])(random_tree()))
    trees.append(T([1,2])([44,30])(random_tree()))
    trees.append(T([1,2])([45,32])(random_tree()))
    trees.append(T([1,2])([45,34])(random_tree()))
    trees.append(T([1,2])([44,37])(random_tree()))
    
    trees.append(T([1,2])([46,35])(random_tree()))
    trees.append(T([1,2])([47,39])(random_tree()))
    trees.append(T([1,2])([46,42])(random_tree()))
    trees.append(T([1,2])([48,43])(random_tree()))
    trees.append(T([1,2])([45,27])(random_tree()))
    trees.append(T([1,2])([48,25])(random_tree()))
    
    trees.append(T([1,2])([50,35])(random_tree()))
    trees.append(T([1,2])([52,38])(random_tree()))
    trees.append(T([1,2])([51,30])(random_tree()))
    trees.append(T([1,2])([53,32])(random_tree()))
    trees.append(T([1,2])([54,34])(random_tree()))
    trees.append(T([1,2])([55,37])(random_tree()))
    
    trees.append(T([1,2])([53,35])(random_tree()))
    trees.append(T([1,2])([55,39])(random_tree()))
    trees.append(T([1,2])([57,42])(random_tree()))
    trees.append(T([1,2])([56,43])(random_tree()))
    trees.append(T([1,2])([58,27])(random_tree()))
    trees.append(T([1,2])([59,25])(random_tree()))
    
    trees.append(T([1,2])([65,44])(random_tree()))
    trees.append(T([1,2])([64,42])(random_tree()))
    trees.append(T([1,2])([63,49])(random_tree()))
    trees.append(T([1,2])([61,44])(random_tree()))
    trees.append(T([1,2])([62,46])(random_tree()))
    trees.append(T([1,2])([64,48])(random_tree()))
    """


    plane = TEXTURE("images/legno.jpg")(CUBOID([160,140,2]))
    street = MATERIAL([0.0, 0.0, 0.0, 1.0,0.454902, 0.454902, 0.454902, 1.0,0.0225, 0.0225, 0.0225, 1.0,0.0, 0.0, 0.0, 1.0,12.8])(T([1,2,3])([30,20,2.2])(STRUCT(street)))
    trees = T([1,2,3])([30,20,2.2])(STRUCT(trees))
    house = T([1,2,3])([30,20,2.2])(STRUCT(house))
    meadow = T([1,2,3])([20,20,2])(TEXTURE("images/prato.jpg")(CUBOID([120,100,0.2])))
    
    model = STRUCT([street,plane,meadow,house,trees])
    
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

