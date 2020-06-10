# Some ISP related process

parse_nv12.py: check how 8bit nv12 was stored in memory
               y bytes number: width* height
               u bytes number: width* height//4
               v bytes number: width* height//4
               
               stored method
               Y00            Y01       Y02...       Y0(w-1)
               Y10            Y11       Y12...       Y1(w-1)
               ................................................
               Y(h-1)0       Y(h-1)1 ...Y(h-1)2      Y(h-1)(w-1)
               u00            v00        u01...      v0(w//2)
               u10            v10        u11...      v1(w//2)
               .................................................
               u(h//2-1)0  v(h//2-1)0 u(h//2-1)1 ... v(h//2-1)(w//2) 
               
               
               decode y,u,v for every pixel as below:
      
               y00 u00 v00, y01 u00 v00, y02 u01 v01, y03,u01,v01...........
               y10 u00 v00, y11 u00 v00, y12 u11 v01, y13,u01,v01...........
               
               
               

convert_rgb444_yuv444_nv12_nv21_to_png.py:convert 8bit/10bit RGB444,YUV444,NV12,NV21 to PNG by opencv, ffmpeg

raw_crop.py:raw cropped
- both raw load and save using numpy function: np.fromfile,np.tofile;
- dtype: 8bit 'u1'; 10bit~16bit 'u2'
- matplotlib.pylot to display the raw and cropped raw(just intution/validation for crop operation); 
