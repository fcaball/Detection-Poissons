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
        #image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image = cv2.GaussianBlur(frame, (5, 5), 0)
        #image = cv2.equalizeHist(image)
        images.append(image)
    images = np.array(images)
    cap.release()
    return np.mean(images, axis = 0)


def compute_mask(image, background, threshold):
    #gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = image.shape
    mask = np.zeros([height, width], np.uint8)
    image = image.astype(np.uint32)
    for i in range(height):
        for j in range(width):
            if abs(background[i][j] - image[i][j])>threshold:
                mask[i][j] = 255
    kernel=np.ones((5, 5), np.uint8)
    mask=cv2.erode(mask, kernel, iterations=1)
    mask=cv2.dilate(mask, kernel, iterations=3)
    return mask


def detecter_vegetation_sous_marine(image_path, bloc_size, c):
    # Charger l'image
    image = cv2.imread(image_path)

    # Convertir l'image en niveaux de gris
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Filtrer par couleur (dans l'espace HSV)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    masque_couleur = cv2.inRange(hsv, (30, 40, 40), (90, 255, 255))

    # Filtrer par texture (utilisation du filtre de Laplace)
    laplacien = cv2.Laplacian(gris, cv2.CV_64F)
    laplacien_positif = np.maximum(laplacien, 0)

    # Binarisation adaptative pour la texture
    masque_texture = cv2.adaptiveThreshold(
        laplacien_positif.astype(np.uint8),
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        bloc_size,
        c
    )

    # Combiner les masques de couleur et de texture
    masque_combine = cv2.bitwise_and(masque_couleur, masque_texture)

    # Appliquer le masque combiné à l'image originale
    resultat = cv2.bitwise_and(image, image, mask=masque_combine)

    # Enregistrer l'image résultante
    return resultat


video = "videos/poissons6.mp4"
video_path_out = "without_dl_result_video/result_video_ameliorer_poissons6.mp4"
threshold = 100

cap = cv2.VideoCapture(video)

ret, frame = cap.read()

H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

background = mean_images(video, 500)
cv2.imwrite('background.png', background)

background_vegetation = detecter_vegetation_sous_marine('background.png', 11, 10)
cv2.imwrite('background_vege.png', background_vegetation)
new_background = background - background_vegetation
cv2.imwrite('new_background.png', new_background)
grey_background = cv2.imread('new_background.png')
grey_background = cv2.cvtColor(grey_background, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grey_background.png", grey_background)

cap = cv2.VideoCapture(video)

while True:
    print("ici")
    ret, frame = cap.read()
    cv2.imwrite('powbel/frame.png', frame)
    frame_vegetation = detecter_vegetation_sous_marine('powbel/frame.png', 11, 10)
    cv2.imwrite('powbel/frame_vege.png', frame_vegetation)
    new_frame = frame - frame_vegetation
    cv2.imwrite('powbel/new_frame.png', new_frame)
    grey_frame = cv2.imread('powbel/new_frame.png')
    grey_frame = cv2.cvtColor(grey_frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grey_frame.png", grey_frame)

    mask = compute_mask(grey_frame, grey_background, threshold)
    cv2.imwrite('powbel/mask.png', mask)
    contours=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in contours:
        # area = cv2.contourArea(c)
        # cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)  # -1 pour dessiner tous les contours
        ((x, y), rayon)=cv2.minEnclosingCircle(c)
        if rayon>20:
            cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), 10)
    out.write(frame)
    key=cv2.waitKey(1)&0xFF
    if key==ord('q'):
        break
    if key==ord('p'):
        threshold+=1
    if key==ord('m'):
        threshold-=1
cap.release()
out.release()
cv2.destroyAllWindows()





