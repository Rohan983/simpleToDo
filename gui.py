import time
import functions
import PySimpleGUI as sg
import os


def alert(ev):
    sg.popup(f"Select a ToDo to {ev}", font=('Helvetica', 20))


if not os.path.exists('ToDo.txt'):
    with open("ToDo.txt", 'w') as file:
        pass

sg.theme("Black")

clock = sg.Text(key = 'Clock')
add_label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-DO", key= 'todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.readfile(), key= 'todotxt',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button('Complete')
exit_button = sg.Button("Exit")

layout = [[clock],
          [add_label],
          [input_box, add_button],
          [list_box, edit_button, complete_button], [exit_button]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['Clock'].update(value = time.strftime("It is %b %d, %Y %H:%M:%S"))

    match event:
        case 'Add':
            todos = functions.readfile()
            if values.get('todo'):
                todos.append(values.get('todo') + "\n")
                functions.writefile(todos)
                window['todotxt'].update(values=todos)
                window['todo'].update("")
            else:
                sg.popup(f"Enter ToDo in Text box", font=('Helvetica', 20))

        case 'Edit':
            try:
                todos = functions.readfile()
                ind = todos.index(values.get('todotxt')[0])
                todos[ind] = values.get('todo')
                functions.writefile(todos)
                window['todotxt'].update(values=todos)
                window['todo'].update("")

            except IndexError:
                alert('Edit')

        case 'todotxt':
            try:
                window['todo'].update(value=values.get('todotxt')[0])
            except IndexError:
                pass

        case 'Complete':
            todos = functions.readfile()
            try:
                todos.remove(values.get('todotxt')[0])
                functions.writefile(todos)
                window['todotxt'].update(values=todos)
                window['todo'].update("")
            except IndexError:
                alert('Complete')

        case 'Exit':
            print("*** Exiting ***")
            break

        case sg.WIN_CLOSED:
            break

window.close()