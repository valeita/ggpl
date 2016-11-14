from pyplasm import *
from larlib import *

def ggpl_my_furniture(dx,dy,dz):
    """
    the following function takes as input 3 parameters, the x, y, and z of the
    space available.Processes information, and invoking the underlying methods,
    builds the room by placing the right components.
    """
    if (check_input == 0): return
    
    room = OFFSET([0.01,0.01,0.01])(SKEL_1(CUBOID([dx,dy,dz])))
    door = OFFSET([0.01,0.01,0.01])(create_door(dx,dy,dz))
    
    cabinet = COLOR(BROWN)(create_cabinet(dx,dy,dz))
    lockers = COLOR(BROWN)(create_lockers(dx,dy,dz))
    cart = COLOR(BROWN)(create_cart(dx,dy,dz))
    cot = COLOR(BROWN)(create_cot(dx,dy,dz))
    
    VIEW(STRUCT([room,cabinet,lockers,door,cart,cot]))
    
    return STRUCT([room,cabinet,lockers,door,cart,cot])



def check_input(dx,dy,dz):
    """
    the following function takes as input 3 parameters, the x, y, and z of the
    space available. performs a check on the size.
    """
    finish = 1
    
    if(dx>2 or dx<1):
        print("lenght size not valid."
              + "ideal size between one meter and two meters\n")
        finish = 0

    if(dy>3 or dy<2):
        print("width size not valid."
              + "ideal size between two meters and three meters\n")
        finish = 0

    if(dz>4 or dz<3):
        print("quote size not valid."
              + "ideal size between two meters and three meters\n")
        finish = 0

    return finish



def create_cabinet(dx,dy,dz):
    """
    the following function takes as input 3 parameters, the x, y, and z of the
    space available. creates cabinet inside the room.
    """
    list = []
    h_tot = (dz/7.0)*2.0
    lun_shelf = dx/7.0
    larg_shelf = dy
    h_shelf = h_tot/10.0
    
    h_cabinet = (h_tot/10.0)*9.0
    larg_cabinet = dy
    lun_cabinet = dx/10.0

    init_dx_1 = dx-lun_cabinet
    init_dx_2 = dx-lun_shelf

    list.append(T(1)(init_dx_1)(SKEL_1(CUBOID([lun_cabinet,larg_cabinet,h_cabinet]))))
    list.append(T(1)(init_dx_1)(CUBOID([lun_cabinet,larg_cabinet,h_cabinet])))
    
    list.append(T([1,3])([init_dx_2,h_cabinet])(SKEL_1(CUBOID([lun_shelf,larg_shelf,h_shelf]))))
    list.append(T([1,3])([init_dx_2,h_cabinet])(CUBOID([lun_shelf,larg_shelf,h_shelf])))

    return STRUCT(list)



    
def create_lockers(dx,dy,dz):
    """
    the following function takes as input 3 parameters, the x, y, and z of the.
    space available. creates the lockers.
    """
    larg_lockers = dy/3.0
    h_lockers = dz/3.0
    lun_lockers = dx/10.0
    
    larg2_locker = (larg_lockers/7.0)*2.0
    larg_plane = (larg_lockers/7.0)*3.0
    h_plane = h_lockers/30.0
    h_locker = h_lockers-(2.0*(h_plane))
    list = []

    list.append(SKEL_1(CUBOID([lun_lockers,larg_lockers,h_plane])))
    list.append(CUBOID([lun_lockers,larg_lockers,h_plane]))
    
    list.append(T(3)(h_lockers-h_plane)(SKEL_1(CUBOID([lun_lockers,larg_lockers,h_plane]))))
    list.append(T(3)(h_lockers-h_plane)(CUBOID([lun_lockers,larg_lockers,h_plane])))
    
    list.append(T(3)(h_plane)(SKEL_1(CUBOID([lun_lockers,larg2_locker,h_locker]))))
    list.append(T(3)(h_plane)(CUBOID([lun_lockers,larg2_locker,h_locker])))
    
    list.append(T([2,3])([larg_lockers-larg2_locker,h_plane])(SKEL_1(CUBOID([lun_lockers,larg2_locker,h_locker]))))
    list.append(T([2,3])([larg_lockers-larg2_locker,h_plane])(CUBOID([lun_lockers,larg2_locker,h_locker])))

    list.append(T([1,2,3])([-(larg2_locker/25.0),larg_lockers-(larg2_locker)+(3*h_plane),3*h_plane])(CUBOID([larg2_locker/10.0,larg2_locker/10.0,larg2_locker/10.0])))
    list.append(T([1,2,3])([-(larg2_locker/25.0),larg_lockers-(larg2_locker)+(3*h_plane),3*h_plane])(SKEL_1(CUBOID([larg2_locker/10.0,larg2_locker/10.0,larg2_locker/10.0]))))
#
    list.append(T([1,2,3])([-(larg2_locker/25.0),larg_lockers-(larg2_locker)+(3*h_plane),3*h_plane])(CUBOID([larg2_locker/10.0,larg2_locker/10.0,larg2_locker/10.0])))
    list.append(T([1,2,3])([-(larg2_locker/25.0),(larg2_locker)-(3*h_plane),3*h_plane])(SKEL_1(CUBOID([larg2_locker/10.0,larg2_locker/10.0,larg2_locker/10.0]))))
