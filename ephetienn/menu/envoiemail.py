
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def envoi(expediteur, subject, message):

    msg = MIMEMultipart()
    msg['From'] = expediteur
    msg['To'] = 'ephetiennetest@gmail.com'
    msg['Subject'] = subject + " - de -  " + expediteur
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('ephetiennetest@gmail.com', 'Ephet_RP003')
    mailserver.sendmail(expediteur, 'ephetiennetest@gmail.com', msg.as_string())
    mailserver.quit()

def envoiCopie(to, subject, message):
    msg = MIMEMultipart()
    msg['From'] = 'ephetiennetest@gmail.com'
    msg['To'] = to
    msg['Subject'] = 'copie de votre message - ' + subject
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('ephetiennetest@gmail.com', 'Ephet_RP003')
    mailserver.sendmail('ephetiennetest@gmail.com', to, msg.as_string())
    mailserver.quit()



