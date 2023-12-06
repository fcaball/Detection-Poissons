import cv2
import numpy as np
from PIL import Image
from skimage import img_as_ubyte
from skimage import exposure
from skimage.restoration import denoise_bilateral
import sys

def median_filter(image, kernel_size):
    median_image = cv2.medianBlur(image, kernel_size)
    return median_image

def mean_filter(image, kernel_size):
    mean_image = cv2.blur(image, kernel_size)
    return mean_image

def histogram_equalize(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv_image[:,:,2] = cv2.equalizeHist(hsv_image[:,:,2])
    equalized_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    return equalized_image

def light_equalize(image, clip_limit, tile_grid_size):
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    L, A, B = cv2.split(lab_image)
    clahe = cv2.createCLAHE(clip_limit, tile_grid_size)
    L_equalized = clahe.apply(L)
    equalized_image = cv2.merge([L_equalized, A, B])
    equalized_image = cv2.cvtColor(equalized_image, cv2.COLOR_LAB2BGR)
    return equalized_image

def sharpen_image(image):
    # Création du noyau de filtre de netteté
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])

    # Application du filtre de netteté à l'image
    sharpened = cv2.filter2D(image, -1, kernel)

    return sharpened

import os

def extract_frames(video_path):
    video = cv2.VideoCapture(video_path)
    frames = []

    while True:
        success, frame = video.read()
        if not success:
            break
        frames.append(frame)

    video.release()
    return frames

# Extract frames
extracted_frames = extract_frames(sys.argv[3])

finalframes=[]
# Loop through all extracted frames
for img in extracted_frames:
    # Perform operations with each frame (for example, display the frame)
    if( sys.argv[1]=='median'):
        image=median_filter(img, 3)
        finalframes.append(image)
    elif( sys.argv[1]=='mean'):
        image=mean_filter(img, (int(sys.argv[4]), int(sys.argv[4])))
        finalframes.append(image)
    elif( sys.argv[1]=='histo'):
        image=histogram_equalize(img)
        finalframes.append(image)
    elif( sys.argv[1]=='light'):
        image=light_equalize(img, 2.0, (8, 8)) 
        finalframes.append(image)
    elif( sys.argv[1]=='nettete'):
        image=sharpen_image(img) 
        finalframes.append(image)    


def create_video(frames, output_path, fps=30.0):
    if len(frames) == 0:
        raise ValueError("Empty frame list")

    frame_height, frame_width = frames[0].shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec (depends on the file format)
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    for frame in frames:
        out.write(frame)

    out.release()

# Example usage:
# Assume 'extracted_frames' is a list containing all the frames extracted from the video
# Replace 'output_video.mp4' with the desired output file path
create_video(finalframes, sys.argv[2]+sys.argv[1]+'_output_video.mp4', fps=30.0)

cv2.waitKey(0)