#this is an example email that adds an attachement, but it doesnt send.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Added
from email.mime.image import MIMEImage

attachment = 'plot.png'

msg = MIMEMultipart()
msg["To"] = 'lindsmeyers@gmail.com'
msg["From"] = 'yolindsysnotifications@gmail.com'
msg["Subject"] = 'Buy stock today'

msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % ('check this out', attachment), 'html')  
msg.attach(msgText)   # Added, and edited the previous line

fp = open(attachment, 'rb')                                                    
img = MIMEImage(fp.read())
fp.close()
img.add_header('Content-ID', '<{}>'.format(attachment))
msg.attach(img)

print (msg.as_string())
exit(0)