#!/usr/bin/python3

import sys
from ast import literal_eval as make_tuple

def default_string(index, defaultValue):
        if(len(sys.argv)-1 < index or sys.argv[index]==""):
                return defaultValue
        return sys.argv[index]

def default_int(index, defaultValue):
        if(len(sys.argv)-1 < index or sys.argv[index]==""):
                return defaultValue
        return int(sys.argv[index])

def default_float(index, defaultValue):
        if(len(sys.argv)-1 < index or sys.argv[index]==""):
                return defaultValue
        return float(sys.argv[index])

def default_tuple(index, defaultValue):
        if(len(sys.argv)-1 < index or sys.argv[index]==""):
                return defaultValue
        return make_tuple(sys.argv[index])
