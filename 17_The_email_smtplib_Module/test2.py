import smtplib


def send_email(host, subject, to_addr, from_addr, body_text):
    """
    send an email
    :param host: 
    :param subject: 
    :param to_addr: 
    :param from_addr: 
    :param body_text: 
    :return: 
    """
    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to_addr,
        "Subject: %s" % subject,
        "",
        body_text
    ))

    server = smtplib.SMTP(host)
    server.sendmail(from_addr, [to_addr], body_text)
    server.quit()


if __name__ == '__main__':
    host = ''
    subject = ''
    to_addr = ''
    from_addr = ''
    body_text = ''
    send_email(host, subject, to_addr, from_addr, body_text)