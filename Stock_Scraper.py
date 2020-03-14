#Summary Of Data:
import requests
from bs4 import BeautifulSoup
import pandas as pd 

labels = []
data = []

url = 'https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch'

request = requests.get(url)
response = request.status_code
if response == 200:
    pass
else:
    print('Server responded with', response)
soup = BeautifulSoup(request.content,'html.parser')
table = soup.find('div',id='quote-summary')
rows = table.find_all('tr')
for row in rows:
    labels.append(str(row.find_all('td')[0].text))
    data.append(str(row.find_all('td')[1].text))
cols = {'Field':labels,'Data':data}
df = pd.DataFrame(cols)

#print(labels)
#print(data)
#print(df)

df.to_csv('Price_Summary.csv')'''

#Historical Data:
'''import pandas as pd
import requests
from bs4 import BeautifulSoup

Date = []
Open = []
High = []
Low = []
Close = []
Adj_Close = []
Volume = []

url = 'https://finance.yahoo.com/quote/TSLA/history?p=TSLA'

request = requests.get(url)
response = request.status_code
if response == 200:
    pass
else:
    print('Server responded with', response)
soup = BeautifulSoup(request.content,'html.parser')
table = soup.find('table',class_='W(100%) M(0)')
rows = table.find_all('tr',class_='BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)')
for row in rows:
    Date.append(str(row.find_all('span')[0].text))
    Open.append(str(row.find_all('span')[1].text))
    High.append(str(row.find_all('span')[2].text))
    Low.append(str(row.find_all('span')[3].text))
    Close.append(str(row.find_all('span')[4].text))
    Adj_Close.append(str(row.find_all('span')[5].text))
    Volume.append(str(row.find_all('span')[6].text))

cols = {'Date':Date,'Open':Open,'High':High,'Low':Low,'Close':Close,'Adj Close':Adj_Close,'Volume':Volume}
df = pd.DataFrame(cols)

#print(df)

df.to_csv('Stock_Data.csv')

#Sending CSV To an Email:

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "brocklesnarchokes@gmail.com"
toaddr = "rishavnandi2@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SENDING ATTACHMENTS WITH PYTHON"

body = "Sent With Python"

msg.attach(MIMEText(body, 'plain'))

filename = "Stock_Data.csv"
attachment = open("/Users/rishav/Desktop/Python_Projects/Stock_Data.csv", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "brockf5lesnar")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()