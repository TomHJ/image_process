
import numpy as np
import matplotlib.pyplot as plt

path=r"/home/tom/software/utility/raw_crop/2560x1440_10b.raw"

# load the raw by numpy function
data=np.fromfile(path,dtype="u2")
data_array=data.reshape((1440,2560))

# crop raw
data_array_crop=data_array[350:950,900:1700]
plt.figure()
plt.imshow(data_array_crop)

# save the cropped raw
data_array_crop.tofile('crop.raw')

# show the cropped raw
crop_data=np.fromfile('crop.raw',dtype='u2')
crop_data_array=crop_data.reshape((600,800))
plt.figure()
plt.imshow(crop_data_array)
plt.show()