#
    list.append(T([2,3])([larg2_locker,h_locker/3.0])(SKEL_1(CUBOID([lun_lockers,larg_plane,h_plane]))))
    list.append(T([2,3])([larg2_locker,h_locker/3.0])(CUBOID([lun_lockers,larg_plane,h_plane])))
    
    list.append(T([2,3])([larg2_locker,(h_locker/3.0)*2])(SKEL_1(CUBOID([lun_lockers,larg_plane,h_plane]))))
    list.append(T([2,3])([larg2_locker,(h_locker/3.0)*2])(CUBOID([lun_lockers,larg_plane,h_plane])))
    
    structure = (STRUCT(list))

    list_s = []
    list_s.append(T([1,2,3])([dx-lun_lockers,dy/3.0,(dz/10.0)*5.0])(structure))
    
    return STRUCT(list_s)


    
def create_door(dx,dy,dz):

    """
    the following function takes as input 3 parameters, the x, y, and z of the
    space available. creates a port.
    """
    larg_door = dy/5.0
    h_door = dz/2.0
    list = []
    list.append(T(2)((dy/5)*3))
    list.append(SKEL_1(CUBOID([0,larg_door,h_door])))
    list.append(SKEL_1(T([2,3])([(larg_door/5),h_door/2])(CUBOID([0,larg_door/10.0,larg_door/10.0]))))
    
    return STRUCT(list)



def create_cart(dx,dy,dz):
    """
    the following function takes as input 3 parameters, the x, y, and z of the
    space available. It creates a cart.
    """
    larg_cart = dy/6.0
    lun_cart = (dx/7.0)*2.0
    h_cart = dz/3.0
    h_cart_reduced = (h_cart/10.0)*8.0
    h_leg = h_cart/5.0
    
    list = []
    
    list.append(T(3)(h_leg)(CUBOID([lun_cart,larg_cart/30.0,h_cart-h_leg])))
    list.append(T(3)(h_leg)(SKEL_1(CUBOID([lun_cart,larg_cart/30.0,h_cart-h_leg]))))
    
    list.append(T([2,3])([larg_cart/30,h_leg])(CUBOID([lun_cart/30.0,larg_cart-(larg_cart/30.0),h_cart-h_leg])))
    list.append(T([2,3])([larg_cart/30,h_leg])(SKEL_1(CUBOID([lun_cart/30.0,larg_cart-(larg_cart/30.0),h_cart-h_leg]))))
    
    list.append(T([1,2,3])([lun_cart-(lun_cart/30.0),larg_cart/30.0,h_leg])(CUBOID([lun_cart/30.0,larg_cart-(larg_cart/30.0),h_cart-h_leg])))
    list.append(T([1,2,3])([lun_cart-(lun_cart/30.0),larg_cart/30.0,h_leg])(SKEL_1(CUBOID([lun_cart/30.0,larg_cart-(larg_cart/30.0),h_cart-h_leg]))))
    
    list.append(T([1,2,3])([lun_cart/30.0,larg_cart/30.0,h_leg])(CUBOID([lun_cart-(2.0*(lun_cart/30.0)),larg_cart-(larg_cart/30.0),h_cart/30.0])))
    list.append(T([1,2,3])([lun_cart/30.0,larg_cart/30.0,h_leg])(SKEL_1(CUBOID([lun_cart-(2*(lun_cart/30.0)),larg_cart-(larg_cart/30.0),h_cart/30.0]))))

    list.append(T([1,2,3])([lun_cart/30.0,larg_cart/30.0,h_leg+(h_cart_reduced/3)])(CUBOID([lun_cart-(2.0*(lun_cart/30.0)),larg_cart-(larg_cart/30.0),h_cart/30.0])))
    list.append(T([1,2,3])([lun_cart/30.0,larg_cart/30.0,h_leg+(h_cart_reduced/3)])(SKEL_1(CUBOID([lun_cart-(2*(lun_cart/30.0)),larg_cart-(larg_cart/30.0),h_cart/30.0]))))

    list.append(T([1,2,3])([lun_cart/30.0,larg_cart/30.0,h_leg+((h_cart_reduced/3)*2)])(CUBOID([lun_cart-(2.0*(lun_cart/30.0)),larg_cart-(larg_cart/30.0),h_cart/30.0])))
    list.append(T([1,2,3])([lun_cart/30.0,larg_cart/30.0,h_leg+((h_cart_reduced/3)*2)])(SKEL_1(CUBOID([lun_cart-(2*(lun_cart/30.0)),larg_cart-(larg_cart/30.0),h_cart/30.0]))))

    list.append(CUBOID([lun_cart/6,larg_cart/6,h_leg]))
    list.append(SKEL_1(CUBOID([lun_cart/6,larg_cart/6,h_leg])))
    
    list.append(T(1)(lun_cart-(lun_cart/6))(CUBOID([lun_cart/6,larg_cart/6,h_leg])))
    list.append(T(1)(lun_cart-(lun_cart/6))(SKEL_1(CUBOID([lun_cart/6,larg_cart/6,h_leg]))))
    
    list.append(T(2)(larg_cart-(larg_cart/6))(CUBOID([lun_cart/6,larg_cart/6,h_leg])))
    list.append(T(2)(larg_cart-(larg_cart/6))(SKEL_1(CUBOID([lun_cart/6,larg_cart/6,h_leg]))))

    list.append(T([1,2])([lun_cart-(lun_cart/6),larg_cart-(larg_cart/6)])(CUBOID([lun_cart/6,larg_cart/6,h_leg])))
    list.append(T([1,2])([lun_cart-(lun_cart/6),larg_cart-(larg_cart/6)])(SKEL_1(CUBOID([lun_cart/6,larg_cart/6,h_leg]))))

    structure = STRUCT(list)
    structure = S(2)(-1)(structure)
    list2 = []
    list2.append(T([1,2])([dx/2.0-lun_cart/2.0,dy])(structure))
    
    return STRUCT(list2)
    


