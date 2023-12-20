import streamlit as st
import pandas as pd
import sqlite3

# https://docs.streamlit.io/library/advanced-features/connecting-to-data


# Connect to SQLite database
@st.connection(hash_funcs={sqlite3.Connection: id})
def get_connection(path):
    return sqlite3.connect(path)


conn = get_connection("ideas.db")


# Function to load data from the SQLite database
def load_data():
    query = "SELECT * FROM ideas"
    df = pd.read_sql_query(query, conn)
    return df


# Function to add a new row to the 'ideas' table
def add_idea(title, notes, impact, confidence, ease):
    query = "INSERT INTO ideas (title, notes, impact, confidence, ease) VALUES (?, ?, ?, ?, ?);"
    cur = conn.cursor()
    cur.execute(query, (title, notes, impact, confidence, ease))
    conn.commit()
    cur.close()


# Streamlit app layout
def main():
    st.title("Ideas Table Visualization")

    # Sidebar inputs
    with st.sidebar:
        st.header("Add New Idea")
        new_title = st.text_input("Title")
        new_notes = st.text_area("Notes")
        new_impact = st.number_input("Impact", min_value=0, max_value=10, step=1)
        new_confidence = st.number_input(
            "Confidence", min_value=0, max_value=10, step=1
        )
        new_ease = st.number_input("Ease", min_value=0, max_value=10, step=1)
        submit_button = st.button("Add Idea")

        if submit_button:
            add_idea(new_title, new_notes, new_impact, new_confidence, new_ease)
            st.success("Idea added successfully!")

    # Main page
    df = load_data()
    st.write("### Ideas DataFrame", df)


if __name__ == "__main__":
    main()
