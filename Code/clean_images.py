import cv2
import numpy as np
from PIL import Image
from skimage import img_as_ubyte
from skimage.restoration import denoise_bilateral
from skimage import exposure

def median_filter(image_path, kernel_size):
    image = cv2.imread(image_path)
    median_image = cv2.medianBlur(image, kernel_size)
    return median_image

def mean_filter(image_path, kernel_size):
    image = cv2.imread(image_path)
    mean_image = cv2.blur(image, kernel_size)
    return mean_image

def histogram_equalize(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv_image[:,:,2] = cv2.equalizeHist(hsv_image[:,:,2])
    equalized_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    return equalized_image

def light_equalize(image_path, clip_limit, tile_grid_size):
    image = cv2.imread(image_path)
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    L, A, B = cv2.split(lab_image)
    clahe = cv2.createCLAHE(clip_limit, tile_grid_size)
    L_equalized = clahe.apply(L)
    equalized_image = cv2.merge([L_equalized, A, B])
    equalized_image = cv2.cvtColor(equalized_image, cv2.COLOR_LAB2BGR)
    return equalized_image






mean_image = light_equalize("image_poissons.jpeg")
cv2.imshow("Image filtree", mean_image)
cv2.waitKey(0)