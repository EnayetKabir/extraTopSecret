import imapclient
import pyzmail
import pprint

gmail_user = 'enayettinkers@gmail.com'
gmail_password = 'computersaysno'

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

imapObj.login(gmail_user, gmail_password)

#choose search folder
imapObj.select_folder('INBOX', readonly=False)

#search email for string in subject and create UIDs
UIDs = imapObj.search(['SUBJECT "hello friend"'])


#iterate through UIDs
for index in range(len(UIDs)):

#pass UIDs into rawMessages
	rawMessages = imapObj.fetch(UIDs[index], ['BODY[]'])

#create a PyzMessage object 
	message = pyzmail.PyzMessage.factory(rawMessages[UIDs[index]]['BODY[]'])

#returns text version of email
	message.text_part != None
	pprint.pprint(message.text_part.get_payload().decode(message.text_part.charset))
#returns html version of email
	#message.html_part != None
	#message.html_part.get_payload().decode(message.html_part.charset)

imapObj.logout()

