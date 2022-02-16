import numpy as np
import cv2

#read images in colour
#returns numpy 3-dimensional array (matrix)
def readColourImage(file):
    return cv2.imread(file, cv2.IMREAD_COLOR)

#read image in greyscale
def readBWImage(file):
    return cv2.imread(file, cv2.IMREAD_GRAYSCALE)

#display image and title
def displayImage(title,img):
    print("Press 0 to close window")
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#extract BGR components
#returns unpacked var as blue, green, red
#usage: (b,g,r) = extractBGRComponents(img)
def extractBGRComponents(img):
    return cv2.split(img)

#merge individual BGR components
def mergeBGRComponents(b,g,r):
    return cv2.merge((b,g,r))

#convert RGB to Y'UV
def rgb2YUV(r,g,b):
    #typecast to unsigned int
    y = np.array(0.299*r+0.587*g+0.114*b, np.uint8)
    u = np.array(b-y, np.uint8)
    v = np.array(r-y, np.uint8)
    return (y,u,v)

#convert Y'UV to Y'PbPr
def yuv2YPbPr(y,u,v):
    pb = np.array((0.5/(1-0.114))*u, np.uint8)
    pr = np.array((0.5/(1-0.299))*v, np.uint8)
    return (y,pb,pr)

#convert Y'PbPr to Y'CbCr
def ypbpr2YCbCr(y,pb,pr):
    y = 16+219*y
    cb = 128+224*pb
    cr = 128+224*pr
    return (y,cb,cr)

#gamma correction
def gammaCorrection(y,gamma):
    return np.array(y**gamma,np.float)

file = "lena512color.tiff"
img = readColourImage(file)
(b,g,r) = extractBGRComponents(img)
(y,u,v) = rgb2YUV(r,g,b)
vout = gammaCorrection(y,2)
print(vout)
displayImage("gamma correction",vout)