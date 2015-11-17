import imapclient
import pyzmail
import pprint
import smtplib
from email.mime.text import MIMEText

gmail_user = 'enayettinkers@gmail.com'
gmail_password = 'computersaysno'
#smtp stuff for sending email
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
type(smtpObj)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.ehlo()
smtpObj.login(gmail_user, gmail_password)

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

imapObj.login(gmail_user, gmail_password)

#choose search folder
imapObj.select_folder('INBOX', readonly=False)

#search email for string in subject and create UIDs
UIDs = imapObj.search(['SUBJECT "hello friend"', 'UNSEEN'])

#iterate through UIDs
for index in range(len(UIDs)):

	#pass UIDs into rawMessages
	rawMessages = imapObj.fetch(UIDs[index], ['BODY[]'])

	#create a PyzMessage object 
	message = pyzmail.PyzMessage.factory(rawMessages[UIDs[index]]['BODY[]'])

	#returns text version of email
	message.text_part != None
	actualText = message.text_part.get_payload().decode(message.text_part.charset)
	pprint.pprint(actualText)

	#returns email address of sender
	addressRaw = message.get_addresses('from')
	address = addressRaw[0][1]
	pprint.pprint(address)

	#trying to send the mail
	msg = MIMEText(actualText)
	msg['Subject'] = ('suck on this noob')
	msg['From'] = gmail_user
	msg['To'] = address
	smtpObj.sendmail(gmail_user, address, msg.as_string())


imapObj.logout()
smtpObj.quit()

