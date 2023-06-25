import datetime
import os
import time
import cv2
import pandas as pd
import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="6304466397",
  database="studentdata"
)
mycursor = mydb.cursor()
cursor = mydb.cursor(buffered=True)

def recognize_attendence():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("./TrainingImageLabel/Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("StudentDetails"+os.sep+"StudentDetails.csv")
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['SNO', 'Id', 'Type', 'Time', 'Date']
    attendance = pd.DataFrame(columns=col_names)
    type = None


    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        _,im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5,minSize = (int(minW), int(minH)),flags = cv2.CASCADE_SCALE_IMAGE)
        for(x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x+w, y+h), (10, 159, 255), 2)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            print(Id, conf)
            cursor.execute("SELECT COUNT(*) FROM sessiontimings")
            n = cursor.fetchone()
            N = int(n[0]) + 1
            cursor.execute("SELECT TypeOfAttendance FROM sessiontimings WHERE StudentId = '{}' ORDER BY Time DESC".format('20481A'+str(Id)))
            type = cursor.fetchone()
            fId = '20481A'+str(Id)

            if conf < 100:

                confstr = "  {0}%".format(round(100 - conf))
                tt = str(Id)
            else:
                Id = '  Unknown  '
                tt = str(Id)
                confstr = "  {0}%".format(round(100 - conf))

            if (100-conf) > 40:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                attendance.loc[len(attendance)] = [N, fId, type, timeStamp, date]

            tt = str(tt)[2:-2]
            if(100-conf) > 67:
                tt = tt + " [Pass]"
                cv2.putText(im, str(tt), (x+5,y-5), font, 1, (255, 255, 255), 2)
            else:
                cv2.putText(im, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2)

            if (100-conf) > 67:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font,1, (0, 255, 0),1 )
            elif (100-conf) > 50:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 255), 1)
            else:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 0, 255), 1)

        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('Attendance', im)
        if cv2.waitKey(500)  or  cv2.waitKey(0) == ord('q'):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    print("Attendance Successful")
    print(attendance)
    if type is None:
        sql = "INSERT INTO sessiontimings(SNO, StudentId, TypeOfAttendance, Time, Date) VALUES (%s, %s, %s, %s, %s)"
        val = (N, fId, '0', timeStamp, date)
        mycursor.execute(sql, val)
        mydb.commit()
    else:
        if type[0] == 1:
            sql = "INSERT INTO sessiontimings(SNO, StudentId, TypeOfAttendance, Time, Date) VALUES (%s, %s, %s, %s, %s)"
            val = (N, fId, '0', timeStamp, date)
            mycursor.execute(sql, val)
            mydb.commit()
        elif type[0] == 0:
            sql = "INSERT INTO sessiontimings(SNO, StudentId, TypeOfAttendance, Time, Date) VALUES (%s, %s, %s, %s, %s)"
            val = (N, fId, '1', timeStamp, date)
            mycursor.execute(sql, val)
            mydb.commit()
    msg = " " + attendance["Id"] + " " + attendance["Date"] + " " + attendance["Time"]
    msg = msg.to_string(index = False)
    print(msg)
    i = attendance["Id"].to_string(index = False)
    from tkinter import messagebox
    messagebox.showinfo(i, msg)

    cam.release()
    cv2.destroyAllWindows()
