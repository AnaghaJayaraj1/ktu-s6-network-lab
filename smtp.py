import smtplib

to='abc@gmail.com'
frm='mno@gmail.com'
pwd='******'
sm=smtplib.SMTP_SSL('smtp.gmail.com',465)
sm.login(frm,pwd)
header='To: '+to+'\nFrom: '+frm+'\nSubject: Test mail\n'
content="This is a test mail .. "
print(header)
msg=header+content
sm.sendmail(frm,to,msg)
