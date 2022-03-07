import numpy
from colourSpaces import ColourSpaces, Image

#subsample image
#A:b:c where A-region width,b-samples in row,c-row changes
#Assuming A=4
class Subsampling:
    #initialise subsample technique
    #0-direct,1-ave,2-left,3-right 
    def __init__(self,b,c,technique=0):
        #check technique is valid
        if technique not in [0,1,2,3]:
            print("Invalid technique\nDefaulting to Direct")
            technique = 0

        #check b and c are valid
        valid = [1,2,4]
        if b not in valid:
            print("Invalid b,c combination\nDefaulting to 4:2:0")
            b = 2
            c = 0
        else:
            valid.append(0)
            if (c > b) or (c not in valid):
                print("Invalid b,c combination\nDefaulting to 4:2:0")
                b = 2
                c = 0
        #set vals
        self.technique = technique
        self.A = 4
        self.b = b
        self.c = c
        del valid, technique, b, c # cleanup
    
    #get technique used for subsampling
    def getTechnique(self):
        tech = ["Direct","Average","Left","Right"]
        return tech[self.technique]

    #subsampling method
    def subsample(self,img):
        #setup vars
        A = img.copy()
        rows = A.shape[0]/2
        cols = A.shape[1] * (self.b/4)
        print(rows,cols)
        #step thru rows and cols
        # for row in range(0,rows):
        #     top = 2 * row
        #     bottom = top + 1
        #     for col in range(0,cols):

lena = Image("lena512color.tiff",1)
x = Subsampling(4,2)
x.subsample(lena.img)