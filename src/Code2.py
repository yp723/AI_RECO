import face_recognition
import pickle
import cv2
import numpy as np
import os
import time
import mysql.connector
from datetime import date
import Recognize

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

while True:
    data = pickle.loads(open("D:\\TrainingModels\\Model.pickle", "rb").read())
    known_face_encoding = data["encodings"]
    known_faces_names = data["names"]
    students = known_faces_names.copy()
    face_locations = []
    face_encoding = []
    face_names = []
    s = True
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0), fx = 0.25, fy = 0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_name = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
            face_names.append(name)
            if name in known_faces_names:
                if name in students:
                    cursor.execute("SELECT COUNT(*) FROM sessiontimings")
                    n = cursor.fetchone()
                    N = int(n[0])+1
                    cursor.execute("SELECT TypeOfAttendance FROM sessiontimings WHERE StudentId = '{}' ORDER BY Time DESC".format(name))
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
    cv2.imshow("attendence system", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()