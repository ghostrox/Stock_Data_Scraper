import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "SenderAddress"
toaddr = "RecieverAddress"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Add Subject"

body = "Add Body"

msg.attach(MIMEText(body, 'plain'))

filename = "Stock_Data.csv OR Price_Summary.csv"
attachment = open("/Path/to/.csv", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "AddYourPassword")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()