import cv2
import numpy as np
from matplotlib import pyplot as plt

def mean_images(video, nb_images):
    cap = cv2.VideoCapture(video)
    images = []
    for i in range(nb_images):
        ret, frame = cap.read()
        if ret is False:
            break
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image = cv2.GaussianBlur(image, (5, 5), 0)
        image = cv2.equalizeHist(image)
        images.append(image)
    images = np.array(images)
    cap.release()
    return np.mean(images, axis = 0)


def compute_mask(image, background, threshold):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray_image.shape
    mask = np.zeros([height, width], np.uint8)
    gray_image = gray_image.astype(np.uint32)
    for i in range(height):
        for j in range(width):
            if abs(background[i][j] - gray_image[i][j])>threshold:
                mask[i][j] = 255
    kernel=np.ones((5, 5), np.uint8)
    mask=cv2.erode(mask, kernel, iterations=1)
    mask=cv2.dilate(mask, kernel, iterations=3)
    return mask


video = "videos/poissons1.mp4"
threshold = 60

background = mean_images(video, 500)

# cv2.imshow('background', background.astype(np.uint8))
# cv2.waitKey(0)

cap = cv2.VideoCapture(video)

while True:
    ret, frame = cap.read()
    mask = compute_mask(frame, background, threshold)
    contours=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in contours:
        #cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)  # -1 pour dessiner tous les contours
        ((x, y), rayon)=cv2.minEnclosingCircle(c)
        if rayon>20:
            cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), 10)
    cv2.imshow('video', frame)
    cv2.imshow('mask', mask)
    key=cv2.waitKey(1)&0xFF
    if key==ord('q'):
        break
    if key==ord('p'):
        threshold+=1
    if key==ord('m'):
        threshold-=1
cap.release()
cv2.destroyAllWindows()





