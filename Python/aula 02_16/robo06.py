import rpa as r
import pyautogui as p

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

r.init()
r.url('https://www.melhorcambio.com/dolar-hoje')
p.sleep(2)

dolar_hoje = r.read('//*[@id="comercial"]')
print(dolar_hoje)
r.close()

texto_email = dolar_hoje + 'hoje' + str(pd.Timestamp('today'))

de = 'andre@zuplae.com'
senha = '*****'
para = 'andregranemann@hotmail.com'

message = MIMEMultipart()
message['From']= de 
message['to'] = para
message['Subject'] = 'Cotacao do dolar hoje ' #Titulo do e-mail

message.attach(MIMEText(texto_email, 'plain'))

session = smtplib.SMTP('smtp.gmail.com', 587)# Usuario do Gmail com porta
session.starttls()#habilitar seguranca
session.login(de, senha)
texto = message.as_string()
session.sendmail(de, para, texto)
session.quit()
