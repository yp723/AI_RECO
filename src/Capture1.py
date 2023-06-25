import cv2
import os
import os.path
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="6304466397",
  database="studentdata"
)
mycursor = mydb.cursor()
cursor = mydb.cursor(buffered=True)

def takeImages(i, n, g, ac, b, sec):
    Id = i
    name = n
    gender = g
    academicyear = ac
    branch = b
    section = sec
    if(Id.isalnum() and name.replace(' ','').isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30,30),flags = cv2.CASCADE_SCALE_IMAGE)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                sampleNum = sampleNum+1
                rev = Id[::-1][0:4]
                idd = rev[::-1]
                cv2.imwrite("TrainingImage" + os.sep +name + "."+idd + '.' +
                            str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                cv2.imshow('frame', img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        print(res)
        sql = "INSERT INTO studentdetails1(StudentId, StudentName, Gender, AcademicYear, Branch, Section) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (Id, name, gender, academicyear, branch, section)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Successful")
    else:
        print("Unsuccessful! Try again.")

