# try to futher check nv12 under the hood
import numpy as np

path=r"sample.nv12"
width=3840
height=2160
bytes=1   # 8bit nv12

y=[]
u=[]
v=[]
with open(path,'rb') as f:
    for i in range(width*height*bytes):
        y.append(ord(f.read(1)))

    for j in range((width*height*bytes)//2):
        if(j%2==0):
            temp=ord(f.read(1))
            u.append(temp)
            u.append(temp)
        else:
            temp=ord(f.read(1))
            v.append(temp)
            v.append(temp)

arry_y=np.array(y).reshape((height,width))

arry_u=np.zeros((height,width))
arry_v=np.zeros((height,width))

temp_u=np.array(u).reshape((height//2,width))
arry_u[::2,::] =temp_u[:,:]
arry_u[1::2,::]=temp_u[:,:]

temp_v=np.array(v).reshape((height//2,width))
arry_v[::2,::]=temp_v[:,:]
arry_v[1::2,::]=temp_v[:,:]

# save some data to verify
with open("yuv.txt","a") as fw:
    for h in range(height):
        for w in range(width):
            if w<4:
                fw.write(str(arry_y[h,w])+" "+str(arry_u[h,w])+" "+str(arry_v[h,w])+"  ,")
            if w>3835:
                fw.write(str(arry_y[h, w]) + " " + str(arry_u[h, w]) + " " + str(arry_v[h, w]) + "  ,")
        fw.write("\n")


