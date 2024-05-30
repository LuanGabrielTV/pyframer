
import cv2
import os


def read_path(path):
    ext = ['.png', '.jpeg', '.jpg']
    paths = []
    if os.path.isdir(path):
        paths = [(path+f) for f in os.listdir(path) if os.path.splitext(f).[1] in ext]
    if len(os.listdir(path))!=len(paths):
        print(", ".join(f for f in os.listdir(path) if os.path.splitext(f)[1] not in ext) + " aren't supported formats")
    else:
        paths = [path]
    
    return paths


def create_border(img, border_percent, color):
    # color = (r, g, b)
    height, width = img.shape[:2]
    padding_vertical = int(border_percent*height)
    padding_horizontal = int(border_percent*width)
    return cv2.copyMakeBorder(img, padding_vertical, padding_vertical, padding_horizontal, padding_horizontal, borderType=cv2.BORDER_CONSTANT, value=color)


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
