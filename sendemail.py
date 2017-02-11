import smtplib

from_name = "Brandon"
to_name = "Jason"
subject = "Smtplib works"
msg = "Hello, World"

from_addr = '@gmail.com'
to_addr = 'david@someemail.com'
message = """From: {} <{}> To: {} <{}>Subject: {} {}"""

message_to_send = message.format(from_name, from_addr, to_name,to_addr, subject, msg)

# Credentials (if needed)
username = '@gmail.com'
password = ''

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()