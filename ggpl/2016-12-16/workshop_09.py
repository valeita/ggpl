from pyplasm import *
from larlib import *
from math import *

def ggpl_geometric_building_roof(segment_list):
    """
    this function takes in input a list of segment charaterized of two points, of this type: [[x,y,z],[x,y,z]]
    the segmend, must be the same orientation, and every side must be long 3 minimum meters.
    it returns the hpc of the completed structure.
    """
    points = []
    i=0
    alfa = search_alfa(segment_list)
    quote = 2.
    list_segment_angle = check_segment(segment_list)
    check_input(segment_list)
    
    while(i<len(segment_list)-1):
    
        points.append(generate_internal_points(segment_list[i],segment_list[i+1], list_segment_angle[i],alfa,quote))

        i=i+1

    points.append(generate_internal_points(segment_list[i],segment_list[0], list_segment_angle[i],alfa,quote))

    planes = generate_planes(segment_list,points)
    terrace = generate_terrace(points,list_segment_angle)

    structure = STRUCT([planes,terrace])
    VIEW(structure)
    search_alfa(segment_list)
    return structure




def search_alfa(segment_list):
    """
    this function takes in input a list of segment charaterized of two points, of this type: [[x,y,z],[x,y,z]]
    it returns the constant alfa, usefull to generate internal points of the roof.
    """
    i=0
    j=0
    list = []
    point = []

    while(i<len(segment_list)):

        j=0
        while(j<2):
            list.append(segment_list[i][j])
            j=j+1
        i=i+1

    i=1
    while(i<len(list)):
        
        point.append(list[i])
        i=i+2

    i=1
    min = search_minimal_distance(point[0],0,point)

    while(i<len(point)):
        
        distance = search_minimal_distance(point[i],i,point)
        
        if(distance<min):

            min = distance
        i=i+1

    return (min/3)



def search_minimal_distance(point,index,list):
    """
    This function takes as input a point, the one from which the search,
    an index that corresponds to its location within the main list, and the list itself.
    it returns the minimum distance.
    """
    min = 100000
    i=0
    
    while(i<len(list)):

        if(i!=index):

            distance = sqrt((list[i][1]-point[1])**2 + (list[i][0]-point[0])**2)
            if(distance<min):

                min = distance
        i = i+1
        
    return min



def generate_terrace(internal_points,list_segment_angle):
    """
    This method takes as input a list of points inside the roof,
    and the angles formed by the sides of the segments.
    it returns the hpc of the terrace.
    """
    i=0
    list = []
    terrace = []
    while(i<len(internal_points)):

        list.append(search_nearest_point(internal_points[i],i,internal_points))
            
        i=i+1
    i=1
    while(i<len(list)):

        terrace.append(TEXTURE("texture/terrazza.jpg")(OFFSET([0.2,0.2,0.13])(MKPOL([ [ list[i][0],list[i][1],list[i-1][0],list[i-1][1]],[[1,2,3,4]],[1]]))))
        i=i+1
    terrace.append(TEXTURE("texture/terrazza.jpg")(OFFSET([0.2,0.2,0.013])(MKPOL([[list[0][0],list[0][1],list[len(list)-1][0],list[len(list)-1][1]],[[1,2,3,4]],[1]]))))
    
    return STRUCT(terrace)


def search_nearest_point(point,index,internal_points):
    """
    This function takes as input a point, the one from which the search,
    an index that corresponds to its location within the main list, and the list itself.
    it returns the segment with the point analyzed, and the nearest point.
    """
    min = 10000
    i=0
    
    while(i<len(internal_points)):

        if(i!=index):

            distance = sqrt((internal_points[i][1]-point[1])**2 + (internal_points[i][0]-point[0])**2)

            if(distance<min):

                min = distance
                segment = [point,internal_points[i]]
        i = i+1
    return segment


    

def generate_planes(segment_list, internal_points_list):
    """
    This function takes as input a list of segments / sides of the roof,
    and its interior points calculated by a previous method.
    it returns all planes of the roof.
    """
    i=1
    list = []

    while(i<len(segment_list)):
        
        list.append(TEXTURE("texture/tetto.jpg")(OFFSET([0.1,0.1,0.1])(MKPOL([[segment_list[i][0],segment_list[i][1],internal_points_list[i-1],internal_points_list[i] ],[[1,2,3,4]],[1]]))))

        i=i+1

    list.append(TEXTURE("texture/tetto.jpg")(OFFSET([0.1,0.1,0.1])(MKPOL([[segment_list[0][0],segment_list[0][1],internal_points_list[0],internal_points_list[len(internal_points_list)-1] ],[[1,2,3,4]],[1]]))))
    
    return STRUCT(list)


