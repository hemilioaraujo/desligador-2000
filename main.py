from tkinter import *
from shutdown import cancelar, horaDesligar, desligar

h = 0
m = 0
step = 1

def bt_hora_mais():
    global h, step
    if h < 23 and (h + step) <= 23:
        h += step
    elif h == 23:
        h = 0
    lb_hora['text'] = str(h)

def bt_hora_menos():
    global h, step
    if h > 0 and (h - step) >= 0:
        h -= step
    elif h == 0:
        h = 23
    lb_hora['text'] = str(h)

def bt_minuto_mais():
    global m, step
    if m < 59 and (m + step) <= 59:
        m += step
    elif m == 59:
        m = 0
    lb_minuto['text'] = str(m)

def bt_minuto_menos():
    global m, step
    if m > 0 and (m - step) >= 0:
        m -= step
    elif m == 0:
        m = 59
    lb_minuto['text'] = str(m)

def bt_confirma():
    global h, m
    a = horaDesligar(h, m)

    if a != 'xxx':
        desligar(a)
        lb_status['text'] = 'Desligamento programado!'
    else:
        lb_status['text'] = 'Hora menor que a atual!'

    pass

def bt_cancela():
    cancelar()
    lb_status['text'] = 'Desligamento cancelado!'
    pass

def rb_1_step():
    global step
    step = 1

def rb_5_step():
    global step
    step = 5

def rb_10_step():
    global step
    step = 10

y_lb_horario, y_bot_ajuste, y_lb_step, y_radiobutton, y_lb_status, y_bt_aplica = 10, 40, 80, 100, 130,160

janela = Tk()

janela.title('Shutdown Programmer')
janela.geometry('300x200+100+100')

lb_hora = Label(janela, text = '0')
lb_hora.place(x=105,y=y_lb_horario)

lb_minuto = Label(janela, text = '0')
lb_minuto.place(x=175,y=y_lb_horario)

lb_step = Label(janela, text='Step')
lb_step.place(x=140,y=y_lb_step)

lb_status = Label(janela)
lb_status.place(x=90, y=y_lb_status)

#BOTÃO HORA +
bt_hora_mais = Button(janela, width = 2, text = '+', command=bt_hora_mais)
bt_hora_mais.place(x=90,y=y_bot_ajuste)

#BOTÃO HORA -
bt_hora_menos = Button(janela, width = 2, text = '-', command=bt_hora_menos)
bt_hora_menos.place(x=120,y=y_bot_ajuste)

#BOTÃO MINUTO +
bt_minuto_mais = Button(janela, width = 2, text = '+', command=bt_minuto_mais)
bt_minuto_mais.place(x=160,y=y_bot_ajuste)

#BOTÃO MINUTO -
bt_minuto_menos = Button(janela, width = 2, text = '-', command=bt_minuto_menos)
bt_minuto_menos.place(x=190,y=y_bot_ajuste)

#BOTÃO CONFIRMA
bt_confirma = Button(janela, width = 10, text = 'Confirma', command=bt_confirma)
bt_confirma.place(x=170,y=y_bt_aplica)

#BOTÃO CANCELA
bt_cancela = Button(janela, width = 10, text = 'Cancela', command=bt_cancela)
bt_cancela.place(x=40,y=y_bt_aplica)

#RADIO BUTTON 1
rb_1 = Radiobutton(janela, text = '1',value = 1, command = rb_1_step)
rb_1.place(x=110, y=y_radiobutton)
#RADIO BUTTON 5
rb_5 = Radiobutton(janela, text = '5',value = 2, command = rb_5_step)
rb_5.place(x=140, y=y_radiobutton)
#RADIO BUTTON 10
rb_10 = Radiobutton(janela, text = '10',value = 3, command = rb_10_step)
rb_10.place(x=170, y=y_radiobutton)

janela.mainloop()