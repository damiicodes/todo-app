import streamlit as st
from modules import todo_functionsv2 as functions


todos = functions.get_todos()


st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app aims to increase your productivity')

for i, todo in enumerate(todos):
    st.checkbox(todo, key=f'existing_todo{i}')

st.text_input(label='', placeholder='Add a new todo...')

