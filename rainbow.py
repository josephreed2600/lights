#!/usr/bin/sudo python3

import sys

def rainbowSlide(strip, index_lo, index_hi, rainbows = 1, speed = 100):
	offset = 0
	length = index_hi-index_lo+1
	try:
		while(True):                                    
			for i in range(length):                       
				setPixel(strip, i+index_lo, rainbow(length/rainbows, (i+offset)%(length/rainbows)))
			offset = (offset-speed)#%(length*rainbows)
	except KeyboardInterrupt:
		sys.exit(0)

if __name__ == "__main__":
	import neopixel as px
	import board
	from primitives import setPixel, rainbow
	from default import *
	PIXEL_LO = default_int(1, 0)
	PIXEL_HI = default_int(2, 71)
	#PIXEL_COUNT = PIXEL_HI - PIXEL_LO + 1
	PIXEL_COUNT = PIXEL_HI + 1
	RAINBOW_COUNT = default_float(3, 1.0)
	SPEED = default_float(4, 1/3)
	BRIGHTNESS = default_float(5, 1.0)
	strip = px.NeoPixel(board.D18, PIXEL_COUNT, brightness=BRIGHTNESS, auto_write=True, pixel_order=px.GRB)
	rainbowSlide(strip, PIXEL_LO, PIXEL_HI, RAINBOW_COUNT, SPEED)
