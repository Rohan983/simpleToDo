import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-DO", key= 'todo')
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.readfile()
            todos.append(values.get('todo') + "\n")
            functions.writefile(todos)

        case sg.WIN_CLOSED:
            break

window.close()