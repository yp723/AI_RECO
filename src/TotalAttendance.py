import mysql.connector
import time
import datetime
from datetime import datetime, date

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="6304466397",
  database="studentdata"
)
cursor = mydb.cursor()
cursor.execute("SELECT StudentId FROM studentdetails")
Name = cursor.fetchall()
NAME = [x[0] for x in Name]
for name in NAME:
    A = 0
    P = 0
    N = 0
    cursor.execute("SELECT attendance FROM attendancedata WHERE StudentId = '{}'".format(name))
    Result = cursor.fetchall()
    Attendance = [x[0] for x in Result]
    for i in Attendance:
        if i == 'A':
            A = A + 1
        elif i == 'P':
            P = P + 1
        elif i == 'N':
            N = N + 1
    Total = 9
    Percentage = str((P/(Total-N)) * 100)
    sql = "INSERT INTO september(StudentId, September12th) VALUES (%s, %s)"
    val = (name, Percentage)
    cursor.execute(sql, val)
    mydb.commit()