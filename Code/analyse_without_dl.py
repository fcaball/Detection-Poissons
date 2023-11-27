import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
#from without_dl import mean_images, compute_mask

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

def draw_curve(thresholds, accuracies, plot_save_path):
    plt.plot(thresholds, accuracies, marker='o', linestyle='-')
    plt.title('Évolution de l\'accuracy en fonction du seuil')
    plt.xlabel('Threshold')
    plt.ylabel('Accuracy')
    plt.grid(True)
    plt.savefig(plot_save_path)


labels_path = "labels_video_poissons_6"
frames_path = "frames_video_poissons_6"
video_path = "videos/poissons6.mp4"
plot_save_folder = "analyse_without_dl"
plot_name_file = "graph_sans_ameliorations_et_threshold.png"

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

background = mean_images(video_path, 500)
cv2.imwrite("images_pipeline/background.png", background)
#threshold = 600

list_precision_moyenne = []
list_f1_score_moyen = []
list_rappel_moyen = []
list_thresholds = []
list_accuracy_moyenne = []
list_etiquettes = ["VP", "FP", "VN", "FN"]
list_valeurs = []

nb_images = list(range(len(list_frames_paths)))
accuracy_moyenne = 0
precision_moyenne = 0
rappel_moyen = 0
f1_score_moyen = 0
vp_moyen = 0
vn_moyen = 0
fp_moyen = 0
fn_moyen = 0

for threshold in range(25, 256, 25):
    print(threshold)
    list_thresholds.append(threshold)
    for label_path, frame_path in zip(list_labels_paths, list_frames_paths):
        print(f"Label path: {label_path}, Frame path: {frame_path}")
        image = cv2.imread(frame_path)
        #image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #cv2.imwrite(f"images_pipeline/frame_{threshold}.png", image_gray)
        mask = compute_mask(image, background, threshold)
        #cv2.imwrite(f"images_pipeline/mask_{threshold}.png", mask)
        contours=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        for c in contours:
            ((x, y), rayon)=cv2.minEnclosingCircle(c)
            if rayon>20:
                cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), 10)
        #cv2.imwrite(f"images_pipeline/image_marquee_{threshold}.png", image)

        rectangles = get_coord_rectangle(label_path)

        vp = 0
        fp = 0
        vn = 0
        fn = 0

        height, width = mask.shape
        #print("Taille de l'image = ", width*height)
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

        # print(vp + fp + vn + fn)
        #taux_vp_sensibilite = (vp / (vp + fn)) * 100
        vp_moyen = vp_moyen + vp

        #taux_vn_specificite = (vn / (vn + fp)) * 100
        vn_moyen = vn_moyen + vn

        #taux_fp = 100 - taux_vn_specificite
        fp_moyen = fp_moyen + fp

        #taux_fn =  100 - taux_vp_sensibilite
        fn_moyen = fn_moyen + fn

        accuracy = (vp + vn)/ (fp+fn+vp+vn)
        accuracy_moyenne = accuracy_moyenne + accuracy

        precision = vp / (vp + fp)
        precision_moyenne = precision_moyenne + precision

        if vp == 0 and fn == 0:
            rappel = 0

        rappel = vp / (vp + fn)
        rappel_moyen = rappel_moyen + rappel

        if rappel == 0 and precision == 0:
            f1_score = 0

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


    vp_moyen = vp_moyen/len(nb_images)
    vn_moyen = vn_moyen/len(nb_images)
    fp_moyen = fp_moyen/len(nb_images)
    fn_moyen = fn_moyen/len(nb_images)
    list_valeurs.append(vp_moyen)
    list_valeurs.append(fp_moyen)
    list_valeurs.append(vn_moyen)
    list_valeurs.append(fn_moyen)


    plt.pie(list_valeurs, labels=list_etiquettes, autopct='%1.1f%%', startangle=90)
    plt.title('Répartition des catégories')
    plt.savefig(f"analyse_without_dl/camembert_{threshold}.png")

plot_save_path = os.path.join(plot_save_folder, plot_name_file)    
draw_curve(list_thresholds, list_accuracy_moyenne, plot_save_path)   

draw_curve(list_thresholds, list_precision_moyenne, os.path.join(plot_save_folder,"precision_without_ameliorations.png"))
draw_curve(list_thresholds, list_rappel_moyen, os.path.join(plot_save_folder,"rappel_without_ameliorations.png"))
draw_curve(list_thresholds, list_f1_score_moyen, os.path.join(plot_save_folder,"f1_score_without_ameliorations.png"))




