from pyplasm import *
from workshop01 import *
import csv

def ggpl_bone_structure(file_name):

    totalFrameList=[]
    paramFrame=[]
    file = open(file_name,'r')
    spamreader = csv.reader(file)
    frame = []
    traslx = []
    
    for row in spamreader:

        dimPillar = []
        dimBeam = []
        hPillars = []
        widthsBeams = []
        i=0
        j=0
        l1=0
        l2=0
        
        if(len(row) == 3):

            traslx.append(int(row[0]))
            
        else:
            
            dimBeam.append(int(row[0]))
            dimBeam.append(int(row[1]))
            dimPillar.append(int(row[2]))
            dimPillar.append(int(row[3]))

            index = 4
            l1=int(row[index])
            while i<int(row[4]):

                index = index + 1
                i=i+1
                hPillars.append(int(row[index]))
                
            index = index+1
            t=index
            l2=int(row[index])
            while j<int(row[t]):

                index = index + 1
                j=j+1
                widthsBeams.append(int(row[index]))
            
            frame.append(gabbia(dimBeam,dimPillar,l1,hPillars,l2,widthsBeams))
            paramFrame.append(dimBeam)
            paramFrame.append(dimPillar)
            paramFrame.append(l1)
            paramFrame.append(hPillars)
            paramFrame.append(l2)
            paramFrame.append(widthsBeams)
            totalFrameList.append(paramFrame)
            
    skeleton = buildStructure(frame,traslx)
    beams = buildStructureBeams(frame, traslx, skeleton,totalFrameList[0][0],totalFrameList[0][1],totalFrameList[0][2],totalFrameList[0][3],totalFrameList[0][4],totalFrameList[0][5])

    building = STRUCT([skeleton,beams])

    VIEW(building)
            
def buildStructure(frame, translations):
     
    skeleton = []
    index=0
    j=0
    for i in frame:

        skeleton.append(T(1)(translations[j]))
        skeleton.append(i)
        j=j+1
        
    return STRUCT(skeleton)


def buildStructureBeams(frame, traslx, skeleton, dimBeam, dimPillar,l1,hPillars,l2,widthsBeams):

    ax=[]
    ay=[]
    az=[]
    i=0
    beams = []

    while i<len(frame)-1:

        
        ax.append(-dimPillar[0])
        var = traslx[i+1]-dimPillar[0]
        ax.append(var)
        i=i+1
        
    for j in hPillars:

         az.append(-j)
         az.append(dimBeam[1])
         
    for k in widthsBeams:

         ay.append(k)
         ay.append(dimPillar[1])

    p1 = QUOTE(ax)
    p2= QUOTE(ay)
    p3 = QUOTE(az)

    d=PROD([p1,p2])
    beams.append(PROD([d,p3]))

    return STRUCT(beams)
    
   




ggpl_bone_structure("frame_data_000000.csv")

    
