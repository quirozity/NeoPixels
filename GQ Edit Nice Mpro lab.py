#Ensure the ws2812.py file is on micro (pico or tiny2040) - currently set to 8MHz
#
#
#
#Phil J - April 26, refer to the ***overview document, tested on the tiny2040 - using pin GP7

import time
import ws2812b 

numpix = 10
strip = ws2812b.ws2812b(numpix, 0,7)

RED = (200, 0, 0) #255, 0,0 - the 135 is still pretty red (note order is corrected in the ws2812b lib)
ORANGE = (255, 165, 0)
YELLOW = (255, 150, 0)
GREEN = (255, 255, 0)
BLUE = (255, 0, 255)#0
INDIGO = (75, 0, 130)#0
VIOLET = (138, 43, 226)#138
COLORS = (RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET)
#COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET])

while True:
    #for color in COLORS:
	colorR = RED#, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET
	colorB = BLUE
	#ws2812b.set_pixel_line_gradient
	#(self, pixel1, pixel2, left_red, left_green, left_blue, right_red, right_green, right_blue)
	#color = ws2812b.set_pixel_line_gradient(COLORS) #just testing the data for a single wafer, using red.
	
        for i in range(numpix):
            strip.set_pixel_line_gradient(0,9,colorR[0], colorR[1], colorR[2], colorB[0], colorB[1], colorB[2])
            time.sleep(0.1)
            strip.show()
            
#         for i in range(1):
#             strip.set_pixel(i, color[0], color[1], color[2])
#             time.sleep(0.5)
#             strip.show()
