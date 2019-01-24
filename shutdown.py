import os, platform
from datetime import datetime

def desligar(tempo):
    if platform.system() == 'Windows':
        comando = 'shutdown -s -t ' + str(tempo)
        return os.system(comando)
    elif platform.system() == 'Linux':
        comando = 'shutdown -h ' + str(tempo)
        return os.system(comando)
    else:
        return 'Sistema Operacional desconhecido!'

def cancelar():
    if platform.system() == 'Windows':
        return os.system('shutdown /a')
    elif platform.system() == 'Linux':
        return os.system('shutdown -c')
    else:
        return 'Sistema operacional desconhecido!'

def horaDesligar(hora,minuto):
    desligar = '{}:{}'.format(hora,minuto)
    hora_desligar = datetime.strptime(desligar, '%H:%M')

    atual = datetime.now()
    atual = atual.strftime('%H:%M')
    hora_atual = datetime.strptime(atual, '%H:%M')

    if hora_atual < hora_desligar:
        segundos = abs((hora_desligar - hora_atual).seconds)
        return segundos
    else:
        return 'xxx'