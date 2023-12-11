import cv2
import os
import numpy as np
from matplotlib import pyplot as plt


list_precision_moyenne = []
list_f1_score_moyen = []
list_rappel_moyen = []
list_thresholds = []
list_accuracy_moyenne = []
list_etiquettes = ["VP", "FP", "VN", "FN"]
list_valeurs = []

accuracy_moyenne = 0
precision_moyenne = 0
rappel_moyen = 0
f1_score_moyen = 0
vp_moyen = 0
vn_moyen = 0
fp_moyen = 0
fn_moyen = 0

def mean_images(video, nb_images):
    cap = cv2.VideoCapture(video)
    images = []
    for i in range(nb_images):
        ret, frame = cap.read()
        if ret is False:
            break
        image = cv2.GaussianBlur(frame, (5, 5), 0)
        images.append(image)
    images = np.array(images)
    cap.release()
    return np.mean(images, axis = 0)


def compute_mask(image, background, threshold):
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

def get_coord_rectangle(file_path):
    rectangles = []
    with open(file_path, 'r') as fichier:
        for ligne in fichier:
            elements = ligne.strip().split()
            all_elements = elements[-4:]
            all_elements = [float(coord) for coord in all_elements]
            rectangles.append(all_elements)
    return rectangles
          
def compute_rectangle_coins(rectangle):
    centre = [rectangle[0], rectangle[1]]
    width = rectangle[2]
    height = rectangle[3]
    x_max = centre[0] + width/2
    y_max = centre[1] + height/2
    coin_sup_gauche = [x_max, y_max]
    x_min = centre[0] - width/2
    y_min = centre[1] - height/2
    coin_inf_droit = [x_min, y_min]
    return coin_sup_gauche, coin_inf_droit

def pixel_is_in_rectangle(pixel_x, pixel_y, coin_sup_gauche, coin_inf_droit):
    x_min = coin_inf_droit[0]
    y_min = coin_inf_droit[1]
    x_max = coin_sup_gauche[0]
    y_max = coin_sup_gauche[1]

    return x_min <= pixel_x <= x_max and y_min <= pixel_y <= y_max

def denormalize_coord(coordonnees, width, height):
    coord_denorm = []
    x_denorm = coordonnees[0] * width
    y_denorm = coordonnees[1] * height
    coord_denorm = [x_denorm, y_denorm]
    return coord_denorm


labels_path = "labels_video_poissons_6"
frames_path = "frames_video_poissons_6"
video_path = "videos/poissons6.mp4"

list_labels_paths = []
list_frames_paths = []

label_files = sorted(os.listdir(labels_path), key=lambda x: int(x.split('_')[1].split('.')[0]))
for filename in label_files:
    file_path =  os.path.join(labels_path, filename)
    list_labels_paths.append(file_path)

frame_files = sorted(os.listdir(frames_path), key=lambda x: int(x.split('_')[1].split('.')[0]))
for filename in frame_files:
    file_path = os.path.join(frames_path, filename)
    list_frames_paths.append(file_path)

nb_images = list(range(len(list_frames_paths)))

background = mean_images(video_path, 500)
cv2.imwrite("background.png", background)
background_vegetation = detecter_vegetation_sous_marine('background.png', 11, 10)
cv2.imwrite('background_vege.png', background_vegetation)
new_background = background - background_vegetation
cv2.imwrite('new_background.png', new_background)
grey_background = cv2.imread('new_background.png')
grey_background = cv2.cvtColor(grey_background, cv2.COLOR_BGR2GRAY)


for threshold in range(25, 256, 25):
    print(threshold)
    list_thresholds.append(threshold)
    for label_path, frame_path in zip(list_labels_paths, list_frames_paths):
        print(f"Label path: {label_path}, Frame path: {frame_path}")
        frame = cv2.imread(frame_path)
        frame_vegetation = detecter_vegetation_sous_marine(frame_path, 11, 10)
        cv2.imwrite('powbel/frame_vege.png', frame_vegetation)
        new_frame = frame - frame_vegetation
        cv2.imwrite('powbel/new_frame.png', new_frame)
        grey_frame = cv2.imread('powbel/new_frame.png')
        grey_frame = cv2.cvtColor(grey_frame, cv2.COLOR_BGR2GRAY)
        mask = compute_mask(grey_frame, grey_background, threshold)
        cv2.imwrite('powbel/mask.png', mask)

        rectangles = get_coord_rectangle(label_path)

        vp = 0
        fp = 0
        vn = 0
        fn = 0

        height, width = mask.shape
        for pixel_y in range(height):
            for pixel_x in range(width):
                pixel = mask[pixel_y, pixel_x]
                for rectangle in rectangles:
                    coin_sup_gauche, coin_inf_droit = compute_rectangle_coins(rectangle)
                    coin_sup_gauche = denormalize_coord(coin_sup_gauche, width, height)
                    coin_inf_droit = denormalize_coord(coin_inf_droit, width, height)
                    if(pixel_is_in_rectangle(pixel_y, pixel_x, coin_sup_gauche, coin_inf_droit) and pixel == 255):
                        vp += 1
                    elif(pixel_is_in_rectangle(pixel_y, pixel_x, coin_sup_gauche, coin_inf_droit) and not pixel == 255):
                        fn += 1
                    elif(not pixel_is_in_rectangle(pixel_y, pixel_x, coin_sup_gauche, coin_inf_droit) and not pixel == 255):
                        vn += 1
                    else:
                        fp += 1

        accuracy = (vp + vn)/ (fp+fn+vp+vn)
        accuracy_moyenne = accuracy_moyenne + accuracy

        if vp == 0 and fp == 0:
            precision = 1
        else:
            precision = vp / (vp + fp)

        precision_moyenne = precision_moyenne + precision

        if vp == 0 and fn == 0:
            rappel = 1
        else:
            rappel = vp / (vp + fn)

        rappel_moyen = rappel_moyen + rappel

        if rappel == 0 and precision == 0:
            f1_score = 1
        else:
            f1_score = 2 * ((rappel * precision) / (rappel + precision))

        f1_score_moyen = f1_score_moyen + f1_score

       
        

    accuracy_moyenne = accuracy_moyenne/len(nb_images)
    list_accuracy_moyenne.append(accuracy_moyenne)
    print("Accuracy = ", accuracy_moyenne)

    precision_moyenne = precision_moyenne/len(nb_images)
    list_precision_moyenne.append(precision_moyenne)
    print("Precision = ", precision_moyenne)

    rappel_moyen = rappel_moyen/len(nb_images)
    list_rappel_moyen.append(rappel_moyen)
    print("Rappel = ", rappel_moyen)

    f1_score_moyen = f1_score_moyen/len(nb_images)
    list_f1_score_moyen.append(f1_score_moyen)
    print("F1 score = ", f1_score_moyen)
  
plt.plot(list_thresholds, list_accuracy_moyenne, color='b', label='Accuracy')
plt.plot(list_thresholds, list_f1_score_moyen, color='r', label='F1 score')
plt.plot(list_thresholds, list_rappel_moyen, color = 'g', label='Rappel')
plt.plot(list_thresholds, list_precision_moyenne, color='m', label='Précision')
plt.xlabel('Seuils')
plt.ylabel('Métriques')
plt.title('Différentes métriques en fonction du seuil')
plt.legend()
plt.savefig("analyse_without_dl/graph_avec_ameliorations.png")