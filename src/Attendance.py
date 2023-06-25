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
t = time.localtime()
today = date.today()
cursor.execute("SELECT StudentId FROM studentdetails")
Name = cursor.fetchall()
NAME = [x[0] for x in Name]
for name in NAME:
    cursor.execute("SELECT Time FROM sessiontimings WHERE StudentId = '{}'".format(name))
    Result = cursor.fetchall()
    TIME = [x[0] for x in Result]
    x = 0
    data={"1":"A", "2":"A", "3":"A", "4":"A", "5":"A", "6":"A", "7":"A", "8":"A", "9":"A"}
    for T in range(len(TIME)):
        W = TIME[T]
        Obj_W = datetime.strptime(W, '%H:%M:%S')
        if T+1 in range(len(TIME)):
            X = TIME[T+1]
            Obj_X = datetime.strptime(X, '%H:%M:%S')
            WX = str(Obj_X - Obj_W)
            Obj_WX = datetime.strptime(WX, '%H:%M:%S')
        if T+2 in range(len(TIME)):
            Y = TIME[T+2]
            Obj_Y = datetime.strptime(Y, '%H:%M:%S')
            XY = str(Obj_Y - Obj_X)
            Obj_XY = datetime.strptime(XY, '%H:%M:%S')
        if T+3 in range(len(TIME)):
            Z = TIME[T+3]
            Obj_Z = datetime.strptime(Z, '%H:%M:%S')
            YZ = str(Obj_Z - Obj_Y)
            Obj_YZ = datetime.strptime(YZ, '%H:%M:%S')
            time_zero = '00:00:00'
            Obj_time_zero = datetime.strptime(time_zero, '%H:%M:%S')
            WXYZ = str(Obj_YZ - Obj_time_zero + Obj_WX)
            Obj_WXYZ = datetime.strptime(WXYZ, "%Y-%m-%d %H:%M:%S")
        Period1_IN = '09:00:00'
        Obj_Period1_IN = datetime.strptime(Period1_IN, '%H:%M:%S')
        Period1_Allowed = '09:10:00'
        Obj_Period1_Allowed = datetime.strptime(Period1_Allowed, '%H:%M:%S')
        PeriodTime = '00:40:00'
        Obj_PeriodTime = datetime.strptime(PeriodTime, '%H:%M:%S')
        PeriodNotAllowed = '00:20:00'
        Obj_PeriodNotAllowed = datetime.strptime(PeriodNotAllowed, '%H:%M:%S')
        Period1_OUT = '09:50:00'
        Obj_Period1_OUT = datetime.strptime(Period1_OUT, '%H:%M:%S')
        Period2_IN = '09:50:00'
        Obj_Period2_IN = datetime.strptime(Period2_IN, '%H:%M:%S')
        Period2_Allowed = '10:00:00'
        Obj_Period2_Allowed = datetime.strptime(Period2_Allowed, '%H:%M:%S')
        Period2_OUT = '10:40:00'
        Obj_Period2_OUT = datetime.strptime(Period2_OUT, '%H:%M:%S')
        Period3_IN = '10:40:00'
        Obj_Period3_IN = datetime.strptime(Period3_IN, '%H:%M:%S')
        Period3_Allowed = '10:50:00'
        Obj_Period3_Allowed = datetime.strptime(Period3_Allowed, '%H:%M:%S')
        Period3_OUT = '11:30:00'
        Obj_Period3_OUT = datetime.strptime(Period3_OUT, '%H:%M:%S')
        Period4_IN = '11:30:00'
        Obj_Period4_IN = datetime.strptime(Period4_IN, '%H:%M:%S')
        Period4_Allowed = '11:40:00'
        Obj_Period4_Allowed = datetime.strptime(Period4_Allowed, '%H:%M:%S')
        Period4_OUT = '12:20:00'
        Obj_Period4_OUT = datetime.strptime(Period4_OUT, '%H:%M:%S')
        Period5_IN = '12:20:00'
        Obj_Period5_IN = datetime.strptime(Period5_IN, '%H:%M:%S')
        Period5_Allowed = '12:30:00'
        Obj_Period5_Allowed = datetime.strptime(Period5_Allowed, '%H:%M:%S')
        Period5_OUT = '13:20:00'
        Obj_Period5_OUT = datetime.strptime(Period5_OUT, '%H:%M:%S')
        Period6_IN = '13:20:00'
        Obj_Period6_IN = datetime.strptime(Period6_IN, '%H:%M:%S')
        Period6_Allowed = '13:30:00'
        Obj_Period6_Allowed = datetime.strptime(Period6_Allowed, '%H:%M:%S')
        Period6_OUT = '14:10:00'
        Obj_Period6_OUT = datetime.strptime(Period6_OUT, '%H:%M:%S')
        Period7_IN = '14:10:00'
        Obj_Period7_IN = datetime.strptime(Period7_IN, '%H:%M:%S')
        Period7_Allowed = '14:20:00'
        Obj_Period7_Allowed = datetime.strptime(Period7_Allowed, '%H:%M:%S')
        Period7_OUT = '15:00:00'
        Obj_Period7_OUT = datetime.strptime(Period7_OUT, '%H:%M:%S')
        Period8_IN = '15:00:00'
        Obj_Period8_IN = datetime.strptime(Period8_IN, '%H:%M:%S')
        Period8_Allowed = '15:10:00'
        Obj_Period8_Allowed = datetime.strptime(Period8_Allowed, '%H:%M:%S')
        Period8_OUT = '15:50:00'
        Obj_Period8_OUT = datetime.strptime(Period8_OUT, '%H:%M:%S')
        Period9_IN = '15:50:00'
        Obj_Period9_IN = datetime.strptime(Period9_IN, '%H:%M:%S')
        Period9_Allowed = '16:00:00'
        Obj_Period9_Allowed = datetime.strptime(Period9_Allowed, '%H:%M:%S')
        Period9_OUT = '16:40:00'
        Obj_Period9_OUT = datetime.strptime(Period9_OUT, '%H:%M:%S')
        if Obj_Period1_IN >= Obj_W or Obj_W <= Obj_Period1_Allowed:
            if x % 2 == 0:
                if Obj_WX >= Obj_PeriodTime:
                    data["1"] = "P"
                elif len(TIME) > 2:
                    if Obj_Period1_IN <= Obj_Y and Obj_Y <= Obj_Period1_OUT:
                        if Obj_XY >= Obj_PeriodNotAllowed:
                            data["1"] = "A"
                        elif Obj_WXYZ >= Obj_PeriodTime:
                            data["1"] = "P"
                else:
                    data["1"] = "A"
            elif x % 2 != 0:
                data["1"] = "A"
        if Obj_Period2_IN >= Obj_W or Obj_W <= Obj_Period2_Allowed:
            if x % 2 == 0:
                if Obj_WX >= Obj_PeriodTime:
                    data["2"] = "P"
                elif len(TIME) > 2:
                    if Obj_Period2_IN <= Obj_Y and Obj_Y <= Obj_Period2_OUT:
                        if Obj_XY >= Obj_PeriodNotAllowed:
                            data["2"] = "A"
                        elif Obj_WXYZ >= Obj_PeriodTime:
                            data["2"] = "P"
                else:
                    data["2"] = "A"
            elif x % 2 != 0:
                data["2"] = "A"
        if Obj_Period3_IN >= Obj_W or Obj_W <= Obj_Period3_Allowed:
            if x % 2 == 0:
                if Obj_WX >= Obj_PeriodTime:
                    data["3"] = "P"
                elif len(TIME) > 2:
                    if Obj_Period3_IN <= Obj_Y and Obj_Y <= Obj_Period3_OUT:
                        if Obj_XY >= Obj_PeriodNotAllowed:
                           data["3"] = "A"
                        elif Obj_WXYZ >= Obj_PeriodTime:
                           data["3"] = "P"
                else:
                    data["3"] = "A"
            elif x % 2 != 0:
                data["3"] = "A"
        if Obj_Period4_IN >= Obj_W or Obj_W <= Obj_Period4_Allowed:
            if x % 2 == 0:
                if Obj_WX >= Obj_PeriodTime:
                    data["4"] = "P"
                elif len(TIME) > 2:
                    if Obj_Period4_IN <= Obj_Y and Obj_Y <= Obj_Period4_OUT:
                        if Obj_XY >= Obj_PeriodNotAllowed:
                             data["4"] = "A"
                        elif Obj_WXYZ >= Obj_PeriodTime:
                            data["4"] = "P"
                else:
                    data["4"] = "A"
            elif x % 2 != 0:
                data["4"] = "A"
        if Obj_Period5_IN >= Obj_W or Obj_W <= Obj_Period5_Allowed:
            if x % 2 == 0:
                if Obj_WX >= Obj_PeriodTime:
                    data["5"] = "N"
                elif len(TIME) > 2:
                    if Obj_Period5_IN <= Obj_Y and Obj_Y <= Obj_Period5_OUT:
                        if Obj_XY >= Obj_PeriodNotAllowed:
                            data["5"] = "N"
                        elif Obj_WXYZ >= Obj_PeriodTime:
                            data["5"] = "N"
                else:
                    data["5"] = "N"
            elif x % 2 != 0:
                data["5"] = "N"
        if Obj_Period6_IN >= Obj_W or Obj_W <= Obj_Period6_Allowed:
            if x % 2 == 0:
                if Obj_WX >= Obj_PeriodTime:
                    data["6"] = "P"
                elif len(TIME) > 2:
                    if Obj_Period6_IN <= Obj_Y and Obj_Y <= Obj_Period6_OUT:
                        if Obj_XY >= Obj_PeriodNotAllowed:
                            data["6"] = "A"
                        elif Obj_WXYZ >= Obj_PeriodTime:
                            data["6"] = "P"
                else:
                    data["6"] = "A"
            elif x % 2 != 0:
                data["6"] = "A"
        if Obj_Period7_IN >= Obj_W or Obj_W <= Obj_Period7_Allowed:
            if x % 2 == 0:
                if Obj_WX >= Obj_PeriodTime:
                    data["7"] = "P"
                elif len(TIME) > 2:
                    if Obj_Period7_IN <= Obj_Y and Obj_Y <= Obj_Period7_OUT:
                        if Obj_XY >= Obj_PeriodNotAllowed:
                            data["7"] = "A"
                        elif Obj_WXYZ >= Obj_PeriodTime:
                            data["7"] = "P"
                else:
                    data["7"] = "A"
            elif x % 2 != 0:
                data["7"] = "A"
        if Obj_Period8_IN >= Obj_W or Obj_W <= Obj_Period8_Allowed:
            if x % 2 == 0:
                if Obj_WX >= Obj_PeriodTime:
                    data["8"] = "P"
                elif len(TIME) > 2:
                    if Obj_Period8_IN <= Obj_Y and Obj_Y <= Obj_Period8_OUT:
                        if Obj_XY >= Obj_PeriodNotAllowed:
                            data["8"] = "A"
                        elif Obj_WXYZ >= Obj_PeriodTime:
                            data["8"] = "P"
                else:
                    data["8"] = "A"
            elif x % 2 != 0:
                data["8"] = "A"
        if Obj_Period9_IN >= Obj_W or Obj_W <= Obj_Period9_Allowed:
            if x % 2 == 0:
                if Obj_WX >= Obj_PeriodTime:
                    data["9"] = "P"
                elif len(TIME) > 2:
                    if Obj_Period9_IN <= Obj_Y and Obj_Y <= Obj_Period9_OUT:
                        if Obj_XY >= Obj_PeriodNotAllowed:
                           data["9"] = "A"
                        elif Obj_WXYZ >= Obj_PeriodTime:
                           data["9"] = "P"
                else:
                    data["9"] = "A"
            elif x % 2 != 0:
               data["9"] = "A"
        x = x + 1
    now = datetime.now()
    WeekDays = {"0": "Monday", "1": "Tuesday", "2": "Wednesday", "3": "Thursday", "4": "Friday", "5": "Saturday", "6": "Sunday"}
    string = str(datetime.weekday(now))
    Day = WeekDays[string]
    Subjects = "SELECT SubjectNames from timetable where Day = '{}'".format('Monday')
    cursor.execute(Subjects)
    SubjectNames = cursor.fetchall()
    SN = [x[0] for x in SubjectNames]
    y = 0
    for Sub in SN:
        y = y + 1
        if Sub == 'NoClassWork':
            data[str(y)] = 'N'
    i = 0
    for Key in data:
        cursor.execute("SELECT COUNT(*) FROM attendancedata")
        n = cursor.fetchone()
        N = int(n[0])+1
        sql = "INSERT INTO attendancedata(SNO, StudentId, Date, Day, Attendance, PeriodNumber, Subjects) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (N, name, '2022-09-12', 'Monday', data[Key], Key, SN[i])
        cursor.execute(sql, val)
        mydb.commit()
        i = i + 1