import os
import smtplib
from email.message import EmailMessage
import PySimpleGUI as sg

#   Janela
layout = [
    [sg.Text('Seu email: '), sg.Input(key='email')],
    [sg.Text('Sua senha: '), sg.Input(key='senha',password_char='*')],
    [sg.Text('Email do alvo: '),sg.Input(key='alvo')],
    [sg.Text('Mensagem:')],
    [sg.Input(key='mensagem')],
    [sg.Button('Enviar')]
]
janela = sg.Window('Enviar emais', layout) 

while True:
    evento, values = janela.read()
    if evento == sg.WINDOW_CLOSED:
        emails = 0
        break
    if evento == 'Enviar':
        #   Informações do alvo
        ALVO_ADDRESS = values['alvo']
        ALVO_MESSAGE = values['mensagem']

        #   Informações email | MEU
        EMAIL_ADDRESS = values['email']
        EMAIL_PASSWORD = values['senha']

        #   Criar o e-mail
        msg = EmailMessage()
        msg['Subject'] = 'Email do josé'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ALVO_ADDRESS
        msg.set_content(ALVO_MESSAGE)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print(f'\n| Seu endereço: {EMAIL_ADDRESS}')
            print(f'| Mensagem enviada: {ALVO_MESSAGE}\n\n')
            print('| Email enviado com sucesso.')
            print('---' * 20)

janela.close()
