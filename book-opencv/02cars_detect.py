import cv2
import numpy as np
from os.path import join

datapath = ""

def path(cls, i):
    return "%s/%s%d.pgm" % (datapath, cls, i+1)

pos, neg = "pos-", "neg-"

detect = cv2.xfeatures2d.SIFT_create()
extract = cv2.xfeatures2d.SIFT_create()

flann_params = dict()