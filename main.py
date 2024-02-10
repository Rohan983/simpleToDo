def writefile(todotxt):
    with open('files/ToDo.txt', 'w') as newfile:
        newfile.writelines(todotxt)


def showfile():
    for position, task in enumerate(todos):
        print(f'{position + 1}: {task}', end='')


def remaction(st, ln):
    return st[ln:]


enter_prompt = 'Choose your Action Add, Show, Edit, Complete, Exit: '

with open('files/ToDo.txt', 'r') as file:
    todos = file.readlines()

print(f'existing todos are:')
showfile()

while True:
    action = input(enter_prompt).strip().upper()

    if action.startswith('ADD'):
        todo = remaction(action, 3).strip().upper() + '\n'
        todos.append(todo)
        writefile(todos)

    elif action == 'SHOW':
        showfile()

    elif action.startswith('EDIT'):
        ed = int(remaction(action, 4).strip().upper())
        todos[ed - 1] = input('Enter a new ToDo: ').strip().upper() + '\n'

        writefile(todos)

    elif action.startswith('COMPLETE'):
        remC = remaction(action, 8).strip().upper()

        if remC.isnumeric():
            ind = int(remC) - 1
            if ind < len(todos):
                print(f'COMPLETING {todos[ind][:-1]}')
                remC = todos[ind]
            else:
                print('Enter valid Position')
                continue
        remC += '\n'
        if remC in todos:
            todos.remove(remC)
            print(f'{remC[:-1]} is COMPLETED')
        else:
            print('This ToDo does not Exist')

        writefile(todos)

    elif action == 'EXIT':
        break

    else:
        print('Enter Valid Option')

print('Bye')
