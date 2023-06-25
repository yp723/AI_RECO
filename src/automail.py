import yagmail
import os
import datetime
date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
yag = yagmail.SMTP("sparkvers@email.com", "ylfxeegirdaauiod")


yag.send(
    to=receiver,
    subject=sub,
    contents=body,
    attachments= filename
)
print("Email Sent!")
