import streamlit as st
import openai
import pandas as pd
import sqlite3
from dotenv import load_dotenv
from pprint import pprint as pp
from pathlib import Path
from datetime import datetime
import os

# Load API keys
dotenv_path = Path(r"C:\Storage\python_projects\ashvin\.env")
load_dotenv(dotenv_path=dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY
GPT_MODEL = "gpt-4-1106-preview"

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


# Function to format ideas
def format_idea(idea):
    instruction = """
    take the input and convert it exactly to the format of the prompt that follows. 
    Do do not add any additional explanation. 
    Be precise and concise and compress the output to 25 words or less : """

    format_prompts = [
        "As a [specific user type], I want to [an action], so that [benefit/value]",
        "How might we [achieve a particular outcome or improvement] for [user/persona] so that [benefit/value]",
        "When [situation] I want to [motivation] so I can [expected outcome].",
        "We believe [hypothesis] results in [outcome/value] because of [single specific reason].",
    ]

    formatted_ideas = []

    for prompt in format_prompts:
        try:
            response = openai.chat.completions.create(
                model=GPT_MODEL,
                messages=[
                    {"role": "system", "content": instruction},
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": idea},
                ],
            )
            assistant_response = response.choices[0].message.content
            formatted_ideas.append(assistant_response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return None

    return formatted_ideas


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

    # Sidebar - Add New Idea Expander
    with st.sidebar.expander("Add New Idea"):
        with st.form("Add Idea", clear_on_submit=True):
            new_title = st.text_input("Title")
            new_notes = st.text_area("Notes")
            new_impact = st.slider("Impact", 0, 10, 5)
            new_confidence = st.slider("Confidence", 0, 10, 5)
            new_ease = st.slider("Ease", 0, 10, 5)
            submit_button = st.form_submit_button("Add Idea")

            if submit_button:
                add_idea(new_title, new_notes, new_impact, new_confidence, new_ease)
                st.success("Idea Added Successfully!")

    # Sidebar - Filters Expander
    with st.sidebar.expander("Filters"):
        filter_title = st.text_input("Search by Title")
        filter_impact = st.slider("Filter by Minimum Impact", 0, 10, 0)
        filter_confidence = st.slider("Filter by Minimum Confidence", 0, 10, 0)
        filter_ease = st.slider("Filter by Minimum Ease", 0, 10, 0)

    # Sidebar - Update and Delete Idea Expander
    with st.sidebar.expander("Update/Delete Idea"):
        idea_ids = pd.read_sql("SELECT id FROM ideas", conn)["id"].tolist()
        selected_id = st.selectbox(
            "Select an Idea", idea_ids, format_func=lambda x: f"Idea {x}"
        )

        if selected_id:
            with st.form(key="edit_form"):
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
                    st.success("Idea Updated Successfully!")

            if st.button("Delete Idea"):
                delete_idea(selected_id)
                st.warning("Idea Deleted!")

    # Sidebar - Format Ideas Expander
    with st.sidebar.expander("Format Ideas"):
        idea_ids = pd.read_sql("SELECT id FROM ideas", conn)["id"].tolist()
        selected_format_id = st.selectbox(
            "Select an Idea to Format", idea_ids, format_func=lambda x: f"Idea {x}"
        )

        format_button = st.button("Format")

        if format_button:
            # Retrieve the idea text from the database
            idea_text = pd.read_sql(
                f"SELECT notes FROM ideas WHERE id = {selected_format_id}", conn
            ).iloc[0]["notes"]

            # Call the format_idea function and store the result
            formatted_ideas = format_idea(idea_text)

            # Store the formatted ideas in a session state for displaying in the main panel
            st.session_state["formatted_ideas"] = formatted_ideas

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

    # Display formatted ideas
    if "formatted_ideas" in st.session_state and st.session_state["formatted_ideas"]:
        st.write("Formatted Ideas:")
        for formatted_idea in st.session_state["formatted_ideas"]:
            st.write(formatted_idea)


if __name__ == "__main__":
    main()
