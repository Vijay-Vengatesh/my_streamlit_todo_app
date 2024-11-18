import streamlit as st
import functions

data = functions.get_todos()
def add_todo():
    todo_local = st.session_state["new_todo"] + '\n'
    if todo_local not in data:
        data.append(todo_local)
        functions.write_todos(data)
        st.session_state["new_todo"] = ''


st.title("My Todo App")
st.subheader("List your day to day activity below")

for index, item in enumerate(data):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        data.pop(index)
        functions.write_todos(data)
        del st.session_state[item]
        st.rerun()

st.text_input(label="", placeholder="Enter a todo",
              on_change=add_todo, key="new_todo")
