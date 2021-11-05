#working auto email that sends with attachment

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import matplotlib.image
import json
with open("/home/yolindsay/stonks-code/trading_algos/coin_dict.json") as file:
    coin_dict = json.load(file)
#email_attachment = matplotlib.image.imread('plot.png')
#list of attachments


# attachments = []
# for user, coins in coin_dict.items():
#     for coin in coins:
#         image = (coin+'plot.png')
#         attachments.append(image)

print(attachments)

#Email Account
email_sender_account = "yolindsysnotifications@gmail.com"
email_sender_username = "yolindsysnotifications@gmail.com"
email_sender_password = "Edgemont74"
email_smtp_server = "smtp.gmail.com"
email_smtp_port = 587
#Email Content
email_recepients = ["lindsmeyers@gmail.com","lunas4734@gmail.com"]
email_subject = "Stock Purchase or Sell Today"
email_body = "you need to buy stock today" 
#
attachment = 'plot.png'

msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % (email_body, attachment), 'html')



#login to email server
server = smtplib.SMTP(email_smtp_server, email_smtp_port)
server.starttls()
server.login(email_sender_username, email_sender_password)

#for loop, sending emails to all recipients
for recipient in email_recepients:
    print(f"Sending email to {recipient}")
    message = MIMEMultipart('alternative')
    message['From'] = email_sender_account
    message['To'] = recipient
    message['Subject'] = email_subject
    message.attach(msgText)
    fp = open(attachment, 'rb')                                                    
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<{}>'.format(attachment))
    message.attach(img)
    text = message.as_string()
    server.sendmail(email_sender_account, recipient, text)
    
#All emails sent, log out.
print(message.as_string())
server.quit()