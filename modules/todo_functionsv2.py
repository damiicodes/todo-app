FILEPATH = '/Users/damifajinmi' \
           '/PMC_PROJECTS/files/todos.txt'


def get_todos(filepath=FILEPATH):
    """"" Reads a text file and returns a list
    of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    :param todos_arg: Writes the new list of to-do items
     into the text file
    :param filepath:
    :return: None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == '__main__':
    print('Hello')
    print(get_todos())

