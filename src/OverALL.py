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
day = 'Monday'
First = ''
Second = ''
Third = ''
Fourth = ''
Fifth = ''
Sixth = ''
Seventh = ''
Eighth = ''
Ninth = ''
for name in NAME:
    cursor.execute("SELECT Subjects FROM subjects")
    SUBJECTS = cursor.fetchall()
    Subjects = [x[0] for x in SUBJECTS]
    for Sub in Subjects:
        if Sub == 'OperatingSystems':
            A = 0
            P = 0
            N = 0
            cursor.execute("SELECT attendance FROM attendancedata where Subjects = '{}' and StudentId = '{}'".format(Sub, name))
            Attendance = cursor.fetchall()
            Att = [x[0] for x in Attendance]
            cursor.execute("select count(SubjectNames) FROM timetable where SubjectNames = '{}' and day = '{}'".format(Sub, day))
            num = cursor.fetchone()
            for x in Att:
                if x == 'A':
                    A = A + 1
                elif x == 'P':
                    P = P + 1
                elif x == 'N':
                    N = N + 1
                Total = num[0]
                First = str((P / (Total - N)) * 100)
        if Sub == 'ComputerNetworks':
            A = 0
            P = 0
            N = 0
            cursor.execute("SELECT attendance FROM attendancedata where Subjects = '{}' AND StudentId = '{}'".format(Sub, name))
            Attendance = cursor.fetchall()
            Att = [x[0] for x in Attendance]
            cursor.execute("select count(SubjectNames) FROM timetable where SubjectNames = '{}' and day = '{}'".format(Sub, day))
            num = cursor.fetchone()
            for x in Att:
                if x == 'A':
                    A = A + 1
                elif x == 'P':
                    P = P + 1
                elif x == 'N':
                    N = N + 1
                Total = num[0]
                Second = str((P / (Total - N)) * 100)
        if Sub == 'FullStackDevelopment':
            A = 0
            P = 0
            N = 0
            cursor.execute("SELECT attendance FROM attendancedata where Subjects = '{}' AND StudentId = '{}'".format(Sub, name))
            Attendance = cursor.fetchall()
            Att = [x[0] for x in Attendance]
            cursor.execute("select count(SubjectNames) FROM timetable where SubjectNames = '{}' and day = '{}'".format(Sub, day))
            num = cursor.fetchone()
            for x in Att:
                if x == 'A':
                    A = A + 1
                elif x == 'P':
                    P = P + 1
                elif x == 'N':
                    N = N + 1
                Total = num[0]
                Third = str((P / (Total - N)) * 100)
        if Sub == 'DesignAndAnalysisOfAlgorithms':
            A = 0
            P = 0
            N = 0
            cursor.execute("SELECT attendance FROM attendancedata where Subjects = '{}' AND StudentId = '{}'".format(Sub, name))
            Attendance = cursor.fetchall()
            Att = [x[0] for x in Attendance]
            cursor.execute("select count(SubjectNames) FROM timetable where SubjectNames = '{}' and day = '{}'".format(Sub, day))
            num = cursor.fetchone()
            for x in Att:
                if x == 'A':
                    A = A + 1
                elif x == 'P':
                    P = P + 1
                elif x == 'N':
                    N = N + 1
                Total = num[0]
                Fourth = str((P / (Total - N)) * 100)
        if Sub == 'DataWarehousingAndDataMining':
            A = 0
            P = 0
            N = 0
            cursor.execute("SELECT attendance FROM attendancedata where Subjects = '{}' AND StudentId = '{}'".format(Sub, name))
            Attendance = cursor.fetchall()
            Att = [x[0] for x in Attendance]
            cursor.execute("select count(SubjectNames) FROM timetable where SubjectNames = '{}' and day = '{}'".format(Sub, day))
            num = cursor.fetchone()
            for x in Att:
                if x == 'A':
                    A = A + 1
                elif x == 'P':
                    P = P + 1
                elif x == 'N':
                    N = N + 1
                Total = num[0]
                Fifth = str((P / (Total - N)) * 100)
        if Sub == 'OpenElective-II':
            A = 0
            P = 0
            N = 0
            cursor.execute("SELECT attendance FROM attendancedata where Subjects = '{}' AND StudentId = '{}'".format(Sub, name))
            Attendance = cursor.fetchall()
            Att = [x[0] for x in Attendance]
            cursor.execute("select count(SubjectNames) FROM timetable where SubjectNames = '{}' and day = '{}'".format(Sub, day))
            num = cursor.fetchone()
            for x in Att:
                if x == 'A':
                    A = A + 1
                elif x == 'P':
                    P = P + 1
                elif x == 'N':
                    N = N + 1
                Total = num[0]
                Sixth = str((P / (Total - N)) * 100)
        if Sub == 'CNLab':
            A = 0
            P = 0
            N = 0
            cursor.execute("SELECT attendance FROM attendancedata where Subjects = '{}' AND StudentId = '{}'".format(Sub, name))
            Attendance = cursor.fetchall()
            Att = [x[0] for x in Attendance]
            cursor.execute("select count(SubjectNames) FROM timetable where SubjectNames = '{}' and day = '{}'".format(Sub, day))
            num = cursor.fetchone()
            for x in Att:
                if x == 'A':
                    A = A + 1
                elif x == 'P':
                    P = P + 1
                elif x == 'N':
                    N = N + 1
                Total = num[0]
                Seventh = str((P / (Total - N)) * 100)
        if Sub == 'CCLab':
            A = 0
            P = 0
            N = 0
            cursor.execute("SELECT attendance FROM attendancedata where Subjects = '{}' AND StudentId = '{}'".format(Sub, name))
            Attendance = cursor.fetchall()
            Att = [x[0] for x in Attendance]
            cursor.execute("select count(SubjectNames) FROM timetable where SubjectNames = '{}' and day = '{}'".format(Sub, day))
            num = cursor.fetchone()
            for x in Att:
                if x == 'A':
                    A = A + 1
                elif x == 'P':
                    P = P + 1
                elif x == 'N':
                    N = N + 1
                Total = num[0]
                Eighth = str((P / (Total - N)) * 100)
        if Sub == 'WADLab':
            A = 0
            P = 0
            N = 0
            cursor.execute("SELECT attendance FROM attendancedata where Subjects = '{}' AND StudentId = '{}'".format(Sub, name))
            Attendance = cursor.fetchall()
            Att = [x[0] for x in Attendance]
            cursor.execute("select count(SubjectNames) FROM timetable where SubjectNames = '{}' and day = '{}'".format(Sub, day))
            num = cursor.fetchone()
            for x in Att:
                if x == 'A':
                    A = A + 1
                elif x == 'P':
                    P = P + 1
                elif x == 'N':
                    N = N + 1
                Total = num[0]
                Ninth = str((P / (Total - N)) * 100)
    sql = "INSERT INTO overallattendancepercentagesubjectwise(StudentId, OperatingSystems, ComputerNetworks, FullStackDevelopment, DesignAndAnalysisOfAlgorithms, DataWarehousingAndDataMining, OpenElectiveII, CNLab, WADLab, CCLab) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (name, First, Second, Third, Fourth, Fifth, Sixth, Seventh, Ninth, Eighth)
    cursor.execute(sql, val)
    mydb.commit()
