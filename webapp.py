import streamlit as st
import functions

lst = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    lst.append(todo)
    functions.write_todos(lst)
    



st.title('My ToDo App')
st.subheader('This is my todo app.')
st.write("This app is to increase your productivity.")

for index, item in enumerate(lst):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        lst.pop(index)
        functions.write_todos(lst)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add To-Do', on_change=add_todo, key='new_todo')