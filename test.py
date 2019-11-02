#!/usr/bin/python3
import sys
import board
import neopixel as px
import time
from default import *
from primitives import *
from wipe import *
strip = px.NeoPixel(board.D18, 72, brightness=1, auto_write=True, pixel_order=px.GRB)
