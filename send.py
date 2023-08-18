import win32com.client as win32
import psutil
import os
import subprocess

def send_notification():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'mohamedyosraaaaaaay@gmail.com'
    mail.Subject = 'Sent through Python'
    mail.body = 'This email alert is auto generated. Please do not respond.'
    mail.Send()


# Open Outlook.exe. Path may vary according to system config
# Please check the path to .exe file and update below

def open_outlook():
    try:
        subprocess.call(['C:\Program Files (x86)\Microsoft Office\Office14\Outlook.exe'])
        os.system("C:\Program Files (x86)\Microsoft Office\Office14\Outlook.exe");
    except:
        print("Outlook didn't open successfully")

# Checking if outlook is already opened. If not, open Outlook.exe and send email
for item in psutil.pids():
    p = psutil.Process(item)
    if p.name() == "OUTLOOK.EXE":
        flag = 1
        break
    else:
        flag = 0

if (flag == 1):
    send_notification()
else:
    open_outlook()
    send_notification()