import cv2
import numpy as np
from PIL import Image
import os
from  Error_Class import Error_project

def start_train(self, helpwindow, userchange, text, flags = 0):
    try:
        # Путь до папки с файлами
        helpwindow.path_programm = os.getcwd()
        helpwindow.dir_path = helpwindow.path_programm + "\dataset"

        #Путь до файла с фото
        path = helpwindow.dir_path

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        detector = cv2.CascadeClassifier(helpwindow.face_detected);

        count_mass = len(userchange.id_mass)
        # function to get the images and label data
        def getImagesAndLabels(path):

            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            faceSamples = []
            ids = []

            for imagePath in imagePaths:

                PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
                img_numpy = np.array(PIL_img, 'uint8')

                id = int(os.path.split(imagePath)[-1].split(".")[1])
                if count_mass != 0:
                    if int(id) in  userchange.id_mass:
                        faces = detector.detectMultiScale(img_numpy)
                    else:
                        continue
                else:
                    faces = detector.detectMultiScale(img_numpy)
                for (x, y, w, h) in faces:
                    faceSamples.append(img_numpy[y:y + h, x:x + w])
                    ids.append(id)

            return faceSamples, ids


        print("\n [INFO] Тренировка займёт несколько секунд")
        faces, ids = getImagesAndLabels(path)
        recognizer.train(faces, np.array(ids))

        if flags == 1:
        # Save the model into trainer/trainer.yml
            path_save_neiron = helpwindow.neiron_save  + "neiron"+ str(text) + ".yml"
            recognizer.write(path_save_neiron)  # recognizer.save() worked on Mac, but not on Pi
        else:
            path_save_neiron = helpwindow.neiron_save + str(text) + ".yml"
            recognizer.write(path_save_neiron)
        # Print the numer of faces trained and end program
        print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
        Error_project.error_27()
    except:
        Error_project.error_8()