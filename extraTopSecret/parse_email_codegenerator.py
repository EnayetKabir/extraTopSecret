APPLICATION_ID = "GyUfmGoQbBBvBCKyH9r7qGK1GgWo6kYKLdi4MPjA"
REST_API_KEY = "SmoaTb8g7ld84iheL13k568C7pT1ybPJjOJc0set"

import random
import string

from parse_rest.connection import register
# Alias the Object type to make clear is not a normal python Object
from parse_rest.datatypes import Object
#first register the app
register(APPLICATION_ID, REST_API_KEY)

#email dependencies
import imapclient
import pyzmail
import pprint
import smtplib
from email.mime.text import MIMEText

#---------------------------------------------------------------------------------

gmail_user = 'enayettinkers@gmail.com'
gmail_password = 'computersaysno'
#smtp stuff for sending email
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
type(smtpObj)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.ehlo()
smtpObj.login(gmail_user, gmail_password)

#creatae IMAP object
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

imapObj.login(gmail_user, gmail_password)

#---------------------------------------------------------------------------------

#choose search folder
imapObj.select_folder('INBOX', readonly=False)

#search email for string in subject and create UIDs
UIDs = imapObj.search(['SUBJECT "gimmegimme"', 'UNSEEN'])

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

	#--------------------------------------------------------

	#define a Python class that inherts from parse_rest.datatypes.Object
	class passcodes(Object):
   		pass

	#creating Object subclass by string name
	objectName = "nextString"
	myObject = Object.factory(objectName)

	#generate random code for user
	code4u = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(17)])
	pprint.pprint(code4u);

	#instantiate new class with some parameters
	newRow = passcodes(passcode=code4u, numOfUses=0, emailAddress=address)

	#save our new object, by calling the save() method
	newRow.save()

	#--------------------------------------------------------

	#trying to send the email
	msg = MIMEText(code4u)
	msg['Subject'] = ('checkit')
	msg['From'] = gmail_user
	msg['To'] = address
	smtpObj.sendmail(gmail_user, address, msg.as_string())

	#--------------------------------------------------------




imapObj.logout()
smtpObj.quit()

