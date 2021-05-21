
import numpy as np

# under CIE color space,transformation matrix from RGB tristimulus value
# to XYZ tristimulus value
sRGB_RGB2XYZ = np.array([[0.4124, 0.3576, 0.1805],
                         [0.2126, 0.7152, 0.0722],
                         [0.0193, 0.1192, 0.9505]])

def XYZ2Lab(XYZ):
    XYZ[0] = float(XYZ[0]) / 95.047  # ref_X =  95.047   Observer= 2°, Illuminant= D65
    XYZ[1] = float(XYZ[1]) / 100.0  # ref_Y = 100.000
    XYZ[2] = float(XYZ[2]) / 108.883  # ref_Z = 108.883

    num = 0
    for value in XYZ:
        if value > 0.008856:
            value = value ** (0.3333333333333333)
        else:
            value = (7.787 * value) + (16 / 116)
        XYZ[num] = value
        num = num + 1

    L = (116 * XYZ[1]) - 16
    a = 500 * (XYZ[0] - XYZ[1])
    b = 200 * (XYZ[1] - XYZ[2])

    Lab = np.round([L, a, b], decimals=4)

    return Lab

# calculate CIE1931 XYZ from RGB pixel value
def sRGB_rgb2xyz(inputColor,matrix):
   num = 0
   RGB = np.zeros([3,1])

   for value in inputColor :
       value = float(value) / 255
       if value > 0.04045 :
           value = ( ( value + 0.055 ) / 1.055 ) ** 2.4 # gamma decode
       else :
           value = value / 12.92
       RGB[num,0] = value * 1005
       num = num + 1
   XYZ=np.round(np.matmul(matrix,RGB),decimals=4)

   return XYZ

if __name__=="__main__":
    r=[255,255,255]
    XYZ=sRGB_rgb2xyz(r,sRGB_RGB2XYZ)
    print(XYZ)