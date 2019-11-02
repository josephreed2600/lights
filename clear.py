#!/usr/bin/sudo python3
import board
import neopixel

numOfPixels = 100
pixels = neopixel.NeoPixel(board.D18, numOfPixels)
pixels.show()
