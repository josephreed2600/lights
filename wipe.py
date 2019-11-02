#!/usr/bin/sudo python3

def wipe(strip, pixel_first, pixel_last, color, delay):
	for i in range(pixel_last - pixel_first):
		setPixel(strip, i+pixel_first, color)
		strip.show()
		if callable(delay):
			time.sleep(delay())
		else:
			time.sleep(delay)

if __name__ == "__main__":
	import sys
	import board
	import neopixel as px
	import time
	from default import *
	from primitives import *
	PIXEL_LO = default_int(1, 0)
	PIXEL_HI = default_int(2, 71)
	#PIXEL_COUNT = PIXEL_HI - PIXEL_LO + 1
	PIXEL_COUNT = PIXEL_HI + 1
	COLOR = default_tuple(3, (0,0,0))
	DELAY = default_float(4, 0.0)
	BRIGHTNESS = default_float(5, 1.0)
	strip = px.NeoPixel(board.D18, PIXEL_COUNT, brightness = BRIGHTNESS, auto_write = False, pixel_order = px.GRB)
	wipe(strip, PIXEL_LO, PIXEL_HI, COLOR, DELAY)
