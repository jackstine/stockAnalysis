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

def sendText(message):
    stockEmailLogin, stockEmailPassword = 'jacobstockprimary@gmail.com', 'stockaholic'
    toaddrs = "8503616563@vtext.com"
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