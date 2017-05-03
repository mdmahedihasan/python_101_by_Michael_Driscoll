import smtplib


HOST = "mySMTP.server.com"
SUBJECT = "Test email from python"
TO = "mahedi@someaddress.org"
FROM = "python@mydomain.com"
text = "python 3.6 rules them all"

BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
))

server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()