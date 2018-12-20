#edited:180610
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import numpy as np
from scipy import misc

try:
	#读取一张小白狗的照片并显示
	plt.figure('av_img')
	av_img = mpimg.imread('E:\\Learn\\Paint\\av2.jpg')
	
	av_img_new_size = misc.imresize(av_img,2.0)
	
	plt.imshow(av_img_new_size)
	plt.axis('off')
	plt.show(av_img_new_size)

except Exception as e:
	print(e)
