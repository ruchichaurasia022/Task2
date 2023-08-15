import random
import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
password="mipvpyxhbzmrevty"
server.login("ruchich0945@gmail.com",password)
otp=''.join([str(random.randint(0,9)) for i in range(4)])
msg='Hello, Your OTP is '+str(otp)
sender='ruchich0945@gmail.com'
receiver='rc20000000002@gmail.com'

server.sendmail(sender,receiver,msg)
server.quit()
