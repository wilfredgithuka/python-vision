#WilfredGithuka
#Githuka.com
#Implementing_Convolutions_with_OpenCV_and_Python
#pyimagesearch.com

from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2

#The convolve method

def convolve(image, kernel):
	#Grab the spatial dimensions of the image as well as those of the kernel
	(iH, iW) = image.shape[:2]
	(kH, kW) = kernel.shape[:2]
	
	#Allocate memory for the output image, taking care to pad the borders of the input image
	#so that the spatial size are not reduced

	pad = (kW - 1) / 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
		cv2.BORDER_REPLICATE)
	output = np.zeros((iH, iW), dtype="float32")
	
	#scan over the input image, sliding the kernel accross each (x,y) cordinate from
	#left to right and top to bottom
	
	for y in np.arrange(pad, iH + pad):
		for x in np.arrange(pad, iW + pad):
	
		#extract the region of interest of the image by extracting the *center* region
		# of the current (x,y) cordinates dimensions
	
		roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

		#the actual convolution
		
		k = (roi * kernel).sum()
	
		#store the convolved value in the output (x,y) cordiate of the output image
	
		output[y - pad, x - pad] = k

		#rescale the output image to be in the range [0, 255]
	
		output = rescale_intensity(output, in_range=(0, 255))
		output = (output * 255).astype("uint8")
 
		# return the output image
		return output
