from modules import todo_functions
import time


time_now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is', time_now)


while True:
    user_action = input('Type add, show, edit, complete or exit:').strip().lower()
    if user_action == 'add':
        todo_functions.add_todo()
    elif user_action == 'show':
        todo_functions.show_todos()
    elif 'edit' in user_action:
        todo_functions.edit_todo(user_action)
    elif user_action == 'complete':
        todo_functions.complete_todo()
    elif user_action == 'exit':
        print('Bye!')
        break
