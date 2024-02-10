def writefile(todotxt):
    with open('files/ToDo.txt', 'w') as newfile:
        newfile.writelines(todotxt)


def showfile():
    for position, task in enumerate(todos):
        print(f'{position + 1}: {task}', end='')


enter_prompt = 'Choose your Action Add, Show, Edit, Remove/Complete, Close/Exit: '

with open('files/ToDo.txt', 'r') as file:
    todos = file.readlines()

print(f'existing todos are:')
showfile()

while True:
    action = input(enter_prompt).strip().upper()

    match action:
        case 'ADD':
            todo = input('Enter a ToDo: ').strip().upper() + '\n'
            todos.append(todo)

            writefile(todos)

        case 'SHOW':
            showfile()

        case 'EDIT':
            ed = int(input(f'Enter the number of ToDo to edit:'))
            todos[ed - 1] = input('Enter a new ToDo: ').strip().upper()

            writefile(todos)

        case 'REMOVE' | 'COMPLETE':
            remC = input(f'Enter a Number or ToDo to be {action}D: ').strip().upper()

            if remC.isnumeric():
                ind = int(remC) - 1
                if ind < len(todos):
                    print(f'{action[:-1]}ING {todos[ind][:-1]}')
                    remC = todos[ind]
                else:
                    print('Enter valid Position')
                    continue

            if remC in todos:
                todos.remove(remC)
                print(f'{remC[:-1]} is {action}D')
            else:
                print('This ToDo does not Exist')

            writefile(todos)

        case 'CLOSE' | 'EXIT':
            break

        case _:
            print('Enter Valid Option')

print('Bye')
