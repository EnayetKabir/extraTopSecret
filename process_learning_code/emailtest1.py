import smtplib

gmail_user = 'enayettinkers@gmail.com'
gmail_password = 'computersaysno'

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
type(smtpObj)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.ehlo()
smtpObj.login(gmail_user, gmail_password)

#send the email
smtpObj.sendmail(gmail_user, gmail_user, 'Subject: this works \nIt is super chill dude')

#disconnect from the server
smtpObj.quit()