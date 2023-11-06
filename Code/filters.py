import cv2
import numpy as np

def balance_color(image_path):
    image_lab = cv2.cvtColor(image_path, cv2.COLOR_BGR2LAB)
    mean_a = np.mean(image_lab[:, :, 1])
    mean_b = np.mean(image_lab[:, :, 2])
    image_lab[:, :, 1] = image_lab[:, :, 1] - ((mean_a - 128) * (image_lab[:, :, 0] / 255.0) * 1.1)
    image_lab[:, :, 2] = image_lab[:, :, 2] - ((mean_b - 128) * (image_lab[:, :, 0] / 255.0) * 1.1)
    corrected_image = cv2.cvtColor(image_lab, cv2.COLOR_LAB2BGR)
    return corrected_image


def reduce_noise(image):
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    return denoised_image


def enhance_underwater_image(image):
    # Appliquer un filtre de renforcement des bords pour améliorer la netteté
    enhanced_image = cv2.filter2D(image, -1, kernel=np.array([[-1, -1, -1],
                                                             [-1, 9, -1],
                                                             [-1, -1, -1]]))

    return enhanced_image


def remove_suspended_particles(image, particle_size_threshold=20):
    # Convertir l'image en niveaux de gris
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un seuillage pour détecter les particules
    _, binary_image = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)

    # Trouver les contours des particules
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Créer un masque pour les particules à conserver
    mask = np.zeros_like(image)

    for contour in contours:
        # Calculer la surface de la particule
        area = cv2.contourArea(contour)

        if area > particle_size_threshold:
            # Dessiner la particule sur le masque
            cv2.drawContours(mask, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)

    # Appliquer le masque sur l'image d'origine pour supprimer les particules
    result_image = cv2.bitwise_xor(image, mask)

    return result_image

# Charger votre image
image = cv2.imread('VID_20230921_155530 max 500 fish/VID_20230921_155530_00135.png')

# Appliquer la correction de la balance des couleurs
corrected_image = balance_color(image)
enhanced_image = enhance_underwater_image(corrected_image)
result_image = remove_suspended_particles(enhanced_image)

# Enregistrer l'image corrigée
cv2.imwrite('image_corrigee.jpg', result_image)
