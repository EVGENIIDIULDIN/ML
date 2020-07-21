import cv2
import numpy as np
import os
from Error_Class import Error_project
import sys
import time
import threading


def pre_start_train(self, helpwindow, cameraparam, neirons):
    if len(cameraparam.camera_mass) == 0:
        start_test_neirons(self, helpwindow, 0,  neirons)
    else:
        for i in cameraparam.camera_mass:
            t = threading.Thread(target=start_test_neirons,
                                 args=(self, helpwindow, i, neirons))
            t.start()


def start_test_neirons(self, helpwindow, camera_digit, neirons):
    try:

        if camera_digit == 0:
            path_save_load = helpwindow.neiron_save + neirons.first_cam
        if camera_digit == 1:
            path_save_load = helpwindow.neiron_save + neirons.second_cam
        if camera_digit == 2:
            path_save_load = helpwindow.neiron_save + neirons.third_cam
        if camera_digit == 3:
            path_save_load = helpwindow.neiron_save + neirons.thourth_cam

    except:
        path_save_load = helpwindow.neiron_save + "trainer.yml"

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(path_save_load)
    cascadePath = helpwindow.face_detected

    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX

    #Задаём путь до сохранения подозреваемых

    path_programms = os.getcwd()
    path = path_programms + "\\DETECTED\\"

    #Создаём словарь ожидания
    user_wait = dict()
    # iniciate id counter
    id = 0

    # names related to ids: example ==> Marcelo: id=1,  etc
    # names = ["sdsd"]
    names = dict()


    with open(helpwindow.path_id + "IDCategoryName.txt", 'r') as f:
        for lines in f:
            temp = lines.strip().split('^^')
            names[int(temp[0])] = [str(temp[1]), str(temp[2])]

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(int(camera_digit) + cv2.CAP_DSHOW)
    cam.set(3, 640)  # set video widht
    cam.set(4, 480)  # set video height

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:

        ret, img = cam.read()
        # img = cv2.flip(img, -1)  # Flip vertically

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                try:
                    ids = names[id][0]
                    caracterist = names[id][1]
                    confidence = "  {0}%".format(round(100 - confidence))

                    #Добавляем в массив человека при первом появлении
                    if int(id) in user_wait:
                        user_wait[int(id)] += 1
                    else:
                        user_wait[int(id)] = 0


                    #Проверяем человека на подозреваемого
                    # if int(confidence) > 50:  # Пороговое значение доверия
                    if names[id][1] == "verifiable":
                        if user_wait[int(id)] % 200 == 0:
                            end_str = str(names[id][0]) + str(user_wait[int(id)])
                            cv2.imwrite(
                                path + f"camera{str(camera_digit)}\\" + f"{end_str}" +".jpg",
                                img)
                    else:
                        pass
                except:
                    ids = "UserUnknown"
                    caracterist = "No character"
                    confidence = "0"
            else:
                try:
                    ids = "unknown"
                    caracterist = 'unknown'
                    confidence = "  {0}%".format(round(100 - confidence))
                except:
                    ids = "UserUnknown"
                    caracterist = "No character"
                    confidence = "0"

            cv2.putText(img, str(ids), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
            cv2.putText(img, str(caracterist), (x, y + h + 30), font, 1, (255, 255, 0), 1)

            # cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)

        cv2.imshow('camera' + str(camera_digit), img)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break

    # Do a bit of cleanup
    # print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
