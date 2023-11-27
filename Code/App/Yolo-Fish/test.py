import cv2
import sys
import time

def create_black_image(file_name):
    # Création d'une image entièrement noire de 100x100 pixels
    image = 255 * 0  # Création d'une image noire

    # Sauvegarde de l'image avec le nom passé en argument
    cv2.imwrite(file_name, image)
    print(f"Image {file_name} créée avec succès.")
    time.sleep(60
               
               )  # Pause de 10 secondes
    print("Fin du script après la pause.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <nom_de_l_image>")
    else:
        image_name = sys.argv[1]
        create_black_image(image_name)
