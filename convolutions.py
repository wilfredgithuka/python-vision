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
