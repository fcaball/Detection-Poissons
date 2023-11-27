import cv2

video_path = "videos/poisson6_rogner.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Erreur lors de l'ouverture de la video")
    exit()

num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Nombre total de frames dans la vidéo :", num_frames)

output_folder = "frames_video_poissons_6/"
if not cv2.os.path.exists(output_folder):
    cv2.os.makedirs(output_folder)

# Lire et enregistrer chaque frame
for frame_number in range(num_frames):
    ret, frame = cap.read()

    # Vérifier si la lecture du frame a réussi
    if not ret:
        print("Erreur lors de la lecture du frame.")
        break

    # Enregistrer le frame dans le dossier de sortie
    frame_filename = output_folder + f"frame_{frame_number:04d}.jpg"
    cv2.imwrite(frame_filename, frame)

    # Afficher la progression
    print(f"Enregistrement du frame {frame_number}/{num_frames}")


cap.release()