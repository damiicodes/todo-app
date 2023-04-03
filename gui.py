from modules import todo_functionsv2
import PySimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo', key='new_todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=todo_functionsv2.get_todos(), key='existing_todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
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
            todo_to_edit = values['existing_todos'][0]
            new_todo = values['new_todo']

            todos = todo_functionsv2.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            todo_functionsv2.write_todos(todos)
            window['existing_todos'].update(values=todos)
        case 'existing_todos':
            window['new_todo'].update(value=values['existing_todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()


