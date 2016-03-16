from googlevoice import Voice
from . import Config

def textMe(message):
    v = getPhone()
    v.text(message)
    v.logout()

def getPhone():
    return Phone()

class Phone:
    def __init__(self, email=None, passwd=None):
        self.v = Voice()
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
