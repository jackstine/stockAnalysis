# from googlevoice import Voice
from . import Config

def textMe(message):
    v = getPhone()
    v.text(message)
    v.logout()

def getPhone():
    return Phone()

class Phone:
    def __init__(self, email=None, passwd=None):
        self.v = None #Voice()
        if (email==None):
            self.v.login(Config.email, Config.email_passwd)
        else:
            self.v.login(email, passwd)

    def text(self, message, phoneNumber=None):
        if (phoneNumber == None):
            self.v.send_sms(Config.phoneNumber, message)
        else:
            self.v.send_sms(phoneNumber, message)

    def logout(self):
        self.v.logout()

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import datetime

def sendEmail(message):
    stockEmailLogin, stockEmailPassword = 'jacobstockprimary@gmail.com', 'stockaholic'
    toaddrs = "ecstaticjack@gmail.com"
    outer=MIMEMultipart()
    outer['Subject'] = 'report' + str(datetime.datetime.now())
    outer['To'] = toaddrs
    outer['From'] = stockEmailLogin
    outer.preamble = 'THE SERVER IS WORKING HAHA YESSSS!!!\n'
    msg=MIMEText(message)
    outer.attach(msg)
    # send it via gmail
    s = SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(stockEmailLogin, stockEmailPassword)
    s.sendmail(stockEmailLogin, toaddrs, outer.as_string())
    s.quit()