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

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("kums519@gmail.com","Google@567")
mail_list=["sk4641230@gmail.com","ksum257@gmail.com"]
 
while True:
    hr=time.localtime()[3]
    mint=time.localtime()[4]
    sec=time.localtime()[5]
    day=time.localtime()[6]
    print("{hr} : {min} : {sec}".format(hr=hr,min=mint,sec=sec))
    while hr==17 and mint==21 and sec<10:
        for mail in mail_list:
            server.sendmail("kums519@gmail.com", mail, message)
        print("done sending notification.")
        time.sleep(10)
        break
    time.sleep(1)
