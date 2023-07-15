import streamlit as st
import functions

todos = functions.read_todo()


st.set_page_config(layout="wide")
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todo(todos)


st.title("My Todo App")
st.subheader("This is my todo app. ")
st.write("This app is to increase your <b>productivity</b>. ",
         unsafe_allow_html=True)

st.text_input(label="", placeholder="Add New To-Do...",
              on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()


print("Hello")
# st.session_state