def create_cot(dx,dy,dz):
    """
    the following function takes as input 3 parameters, the x, y, and z of the
    space available. It creates a cot
    """
    lun_cot = (dx/7.0)+ (dx/14)*3
    larg_cot = dy-(dy/5.0 + dy/10.0)
    h_cot = dz/3.0

    h_reduced = h_cot/2.0
    
    list = []

    list.append(T(3)(h_reduced)(CUBOID([lun_cot,(larg_cot/3)*2,h_reduced/5.0])))
    list.append(T(3)(h_reduced)(SKEL_1(CUBOID([lun_cot,(larg_cot/3)*2,h_reduced/5.0]))))
    
    list.append(CUBOID([lun_cot/6.0,lun_cot/6.0,h_cot/2.0]))
    list.append(SKEL_1(CUBOID([lun_cot/6.0,lun_cot/6.0,h_cot/2.0])))
    
    list.append(T(1)(lun_cot-(lun_cot/6.0))(CUBOID([lun_cot/6.0,lun_cot/6.0,h_cot/2.0])))
    list.append(T(1)(lun_cot-(lun_cot/6.0))(SKEL_1(CUBOID([lun_cot/6.0,lun_cot/6.0,h_cot/2.0]))))
    
    list.append(T([1,2])([lun_cot-(lun_cot/6.0),(larg_cot/3.0)*2.0-lun_cot/6.0])(CUBOID([lun_cot/6.0,lun_cot/6.0,h_cot/2.0])))
    list.append(T([1,2])([lun_cot-(lun_cot/6.0),(larg_cot/3.0)*2.0-lun_cot/6.0])(SKEL_1(CUBOID([lun_cot/6.0,lun_cot/6.0,h_cot/2.0]))))
    
    list.append(T(2)((larg_cot/3.0)*2-lun_cot/6.0)(CUBOID([lun_cot/6.0,lun_cot/6.0,h_cot/2.0])))
    list.append(T(2)((larg_cot/3.0)*2-lun_cot/6.0)(SKEL_1(CUBOID([lun_cot/6.0,lun_cot/6.0,h_cot/2.0]))))

    list.append(T([1,3])([lun_cot/6.0,h_reduced/2.0])(CUBOID([lun_cot-(2*(lun_cot/6.0)),(larg_cot/3.0)*2.0-(lun_cot/6.0),h_reduced/10.0])))
    list.append(T([1,3])([lun_cot/6.0,h_reduced/2.0])(SKEL_1(CUBOID([lun_cot-(2*(lun_cot/6.0)),(larg_cot/3.0)*2.0-(lun_cot/6.0),h_reduced/10.0]))))
    coord = []
    coord.append([0,(larg_cot/3)*2,(h_cot/2.0)+h_reduced/5])
    coord.append([lun_cot,(larg_cot/3)*2,h_cot/2.0+(h_reduced/5.0)])
    coord.append([lun_cot,(larg_cot/3)*2,h_cot/2.0])
    coord.append([0,(larg_cot/3)*2,h_cot/2.0])
    coord.append([0,((larg_cot/3)*2)+(larg_cot/3.0),h_cot/2.0+((h_reduced/5.0)*4)])
    coord.append([0,((larg_cot/3)*2)+(larg_cot/3.0),(h_cot/2.0)+(h_reduced/5)+(h_reduced/5.0)*4])
    coord.append([lun_cot,((larg_cot/3)*2)+(larg_cot/3.0),h_cot/2.0+(h_reduced/5.0)*4])
    coord.append([lun_cot,((larg_cot/3)*2)+(larg_cot/3.0),h_cot/2.0+(h_reduced/5.0)+(h_reduced/5.0)*4])
    
    plane = SKEL_2(MKPOL([coord,[[1,2,3,4,5,6,7,8]],[[1]]]))
    list.append(plane)
    structure = S(2)(-1)(STRUCT(list))
    structure = T([1,2])([dx/2-(lun_cot/2),larg_cot+dy/20])(structure)
    
    return structure



ggpl_my_furniture(1.5,2.5,2.0)


    





