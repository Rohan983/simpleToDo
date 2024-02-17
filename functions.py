FILEPATH = "files/ToDo.txt"


def readfile(fp=FILEPATH):
    """
    Reads the text file and returns the list of ToDo items
    """
    with open(fp, 'r') as file:
        tdl = file.readlines()
    return tdl


def writefile(todotxt, fp=FILEPATH):
    """
    Writes the content of list in provide filepath
    """
    with open(fp, 'w') as newfile:
        newfile.writelines(todotxt)


def showtodo(tdl):
    """ Prints ToDo list """
    for position, task in enumerate(tdl):
        print(f'{position + 1}: {task}', end='')


def remaction(st, ln):
    """ Removes input action and return the string """
    return st[ln:]