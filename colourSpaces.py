import numpy as np
import cv2

#class to handle anything related to acquiring and displaying image
class Image:
    #overriding constructor
    #iscolour represents if image is colour (1) or black white (0)
    def __init__(self,file,isColour=1):
        self.file = file
        self.img = cv2.imread(self.file, isColour) # matrix of vals

    #display image and title
    def displayImage(self,title,img):
        print("Press 0 to close window")
        cv2.imshow(title,img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#class to handle colour space transformations
class ColourSpaces:
    #extract BGR components
    #returns unpacked var as blue, green, red
    #usage: (b,g,r) = extractBGRComponents(img)
    def extractBGRComponents(self,img):
        return cv2.split(img)

    #merge individual BGR components
    def mergeBGRComponents(self,b,g,r):
        return cv2.merge((b,g,r))

    #convert RGB to Y'UV
    def rgb2YUV(self,r,g,b):
        #typecast to unsigned int
        y = np.array(0.299*r+0.587*g+0.114*b, np.uint8)
        u = np.array(b-y, np.uint8)
        v = np.array(r-y, np.uint8)
        return (y,u,v)

    #convert Y'UV to Y'PbPr
    def yuv2YPbPr(self,y,u,v):
        pb = np.array((0.5/(1-0.114))*u, np.uint8)
        pr = np.array((0.5/(1-0.299))*v, np.uint8)
        return (y,pb,pr)

    #convert Y'PbPr to Y'CbCr
    def ypbpr2YCbCr(self,y,pb,pr):
        y = 16+219*y
        cb = 128+224*pb
        cr = 128+224*pr
        return (y,cb,cr)

    #gamma correction
    def gammaCorrection(self,img,gamma):
        img = img.astype("double") #typecast to not lose precision
        imgPrime = np.clip(255 * ((img/255) ** 1/gamma),0,255) #prevent overflow
        return imgPrime.astype("uint8") #typecast back so can be displayed


# lena = Image("lena512color.tiff",1)
# test = ColourSpaces()
# (b,g,r) = test.extractBGRComponents(lena.img)
# (y,u,v) = test.rgb2YUV(r,g,b)
# vout = test.gammaCorrection(lena.img,5)
# lena.displayImage("gamma correction",vout)