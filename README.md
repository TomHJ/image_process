# ISP related process
parse_rgb444_yuv444_nv12_nv21.py:convert 8bit/10bit RGB444,YUV444,NV12,NV21 to PNG by opencv, ffmpeg

raw_crop.py:raw cropped
- both raw load and save using numpy function: np.fromfile,np.tofile;
- dtype: 8bit 'u1'; 10bit~16bit 'u2'
- matplotlib.pylot to display the raw and cropped to raw(just intution/validation for crop operation); 