def generate_internal_points(segment_first, segment_last, angle, alfa,quote):
    """
    This function takes as input:
    -one business segment that will be analyzed.
    -another segment, the next of the previous segment.
    -an angle, the one between the two segments.
    -a quota, set by us.
    it returns the internal points of the roof.
    """
    next = segment_last[1]
    central = segment_first[1]
    previous = segment_first[0]
    i=0
    
    x_prev = previous[0]-central[0]
    y_prev = previous[1]-central[1]

    x_next = next[0]-central[0]
    y_next = next[1]-central[1]
    
    first_angle = atan2(y_prev,x_prev)
    
    hpc_prev = MKPOL([[[x_prev,y_prev,0]],[[1]],[1]])
    hpc_next = MKPOL([[[x_next,y_next,0]],[[1]],[1]])
    
    hpc_prev=ROTATE([1,2])(-first_angle)(hpc_prev)
    hpc_next=ROTATE([1,2])(-first_angle)(hpc_next)

    u_prev = normalize_values(UKPOL(hpc_prev))
    u_next = normalize_values(UKPOL(hpc_next))

    if(angle < 180):

        cont = (angle-90)/10.
        
        if(u_next[1]>u_prev[1]):

            point = [alfa+(cont*(1/9)),alfa,0]
            
        elif(u_next[1]<u_prev[1]):

            point = [alfa-(cont*(1/9)),-alfa,0]
    
        hpc_point = MKPOL([[[point[0],point[1],0]],[[1]],[1]])
        hpc_point = ROTATE([1,2])(first_angle)(hpc_point)
        hpc_point = normalize_values(UKPOL(hpc_point))
        return [hpc_point[0]+central[0],hpc_point[1]+central[1],quote]
         
    if(angle>180):

        cont = (angle-270)/10.
        
        if(u_next[1]>u_prev[1]):

            point = [alfa+(cont*(1/9)),alfa,0]
            
        elif(u_next[1]<u_prev[1]):

            point = [alfa-(cont*(1/9)),-alfa,0]
    
        hpc_point = MKPOL([[[point[0],point[1],0]],[[1]],[1]])
        hpc_point = ROTATE([1,2])(first_angle+radians(180))(hpc_point)
        hpc_point = normalize_values(UKPOL(hpc_point))
        return [hpc_point[0]+central[0],hpc_point[1]+central[1],quote]
            
        



    
def check_segment(segment_list):

    """
    this function takes in input a list of segment charaterized of two points, of this type: [[x,y,z],[x,y,z]]
    it returns the angles of all roof's edge
    """
    i=0
    list = []
    
    while(i<len(segment_list)-1):

        previous = segment_list[i][0]
        central = segment_list[i][1]
        next = segment_list[i+1][1]

        angle = check_angle(previous,central,next)
        list.append(angle)
        
        i = i+1

    if(i == len(segment_list)-1):

        previous = segment_list[i][0]
        central = segment_list[i][1]
        next = segment_list[0][1]

        angle = check_angle(previous,central,next)     
        list.append(angle)
       
    return list


def check_angle(previous,central,next):

    """
    This function takes as input 3 points, according to a predefined orientation.
    the point have this form [x,y,z]
    return the angle between the three points.
    """
    x_prev = previous[0]-central[0]
    y_prev = previous[1]-central[1]

    x_next = next[0]-central[0]
    y_next = next[1]-central[1]
    
    first_angle = atan2(y_prev,x_prev)
    
    hpc_prev = MKPOL([[[x_prev,y_prev,0]],[[1]],[1]])
    hpc_next = MKPOL([[[x_next,y_next,0]],[[1]],[1]])
    
    hpc_prev=ROTATE([1,2])(-first_angle)(hpc_prev)
    hpc_next=ROTATE([1,2])(-first_angle)(hpc_next)

    u_prev = normalize_values(UKPOL(hpc_prev))
    u_next = normalize_values(UKPOL(hpc_next))

    if (degrees(atan2(u_next[1],u_next[0])) < 0):

        return 360 + degrees(atan2(u_next[1],u_next[0]))
    else:
        return degrees(atan2(u_next[1],u_next[0]))




def normalize_values(list):
    """
    normalize_values is a function that rounds float in list.
    and return a normalized list.
    """
    point=list[0][0]
    values_normalized = []
    for i in point:
        
        if (abs(i)<0.001):

            values_normalized.append(0)
        else:
            values_normalized.append(i)
            
    return values_normalized





def check_input(segment_list):
    """
    this function takes in input a list of segment charaterized of two points, of this type: [[x,y,z],[x,y,z]]
    it verified that the input is acceptable
    """
    for i in segment_list:

        left_point = i[0]
        right_point = i[1]

        distance = sqrt((i[1][1]-i[0][1])**2 + (i[1][0]-i[0][0])**2)

        if(distance <3):

            exit("errore nella creazione di questa sezione di tetto: " + str(i) + "\nogni lato deve essere lungo almeno tre metri per la costruzione di un buon tetto. non rispettare questo vincolo, porta alla creazione di un tetto con un risultato poco apprezzabile")

    
ggpl_geometric_building_roof([[[0,0,0],[0,9,0]],[[0,9,0],[11,9,0]],[[11,9,0],[11,6,0]],[[11,6,0],[3,6,0]],[[3,6,0],[3,3,0]],[[3,3,0],[8,3,0]],[[8,3,0],[8,0,0]],[[8,0,0],[0,0,0]]])
ggpl_geometric_building_roof([[[4,5,0],[2,8,0]],[[2,8,0],[11,8,0]],[[11,8,0],[9,11,0]],[[9,11,0],[20,8,0]],[[20,8,0],[20,3,0]],[[20,3,0],[14,1,0]],[[14,1,0],[11,5,0]],[[11,5,0],[4,5,0]]])









        
