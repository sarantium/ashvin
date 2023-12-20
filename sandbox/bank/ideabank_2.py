import streamlit as st
import sqlite3
import pandas as pd

# Database connection
conn = sqlite3.connect("ideas.db", check_same_thread=False)


# Function to create the table
def create_table():
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS ideas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            notes TEXT,
            impact INTEGER,
            confidence INTEGER,
            ease INTEGER
        )
    """
    )
    conn.commit()


# Function to add a new idea
def add_idea(title, notes, impact, confidence, ease):
    conn.execute(
        """
        INSERT INTO ideas (title, notes, impact, confidence, ease)
        VALUES (?, ?, ?, ?, ?)
    """,
        (title, notes, impact, confidence, ease),
    )
    conn.commit()


# Function to view all ideas
def view_all_ideas():
    return pd.read_sql("SELECT * FROM ideas", conn)


# Function to update an idea
def update_idea(id, title, notes, impact, confidence, ease):
    conn.execute(
        """
        UPDATE ideas
        SET title = ?, notes = ?, impact = ?, confidence = ?, ease = ?
        WHERE id = ?
    """,
        (title, notes, impact, confidence, ease, id),
    )
    conn.commit()


# Function to delete an idea
def delete_idea(id):
    conn.execute("DELETE FROM ideas WHERE id = ?", (id,))
    conn.commit()


def main():
    st.title("Idea Management App")

    # Creating the table
    create_table()

    # Sidebar for Create functionality
    with st.sidebar.form("Add Idea", clear_on_submit=True):
        st.subheader("Add New Idea")
        new_title = st.text_input("Title")
        new_notes = st.text_area("Notes")
        new_impact = st.slider("Impact", 1, 5, 3)
        new_confidence = st.slider("Confidence", 1, 5, 3)
        new_ease = st.slider("Ease", 1, 5, 3)
        submit_button = st.form_submit_button("Add Idea")

        if submit_button:
            add_idea(new_title, new_notes, new_impact, new_confidence, new_ease)
            st.success("Idea Added Successfully!")

    # Main panel for viewing and editing ideas
    st.subheader("All Ideas")
    all_ideas = view_all_ideas()
    st.dataframe(all_ideas)

    # Update/Delete functionality
    selected_id = st.selectbox("Select an Idea to Edit/Delete", all_ideas["id"])

    if st.button("Update Idea"):
        idea_to_update = all_ideas[all_ideas["id"] == selected_id].iloc[0]
        update_title = st.text_input("Title", idea_to_update["title"])
        update_notes = st.text_area("Notes", idea_to_update["notes"])
        update_impact = st.slider("Impact", 1, 5, idea_to_update["impact"])
        update_confidence = st.slider("Confidence", 1, 5, idea_to_update["confidence"])
        update_ease = st.slider("Ease", 1, 5, idea_to_update["ease"])
        if st.button("Submit Update"):
            update_idea(
                selected_id,
                update_title,
                update_notes,
                update_impact,
                update_confidence,
                update_ease,
            )
            st.success("Idea Updated Successfully!")

    if st.button("Delete Idea"):
        delete_idea(selected_id)
        st.warning("Idea Deleted!")


if __name__ == "__main__":
    main()
