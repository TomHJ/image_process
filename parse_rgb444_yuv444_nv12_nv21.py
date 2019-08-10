'''
 this script can not run directly, it need to 
 be modified in local area. Hope helpful for your problem

'''



import os
import re
import cv2
import numpy as np
from skimage.measure import compare_ssim
from shutil import copyfile
import matplotlib.pyplot as plt


def parse_pix_fmts(s):
    output = re.findall(r"_(\d+bit_\S+\d+)_", s)[0]
    return output

def parse_resolution(s):
    output = re.findall(r'(\d+)x(\d+)_', s)[0]
    return int(output[0]),int(output[1])

def yuv2bgr(filename,height,width,bit_depth,format_,output_name):
    path=os.path.dirname(filename)
    base=os.path.basename(filename)
    if bit_depth=="8bits":
        bpp=1; dtype='uint8'
    else:
        bpp=2; dtype='uint16'

    if format_=="nv21":
        cv_format=cv2.COLOR_YUV2BGR_NV21

    if format_ == "nv12":
        cv_format = cv2.COLOR_YUV2BGR_NV12

    with open(filename,'rb') as fp:
        frame_len=height*width*bpp*3//2

        fp.seek(0,2)
        ps=fp.tell()
        numfrm=ps//frame_len

        fp.seek(0,0)
        for i in range(numfrm):
        # for i in range(1):
            raw = fp.read(frame_len)
            yuv = np.frombuffer(raw, dtype=dtype)
            yuv = yuv.reshape((height*3//2, width))

            if bpp==1:
                bgr_img = cv2.cvtColor(yuv, cv_format)
            else:
                yuv_tmp = yuv * 255.0 / 1023             # scale data from 10bit to 8bit: max value is 1023 for 10bit
                                                         #  Sn=a1*(1-q^n)/(1-q)  a1:1st vaule(1); q:2 n =10
                yuv_uint8=yuv_tmp.astype(np.uint8)
                bgr_img = cv2.cvtColor(yuv_uint8, cv_format)

            cv2.imwrite(output_name , bgr_img)

def convert_to_png(path):
    files=os.listdir(path)

    for file in files:
        fmts=parse_pix_fmts(file)
        width, height = parse_resolution(file)
    
        if fmts=="8bit_NV12":
            yuv2bgr(os.path.join(path,file), height, width,
                    "8bits", "nv12",
                    os.path.join(path,file.replace(".nv12",".png")))

        if fmts=="8bit_NV21":
            yuv2bgr(os.path.join(path,file), height, width,
                    "8bits", "nv21",
                    os.path.join(path,file.replace(".nv21",".png")))
    
        if fmts=="8bit_RGB444":
            with open(os.path.join(path,file), "rb") as fp:
                size_channel = height * width
                imgs = np.fromfile(fp, np.dtype('u1'))
                b=imgs[0:size_channel];g=imgs[size_channel:size_channel*2];r=imgs[size_channel*2:]
                r=r.reshape(height,width);g=g.reshape(height,width);b=b.reshape(height,width);
                img_rgb=np.dstack([r,g,b])
                save_name=os.path.join(path,file).replace(".rgb",".png")
                cv2.imwrite(save_name,img_rgb)
    
        if fmts=="8bit_YUV444":
            cmd="ffmpeg.exe -y -s %dx%d -pix_fmt yuv444p -i %s %s"%(width,height,
                                                              os.path.join(path,file),
                                                              os.path.join(path,file.replace(".yuv",".png")))
            os.system(cmd)
    
        if fmts=="10bit_NV12":
            yuv2bgr(os.path.join(path,file), height, width,
                    "10bits", "nv12",
                    os.path.join(path,file.replace(".nv12",".png")))

        if fmts=="10bit_NV21":
            yuv2bgr(os.path.join(path,file), height, width,
                    "10bits", "nv21",
                    os.path.join(path,file.replace(".nv21",".png")))
    
        if fmts=="10bit_RGB444":
            with open(os.path.join(path,file), "rb") as fp:
                size_channel = height * width
                imgs = np.fromfile(fp, np.dtype('u2'))
                b=imgs[0:size_channel];g=imgs[size_channel:size_channel*2];r=imgs[size_channel*2:]
                r=r.reshape(height,width);g=g.reshape(height,width);b=b.reshape(height,width);
                img_rgb=np.dstack([r,g,b])
                save_name=os.path.join(path,file).replace(".rgb",".png")
                cv2.imwrite(save_name,img_rgb)
    
        if fmts=="10bit_YUV444":
            cmd="ffmpeg.exe -y -s %dx%d -pix_fmt yuv444p10le -i %s %s"%(width,height,
                                                              os.path.join(path,file),
                                                              os.path.join(path,file.replace(".yuv",".png")))
            os.system(cmd)


if __name__=='__main__':

    path=local/path/here
    convert_to_png(path)


