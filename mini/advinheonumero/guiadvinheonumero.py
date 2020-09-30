import PySimpleGUI as sg
import random

class Screen:
    def __init__(self):
        self.layout = [
            [sg.Text("Chute um numero de 1 a 10: ")],
            [sg.Input(do_not_clear=False)],
            [sg.Button("Tentar")]
        ]
        self.random_number = random.randint(1, 10)
    def __call__(self):
        window = sg.Window("Advinhe o numero", self.layout)
        showPopup = False
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "Tentar":
                acertou = int(values[0]) == self.random_number
                if acertou:
                    showPopup = True
                    break

        window.close()
        if showPopup:
            sg.popup(f"Acertou: {self.random_number}")


Screen()()