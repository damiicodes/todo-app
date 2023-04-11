from modules import todo_functionsv2
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass


sg.theme('163537Dark')

clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo', key='new_todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=todo_functionsv2.get_todos(), key='existing_todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = todo_functionsv2.get_todos()
            new_todo = values['new_todo'] + '\n'
            todos.append(new_todo)
            todo_functionsv2.write_todos(todos)
            window['existing_todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['existing_todos'][0]
                new_todo = values['new_todo']

                todos = todo_functionsv2.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                todo_functionsv2.write_todos(todos)
                window['existing_todos'].update(values=todos)
            except IndexError:
                sg.Popup('Please select an item first', background_color='red',
                         text_color='black', font=('Helvetica', 20))

        case 'Complete':
            try:
                todo_to_complete = values['existing_todos'][0]
                todos = todo_functionsv2.get_todos()
                todos.remove(todo_to_complete)
                todo_functionsv2.write_todos(todos)
                window['existing_todos'].update(values=todos)
                window['new_todo'].update(value='')
            except IndexError:
                sg.Popup('Please select an item first', background_color='red',
                         text_color='black', font=('Helvetica', 20))
        case 'Exit':
            break
        case 'existing_todos':
            window['new_todo'].update(value=values['existing_todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()


