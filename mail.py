import smtplib, os
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.outlook.com', 587)

server.ehlo()

server.starttls()

server.login(os.environ.get('EMAIL'), os.environ.get('PASSWORD'))

# creating a message 

msg = MIMEMultipart()
msg['From'] = 'Farid Isayev'
msg['To'] = 'faridisayev3@icloud.com'
msg['Subject'] = 'Testing'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

# opening in read byte mode 

attachment = open('cutedog.jpg', 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename=cutedog.jpg')
msg.attach(p)

text = msg.as_string()
server.sendmail(os.environ.get('EMAIL'), 'faridisayev3@icloud.com', text)
