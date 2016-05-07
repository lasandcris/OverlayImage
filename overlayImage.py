import cv2
import numpy as np

src = cv2.imread("C:/Users/lrikk/Pictures/art-nature-twitter-background.jpg")		# Load a source image
overlay = cv2.imread("C:/Users/lrikk/Pictures/sdg.png", -1)		# Load an image to overlay obviously smaller than the source

oheight, owidth, ochannels = overlay.shape
print oheight, owidth, ochannels

sheight, swidth, schannels = src.shape
print sheight, swidth, schannels


posx = 500				# Define a point (posx, posy) on the source
posy = 300					# image where the overlay will be placed
S = (0.5, 0.5, 0.5, 0.5)			# Define blending coefficients S and D
D = (0.5, 0.5, 0.5, 0.5)			

def OverlayImage(src, overlay, posx, posy, S, D):

	for x in range(owidth):

		if x+posx < swidth:

			for y in range(oheight):

				if y+posy < sheight:

					source = src[y+posy, x+posx]
					over   = overlay[y, x]

					src[y+posy, x+posx] = (S*source+D*over)


OverlayImage(src, overlay, posx, posy, S, D)

cv2.imwrite('src.png', src) #Saves the image
print "Done"