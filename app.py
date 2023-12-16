import PySimpleGUI as sg
from time import strftime

def atualizar_relogio():
    while True:
        event, values = window.read(timeout=1000)  # Atualize a cada 1000ms (1 segundo)
        if event == sg.WIN_CLOSED:
            break
        hora_atual = strftime("%H:%M:%S %p")
        window['-HORA-'].update(hora_atual)

sg.theme('DarkBlue3')

layout = [
    [sg.Text('', size=(15, 1), font=('Helvetica', 20), key='-HORA-')],
    [sg.Button('Sair')]
]

window = sg.Window('Relógio', layout, finalize=True)

atualizar_relogio()

window.close()

