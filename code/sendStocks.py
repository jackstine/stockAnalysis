from stock.streams.mysql import DB
from stock.models import InsertModel
from stock.repository.nasdaq import NasdaqCompanyListingRepository
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import random,datetime

def getWeb(s):
    return "https://www.google.com/finance?q=" + s.lower() +"&ei=m58UVvGqK8KVmAGtzamwDAa"

db = DB(DB.Connections.STOCK)
repo = NasdaqCompanyListingRepository()
model = repo.selectAll(db)
rows = model.getRows()
symbolField = model.getDictFields()["symbol"]
symbols = []
for r in rows:
    symbols.append(r[symbolField])
symbols = sorted(symbols)
#TODO  need to make Business Logic
cur = db.executeQuery("Select symbol FROM LookedAtStocks")
alreadyHave = []
while(True):
    s = cur.fetchone()
    if (s == None):
        break;
    alreadyHave.append(s[0])
for a in alreadyHave:
    symbols.remove(a)
picked = []
for i in range(0,200):
    r = int(random.random() * len(symbols))
    p = symbols[r]
    picked.append(p)
    symbols.remove(p)
objects = []
for p in picked:
    im = InsertModel("LookedAtStocks")
    im.insert("symbol", p)
    db.insert(im).queue()
    objects.append(p + ","  +getWeb(p))
f = open("stocksLook.txt","w")
for o in objects:
    f.write(o+"\n")
f.close()
#send email to work with file

stockEmailLogin, stockEmailPassword = 'jacobstockprimary@gmail.com', 'stockaholic'
toaddrs = "ecstaticjack@gmail.com"
f = open("stocksLook.txt","r")
outer=MIMEMultipart()
outer['Subject'] = 'report' + str(datetime.datetime.now())
outer['To'] = toaddrs
outer['From'] = stockEmailLogin
outer.preamble = 'THE SERVER IS WORKING HAHA YESSSS!!!\n'
msg=MIMEText(f.read())
msg.add_header('Content-Sisposition','attachment',filename="stocksLook.txt")
outer.attach(msg)
# send it via gmail
s = SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login(stockEmailLogin, stockEmailPassword)
s.sendmail(stockEmailLogin, toaddrs, outer.as_string())
s.quit()
db.commit()
