'''
Created on 05-Feb-2021

@author: sk464
'''
message = """From: Sumit <from@fromdomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Timesheet Remainder

Please fill your timesheet. :)<br>
Good day!
"""
import smtplib
import time

hr=time.localtime()[3]
day=time.localtime()[6]
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("kums519@gmail.com","Google@567")
mail_list=["sk4641230@gmail.com","ksum257@gmail.com"]
for id in mail_list:
    server.sendmail("kums519@gmail.com", id, message)
server.close()
print("done.")