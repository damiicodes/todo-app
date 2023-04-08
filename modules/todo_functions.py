import os

if __name__ == '__main__':
    from modules import todo_filepath


def add_todo():
    """
    Adds a new todo item to the list of todos.
    """
    todo = input('Enter a todo:').strip()
    if not todo:
        print("You can't add an empty task.")
        return
    todo += "\n"
    if not os.path.exists(todo_filepath.filepath):
        with open('../files/todos.txt', 'w'):
            pass
    with open(todo_filepath.filepath, 'a') as file:
        file.write(todo)
    print('Todo added successfully.')


def show_todos():
    """
    Displays all the todos in the list.
    """
    if not os.path.exists(todo_filepath.filepath):
        print("No to-do list found.")
        return
    with open(todo_filepath.filepath, 'r') as file:
        todos = file.readlines()
    if not todos:
        print("The to-do list is empty.")
        return
    for index, item in enumerate(todos):
        row = f"{index + 1}--{item.strip()}"
        print(row)


def edit_todo(user_action):
    """
    Edits an existing todo item in the list.
    """
    try:
        if not os.path.exists(todo_filepath.filepath):
            print("No to-do list found.")
            return
        with open(todo_filepath.filepath, 'r') as file:
            todos = file.readlines()
        new_todos = [item.strip() for item in todos]
        if not new_todos:
            print("The to-do list is empty.")
            return
        if 'edit' in user_action:
            if len(user_action) > 4:
                number = int(user_action[5:]) - 1
                new_todo = input('Enter new todo:').strip()
                new_todos[number] = new_todo
                with open(todo_filepath.filepath, 'w') as file:
                    file.writelines([item + "\n" for item in new_todos])
                print('Todo updated successfully.')
            else:
                number = int(input('Please choose the number of the todo you would like to edit: '))
                number -= 1
                new_todo = input('Enter new todo:').strip()
                new_todos[number] = new_todo
                with open(todo_filepath.filepath, 'w') as file:
                    file.writelines([item + "\n" for item in new_todos])
                print('Todo updated successfully.')
        else:
            print('Invalid input. Please try again.')
    except ValueError:
        print('Invalid input. Please try again.')


def complete_todo():
    """
    Marks an existing todo item as completed and removes it from the list.
    """
    if not os.path.exists(todo_filepath.filepath):
        print("No to-do list found.")
        return
    with open(todo_filepath.filepath, 'r') as file:
        todos = file.readlines()
    new_todos = [item.strip() for item in todos]
    if not new_todos:
        print("The to-do list is empty.")
        return
    number = int(input('Number of the todo to complete: '))
    index = number - 1
    if not 0 <= index < len(new_todos):
        print('Invalid input. Please try again.')
        return
    todo_to_remove = new_todos[index]
    new_todos.pop(index)
    with open(todo_filepath.filepath, 'w') as file:
        file.writelines([item + "\n" for item in new_todos])
    message = f'Todo "{todo_to_remove}" was removed from the list.'
    print(message)


