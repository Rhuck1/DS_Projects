import cv2
import numpy as np

def read_file(filename):

    img = cv2.imread(filename)
    cv2.imshow(img)
    return img

read_file("me.jpeg")