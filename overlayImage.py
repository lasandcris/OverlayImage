import cv2
import numpy as np

src = cv2.imread("C:/Users/lrikk/Pictures/art-nature-twitter-background.jpg")		# Load a source image
overlay = cv2.imread("C:/Users/lrikk/Desktop/ping.png", -1)							# Load an image to overlay obviously smaller than the source

oheight, owidth, ochannels = overlay.shape
sheight, swidth, schannels = src.shape

b_channel, g_channel, r_channel = cv2.split(src)
src = cv2.merge((b_channel, g_channel, r_channel, b_channel))

for i in range(sheight):
    for j in range(swidth):
    	src[i,j,3]=255 			# Set alpha to 1 or 255

posx = 500						# Define a point (posx, posy) on the source
posy = 300						# image where the overlay will be placed
			
def OverlayImage(src, overlay, posx, posy):

	for x in range(owidth):

		if x+posx < swidth:

			for y in range(oheight):

				if y+posy < sheight:

					alpha = overlay[y, x, 3] / 255.0

					src[y+posy, x+posx] = (src[y+posy, x+posx]*(1.0-alpha)) + (overlay[y, x] * alpha)

						
OverlayImage(src, overlay, posx, posy)

cv2.imwrite('src.png', src) #Saves the image
print "Done"