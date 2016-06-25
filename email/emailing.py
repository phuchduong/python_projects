from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

user_name = ''
user_password = ''

from_address = ''
to_address = ''

msg = MIMEMultipart('alternative')
msg['Subject'] = "hi"
msg['From'] = user_name
msg['To'] = user_password

text = "My name is " + user_name + "."
html = """\
<html>
    <head></head>
    <body>
        <p>Hi!<br>
        How are you?<br>
        </p>
    </body>
</html>
"""

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

email_server = 'smtp.office365.com'
email_port = 578
email_client = smtplib.SMTP(email_server, email_port)
email_client.set_debuglevel(1)
email_client.ehlo()
email_client.starttls()
email_client.login(user_name, user_password)
email_client.sendemail(from_address, to_address, msg.as_string())
email_client.quit()
