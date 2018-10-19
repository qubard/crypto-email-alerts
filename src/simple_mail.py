import smtplib
import config

from email.message import EmailMessage

class SimpleEmailMessage:

    def __init__(self, dst):
        self.src = config.email_user
        self.dst = dst

    def setSubject(self, subject):
        self.subject = subject
        return self

    """
    Send an e-mail with the message
    return true if the message sent was validated
    """
    def sendMessage(self, message):
        if self.subject is None:
            return False

        msg = EmailMessage()
        msg.set_content(message)

        msg['Subject'] = self.subject
        msg['From'] = self.src
        msg['To'] = self.dst

        try:
            s = smtplib.SMTP_SSL(config.email_smtp, 465)
            s.login(config.email_user, config.email_pass)
            s.send_message(msg)
            s.quit()
        except:
            return False

        return True
