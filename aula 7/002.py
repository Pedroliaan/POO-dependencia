
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
   [sg.Text('Usuário'),sg.Input(key='usuario',size=(20,1))],
   [sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(20,1))],
   [sg.Button('Entrar')]
]

janela = sg.Window('Tela de Login', layout)

while True:
   eventos, valores = janela.read()
   if eventos == 'Entrar':
       if valores['usuario'] == 'internacional' and valores['senha'] == '123456':
           print('Senha Correta!!!')
       else:
           print('Senha Errada!!!')


