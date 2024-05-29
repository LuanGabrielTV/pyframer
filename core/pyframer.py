
import cv2
import numpy as np


def fit_to_aspect_ratio(img, ar, color):
    height, width = img.shape[:2]
    nh = 0
    nw = 0
    # ar = (arw, arh)
    if(ar[0] > ar[1]):
        nw = int(height*ar[0]/ar[1])
        nh = height
    else:
        nh = int(width*ar[1]/ar[0])
        nw = width
    
    padding_vertical = int(abs(nh-height)/2)
    padding_horizontal = int(abs(nw-width)/2)
    return cv2.copyMakeBorder(img, padding_vertical, padding_vertical, padding_horizontal, padding_horizontal, borderType=cv2.BORDER_CONSTANT, value=color)