import PySimpleGUI as sg

sg.theme('TealMono') # Add a touch of color
# All the stuff inside your window.
# layout = [  [sg.Text('Some text on Row 1')],
#             [sg.Text('Enter something on Row 2'), sg.InputText()],
#             [sg.Button('Ok'), sg.Button('Cancel')] ]

layout = [
    [sg.Text("Tool name: ")],
    [sg.InputText(size=(36,20),key="nome")],
    [sg.Text("Description Tool: "), sg.InputText()],
    [sg.Text("Paste links: "), sg.InputText()],
    [sg.Button("Save"), sg.Button("Cancel")],
]


# Create the Window
window = sg.Window('Save Tools', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values)

window.close()