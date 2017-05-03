import os
import smtplib
import sys


from configparser import ConfigParser


def send_email(subject, body_text, to_emails, cc_emails, bcc_emails):
    """
    send an email
    :param subject: 
    :param to_addr: 
    :param body_text: 
    :return: 
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")

    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config not found. Exiting!")
        sys.exit(1)

    host = cfg.get("smtp", "server")
    from_addr = cfg.get("smtp", "from_addr")

    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % ', '.join(to_emails),
        "CC: %s" % ', '.join(cc_emails),
        "BCC: %s" % ', '.join(bcc_emails),
        "Subject: %s" % subject,
        "",
        body_text
    ))

    emails = to_emails + cc_emails + bcc_emails

    server = smtplib.SMTP(host)
    server.sendmail(from_addr, emails, BODY)
    server.quit()


if __name__ == '__main__':
    subject = ''
    emails = ''
    cc_emails = ''
    bcc_emails = ''
    body_text = ''
    send_email(subject, body_text, emails, cc_emails, bcc_emails)