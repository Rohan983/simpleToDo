def writefile(fp, todotxt):
    with open(fp, 'w') as newfile:
        newfile.writelines(todotxt)


def showtodo(tdl):
    for position, task in enumerate(tdl):
        print(f'{position + 1}: {task}', end='')


def remaction(st, ln):
    return st[ln:]


enter_prompt = 'Choose your Action Add, Show, Edit, Complete, Clear, Exit: '

filepath = "files/ToDo.txt"

with open(filepath, 'r') as file:
    todos = file.readlines()

print(f'existing todos are:')
showtodo(todos)

while True:
    action = input(enter_prompt).strip().upper()

    if action.startswith('ADD'):
        todo = remaction(action, 3).strip().upper() + '\n'
        todos.append(todo)
        writefile(filepath, todos)

    elif action == 'SHOW':
        showtodo(todos)

    elif action.startswith('EDIT'):
        try:
            ed = int(remaction(action, 4).strip().upper())
            todos[ed - 1] = input('Enter a new ToDo: ').strip().upper() + '\n'
            writefile(filepath, todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif action.startswith('COMPLETE'):
        remC = remaction(action, 8).strip().upper()

        if remC.isnumeric():
            ind = int(remC) - 1
            try:
                print(f'COMPLETING {todos[ind][:-1]}')
                remC = todos[ind][:-1]
            except IndexError:
                print('Enter valid Position')
                continue

        remC += '\n'
        if remC in todos:
            todos.remove(remC)
            print(f'{remC[:-1]} is COMPLETED')
        else:
            print('This ToDo does not Exist')

        writefile(filepath, todos)

    elif action == 'CLEAR':
        todos = []

    elif action == 'EXIT':
        break

    else:
        print('Enter Valid Option')

print('Bye')
