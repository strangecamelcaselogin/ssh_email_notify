import smtplib


def notify(server_account, target, message):
    server, login, password = server_account
    
    msgbox = smtplib.SMTP_SSL(server)
    msgbox.login(login, password)
    msgbox.sendmail(login, target, message)
    msgbox.quit()


if __name__ == '__main__':
    smtp_server = ''  # as example smtp.yandex.ru:465
    sender = ''       # sender email
    password = ''     # password
    
    server_account = (smtp_server, sender, password)

    target = ''  # target email

    subject = ''
    body = ''
    message = """From: {0}\r\nTo: {1}\r\nSubject: {2}\r\n\r\n{3}""".format(sender, target, subject, body)

    notify(server_account, target, message)
