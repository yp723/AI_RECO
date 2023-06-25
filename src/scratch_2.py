import os
from time import strftime
import face_recognition
import cv2
import pickle
import warnings
import numpy as np
import csv
import os
import datetime as datetime, time

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

video_capture = cv2.VideoCapture(0)

t = time.localtime()
today = date.today()

data = pickle.loads(open("D:\\TrainingModels\\Model.pickle", "rb").read())
known_face_encodings = data["encodings"]
known_face_names = data["names"]
students = known_face_names.copy()

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

noe = datetime.time()
current_date = noe.strftime("%Y-%M-%D")

while True:
    ret, frame = video_capture.read()

    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)
            warnings.simplefilter(action='ignore', category=FutureWarning)
            if name in known_face_names:
                if name in students:
                    cursor.execute("SELECT COUNT(*) FROM sessiontimings")
                    n = cursor.fetchone()
                    N = int(n[0]) + 1
                    cursor.execute(
                        "SELECT TypeOfAttendance FROM sessiontimings WHERE StudentId = '{}' ORDER BY Time DESC".format(
                            name))
                    TypeOfAttendance = cursor.fetchone()
                    if TypeOfAttendance == None:
                        students.remove(name)
                        current_time = time.strftime("%H:%M:%S")
                        sql = "INSERT INTO sessiontimings(SNO, StudentId, TypeOfAttendance, Time, Date) VALUES (%s, %s, %s, %s, %s)"
                        val = (N, name, '0', current_time, today)
                        mycursor.execute(sql, val)
                        mydb.commit()
                    else:
                        if TypeOfAttendance[0] == 1:
                            students.remove(name)
                            current_time = time.strftime("%H:%M:%S")
                            sql = "INSERT INTO sessiontimings(SNO, StudentId, TypeOfAttendance, Time, Date) VALUES (%s, %s, %s, %s, %s)"
                            val = (N, name, '0', current_time, today)
                            mycursor.execute(sql, val)
                            mydb.commit()
                        elif TypeOfAttendance[0] == 0:
                            students.remove(name)
                            current_time = time.strftime("%H:%M:%S")
                            sql = "INSERT INTO sessiontimings(SNO, StudentId, TypeOfAttendance, Time, Date) VALUES (%s, %s, %s, %s, %s)"
                            val = (N, name, '1', current_time, today)
                            mycursor.execute(sql, val)
                            mydb.commit()

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()