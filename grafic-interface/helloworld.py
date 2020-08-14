import PySimpleGUI as sg
from json import load, dumps
from sys import exit


class Screen():

    def __init__(self):
        self.path = "tools.json"
        self.theme = sg.theme('TealMono')
        self.layout = [
            [sg.Text("Tool name: ")],
            [sg.Input(size=(20, 0), key="nameTool")],
            [sg.Text("Description tool: ")],
            [sg.Input(size=(30, 0), key="descriptionTool")],
            [sg.Text("Paste a useful link: ")],
            [sg.Input(size=(20, 0), key="links")],
            [sg.Button('Save'), sg.Button("Cancel")]
        ]

    def create_tool(self, event, object_tool: dict):

        with open(self.path) as tools_json:
            arquive_json = load(tools_json)

            arquive_json.append(object_tool)
            
            if event == sg.WIN_CLOSED or event == "Cancel":
                exit(1)

            with open(self.path, "w") as new_arquive:
                new_arquive.write(dumps(arquive_json))
                sg.popup("Saved tool!", text_color="green")

    def start_screen(self):
        window = sg.Window('Help Dev - Save Tool').layout(self.layout)
        event, tool = window.read()
        self.create_tool(event=event, object_tool=tool)

        window.close()


Screen().start_screen()
