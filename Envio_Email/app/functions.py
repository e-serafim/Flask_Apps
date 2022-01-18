from flask import render_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
import os

def manda_email(para, name):
    try:
        msg = MIMEMultipart()
        #-------------------------------------------
        #Informações do server, login e senha
        server = smtplib.SMTP('smtp.ethereal.email: 587')
        msg['From'] = "maritza.zieme3@ethereal.email" #e-mail criado em ethereal.email
        password = "g5tkMf7KN1J3UhMJHc"
        #-------------------------------------------
        msg['To'] = para
        msg['Subject'] = "Bem-vindo! Isso é um teste!"

        # Corpo principal do email (tb um anexo)
        # body = MIMEText("""Olá, segue o arquivo teste em anexo!""", 'plain') # Apenas texto, passar como plain
        body = MIMEText(render_template('mail.html', name=name),'html') # Usar o render_template é um opção, passar como html
        msg.attach(body)

        # Anexando o arquivo
        filename=os.path.join(os.getcwd(),'app','files','teste.txt')
        fp=open(filename,'rb')
        anexo = MIMEApplication(fp.read(),_subtype="txt")
        fp.close()
        filename_on_email='teste.txt'
        anexo.add_header('Content-Disposition','attachment',filename=filename_on_email)
        msg.attach(anexo)

        #Starta o server
        server.starttls()
        #Loga no server
        server.login(msg['From'], password)
        #Manda o email
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        #Sai do server
        server.quit()
        return True
    except:
        return False