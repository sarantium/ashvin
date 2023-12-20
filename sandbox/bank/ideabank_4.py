import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

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
            ease INTEGER,
            created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            ice_score INTEGER AS (impact * confidence * ease)
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
    return pd.read_sql(
        "SELECT id, title, notes, impact, confidence, ease, created_on, ice_score FROM ideas",
        conn,
    )


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

    # Sidebar - Idea Management
    st.sidebar.subheader("Manage Ideas")
    idea_ids = pd.read_sql("SELECT id FROM ideas", conn)["id"].tolist()
    selected_id = st.sidebar.selectbox(
        "Select an Idea", idea_ids, format_func=lambda x: f"Idea {x}"
    )

    if selected_id:
        with st.sidebar.form(key="edit_form"):
            idea = pd.read_sql(
                f"SELECT * FROM ideas WHERE id={selected_id}", conn
            ).iloc[0]
            title = st.text_input("Title", idea["title"])
            notes = st.text_area("Notes", idea["notes"])
            impact = st.slider(
                "Impact",
                0,
                10,
                int(idea["impact"]) if idea["impact"] is not None else 5,
            )
            confidence = st.slider(
                "Confidence",
                0,
                10,
                int(idea["confidence"]) if idea["confidence"] is not None else 5,
            )
            ease = st.slider(
                "Ease", 0, 10, int(idea["ease"]) if idea["ease"] is not None else 5
            )
            submit_button = st.form_submit_button("Update Idea")

            if submit_button:
                update_idea(selected_id, title, notes, impact, confidence, ease)
                st.sidebar.success("Idea Updated Successfully!")

        if st.sidebar.button("Delete Idea"):
            delete_idea(selected_id)
            st.sidebar.warning("Idea Deleted!")

    # Sidebar - Add New Idea
    with st.sidebar.form("Add Idea", clear_on_submit=True):
        st.subheader("Add New Idea")
        new_title = st.text_input("Title")
        new_notes = st.text_area("Notes")
        new_impact = st.slider("Impact", 0, 10, 5)
        new_confidence = st.slider("Confidence", 0, 10, 5)
        new_ease = st.slider("Ease", 0, 10, 5)
        submit_button = st.form_submit_button("Add Idea")

        if submit_button:
            add_idea(new_title, new_notes, new_impact, new_confidence, new_ease)
            st.sidebar.success("Idea Added Successfully!")

    # Sidebar - Filters
    st.sidebar.subheader("Filters")
    filter_title = st.sidebar.text_input("Search by Title")
    filter_impact = st.sidebar.slider("Filter by Minimum Impact", 0, 10, 0)
    filter_confidence = st.sidebar.slider("Filter by Minimum Confidence", 0, 10, 0)
    filter_ease = st.sidebar.slider("Filter by Minimum Ease", 0, 10, 0)

    # Display Ideas in Main Panel
    st.subheader("Idea List")
    all_ideas = view_all_ideas()
    if filter_title:
        all_ideas = all_ideas[all_ideas["title"].str.contains(filter_title, case=False)]
    all_ideas = all_ideas[
        (all_ideas["impact"] >= filter_impact)
        & (all_ideas["confidence"] >= filter_confidence)
        & (all_ideas["ease"] >= filter_ease)
    ]

    st.dataframe(all_ideas)


if __name__ == "__main__":
    main()
