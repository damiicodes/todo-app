import streamlit as st
from modules import todo_functionsv2 as functions

todos = functions.get_todos()


def add_todo():
    todo_to_add = st.session_state['new_todo'] + '\n'
    todos.append(todo_to_add)
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app aims to increase your productivity')

for i, todo in enumerate(todos):
    st.checkbox(todo, key=i)

st.text_input(label='test', placeholder='Add a new todo...',
              on_change=add_todo, key='new_todo')

