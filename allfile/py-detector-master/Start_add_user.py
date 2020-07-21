import cv2
import os
import time

from Error_Class import Error_project


# Добавляем пользователей после проверок(их фото в папку)
def autom_start_add(self, helpwindow):
    # cv2.destroyAllWindows()
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height

    face_detector = cv2.CascadeClassifier(helpwindow.face_detected)
    eyeCascade = cv2.CascadeClassifier(helpwindow.eye_detected)
    smileCascade = cv2.CascadeClassifier(helpwindow.luck_detected)

    # Даём каждому человеку личный id
    face_id = self.id_user

    Error_project.error_3()
    time.sleep(3)

    # Начальное колличество фреймов
    count = 0

    while (True):

        ret, img = cam.read()
        # img = cv2.flip(img, -1)  # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, helpwindow.face_scaleFactor, helpwindow.face_minNeighbours)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            eyes = eyeCascade.detectMultiScale(
                roi_gray,
                scaleFactor=helpwindow.eye_scaleFactor,
                minNeighbors=helpwindow.eye_minNeighbours,
                minSize=helpwindow.eye_minSize,
            )

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            smile = smileCascade.detectMultiScale(
                roi_gray,
                scaleFactor=helpwindow.luck_scaleFactor,
                minNeighbors=helpwindow.luck_minNeighbours,
                minSize=helpwindow.luck_minSize,
            )

            for (xx, yy, ww, hh) in smile:
                cv2.rectangle(roi_color, (xx, yy), (xx + ww, yy + hh), (0, 255, 0), 2)

            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite(
                helpwindow.dir_path + str(face_id) + '.' + str(count) + ".jpg",
                gray[y:y + h, x:x + w])


            cv2.imshow('image', img)

        k = cv2.waitKey(50) & 0xff  # Нажмите ESC для выхода
        if k == 27:
            break
        elif count >= self.freim:  # Колличество кадров, для каждого человека
            break

    #Конец работы по 1 человеку
    Error_project.error_4()
    cam.release()
    cv2.destroyAllWindows()
