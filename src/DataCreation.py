import sys
import os
import cv2
import numpy
import shutil
import face_recognition
from imutils import paths
import ctypes

e_id = input('Enter Student ID: ')
num = int(input("Enter the number of shots you want to take: "))

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

Screen_Width = 820
Screen_Height = 620

Screen_Center_Width = int((screensize[0] - Screen_Width) / 2)
Screen_Center_Height = int((screensize[1] - Screen_Height) / 2) - 30

cap = cv2.VideoCapture(0)

folder_name = e_id
total = num
current = 1

font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10, 40)
fontScale = 1
fontColor = (0, 0, 255)
lineType = 2

CapturePosition = (10, 80)
CaptureFontColor = (255, 0, 0)
ExitPosition = (10, 120)

if not os.path.exists("D:\\Dataset\\{}".format(folder_name)):
    os.makedirs("D:\\Dataset\\{}".format(folder_name))

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (Screen_Width, Screen_Height))

    newImage = frame.copy()
    cv2.putText(newImage, '({} / {})'.format(current - 1, total), bottomLeftCornerOfText, font, fontScale, fontColor,
                lineType)
    cv2.putText(newImage, "Press 'Spacebar' to capture images".format(current, total), CapturePosition, font, 1,
                CaptureFontColor, 2)
    cv2.putText(newImage, "Press 'Escape' to start again".format(current, total), ExitPosition, font, 1,
                CaptureFontColor, 2)
    cv2.imshow("Display", newImage)
    cv2.moveWindow('Display', Screen_Center_Width, Screen_Center_Height)  ##center window
    k = cv2.waitKey(1)

    if k == 32:
        if int(current) <= int(total):
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(rgb, model="hog")
            if (len(boxes) != 0):
                cv2.imwrite("D:\\Dataset\\{}\\{}.jpg".format(folder_name, current), frame)
                print("Image No: {}".format(current))
                current = current + 1
                print("Ok, Next")
                print(current)
            else:
                print("Try Again")
        else:
            try:
                file = open("D:\\Data_Creator_Status.txt", "w")
                file.write("Finished")
                file.close()
                exit()
            except Exception as e:
                exit()
    elif k == 27:
        print("The image capturing process has been stopped by the user.")
        shutil.rmtree("D:\\Dataset\\{}".format(folder_name))
        try:
            file = open("D:\\Data_Creator_Status.txt", "w")
            file.write("Stopped")
            file.close()
            exit()
        except Exception as e:
            exit()