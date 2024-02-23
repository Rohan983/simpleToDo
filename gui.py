import functions
import PySimpleGUI as sg

add_label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-DO", key= 'todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.readfile(), key= 'todotxt',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[add_label],
                           [input_box, add_button],
                           [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.readfile()
            todos.append(values.get('todo') + "\n")
            functions.writefile(todos)
            window['todotxt'].update(values=todos)

        case 'Edit':
            todos = functions.readfile()
            ind = todos.index(values.get('todotxt')[0])
            todos[ind] = values.get('todo') + "\n"
            functions.writefile(todos)
            window['todotxt'].update(values=todos)

        case 'todotxt':
            window['todo'].update(value=values.get('todotxt')[0])

        case sg.WIN_CLOSED:
            break

window.close()