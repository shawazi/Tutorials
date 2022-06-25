import smtplib, ssl

# email spammer

me = "waz"
email = "shawazisonfire@gmail.com"
password = "080194Si1"
message = "Is this a real business?"
reciever = "shawazisonfire@gmail.com"
port = 465
sslcontext = ssl.create_default_context()
connection = smtplib.SMTP_SSL("smtp.gmail.com", port, context=sslcontext)
connection.login(email, password)
connection.sendmail(email, reciever, message)
print("Email sent!")

# disable 2fa 