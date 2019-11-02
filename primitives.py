#!/usr/bin/python3
import sys
import board
import neopixel as px
import time
from default import *

ORDER = px.GRB


def setPixel(strip, index, color=(255,255,255)):
	strip[index] = color;

def clearPixel(strip, index):
	setPixel(strip, index, (0,0,0))

def setPixels(strip, indexLo, indexHi, color=(255,255,255)):
	for p in range(indexHi-indexLo+1):
		setPixel(strip, p+indexLo, color)

def clearPixels(strip, indexLo, indexHi):
	setPixels(strip, indexLo, indexHi, (0,0,0))

def setStrip(strip, color=(255,255,255)):
	setPixels(strip, 0, strip.n-1, color)

def clearStrip(strip):
	setStrip(strip, (0,0,0))

def rgbOneToByte(r, g, b):
	return (int(r*255), int(g*255), int(b*255))

def rgbByteToOne(r, g, b):
	return (r/255, g/255, b/255)

RED          = (255,   0,   0)
#ORANGE       = (255, 127,   0)
ORANGE       = (255,  76,   0)
YELLOW       = (255, 255,   0)
LEMONLIME    = (127, 255,   0)
GREEN        = (  0, 255,   0)
AQUA         = (  0, 255, 127)
CYAN         = (  0, 255, 255)
LIGHTBLUE    = (  0, 127, 255)
BLUE         = (  0,   0, 255)
LAVENDER     = (127,   0, 255)
MAGENTA      = (255,   0, 255)
PINK         = (255,   0, 127)
WHITE        = (255, 255, 255)
EIGHTH       = ( 31,  31,  31)
QUARTER      = ( 63,  63,  63)
HALF         = (127, 127, 127)
THREEQUARTER = (191, 191, 191)
BLACK        = (  0,   0,   0)
SKY          = (  0, 200, 230)
FULL         = WHITE
ON           = WHITE
MID          = HALF
BLANK        = BLACK
OFF          = BLACK

"""
function rainbow(numOfSteps, step) {
    // This function generates vibrant, "evenly spaced" colours (i.e. no clustering). This is ideal for creating easily distinguishable vibrant markers in Google Maps and other apps.
    // Adam Cole, 2011-Sept-14
    // HSV to RBG adapted from: http://mjijackson.com/2008/02/rgb-to-hsl-and-rgb-to-hsv-color-model-conversion-algorithms-in-javascript
    var r, g, b;
    var h = step / numOfSteps;
    var i = ~~(h * 6);
    var f = h * 6 - i;
    var q = 1 - f;
    switch(i % 6){
        case 0: r = 1; g = f; b = 0; break;
        case 1: r = q; g = 1; b = 0; break;
        case 2: r = 0; g = 1; b = f; break;
        case 3: r = 0; g = q; b = 1; break;
        case 4: r = f; g = 0; b = 1; break;
        case 5: r = 1; g = 0; b = q; break;
    }
    var c = "#" + ("00" + (~ ~(r * 255)).toString(16)).slice(-2) + ("00" + (~ ~(g * 255)).toString(16)).slice(-2) + ("00" + (~ ~(b * 255)).toString(16)).slice(-2);
    return (c);
}
"""
def rainbow(steps, step):
	h = step / steps;
	i = int(h*6)
	f = h*6-i
	q = 1 - f
	rgbs = [(1,f,0),(q,1,0),(0,1,f),(0,q,1),(f,0,1),(1,0,q)]
	(r,g,b) = rgbs[i % 6]
	return rgbOneToByte(r,g,b)
