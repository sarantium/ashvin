import streamlit as st
import openai
import pandas as pd
import sqlite3
from dotenv import load_dotenv
from pathlib import Path
import os

# Load API keys
dotenv_path = Path(r"C:\Storage\python_projects\ashvin\.env")
load_dotenv(dotenv_path=dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY
GPT_MODEL = "gpt-3.5-turbo"

# Database Connection
DB_PATH = "ideas.db"  # Update the path to your database


def load_ideas():
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql("SELECT * FROM ideas", conn)


def save_idea(idea_id, new_title):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("UPDATE ideas SET title = ? WHERE id = ?", (new_title, idea_id))
        conn.commit()


# Streamlit App
def main():
    st.set_page_config(page_title="Kiln")
    st.title("Kiln")

    # Load ideas from the database
    df_ideas = load_ideas()
    st.write(df_ideas)

    st.sidebar.markdown("## Controls")
    selected_idea_id = st.sidebar.selectbox("Select an Idea", df_ideas["id"])
    idea_row = df_ideas[df_ideas["id"] == selected_idea_id]
    selected_idea = f"{idea_row['title'].iloc[0]} - {idea_row['notes'].iloc[0]}"

    format_button = st.sidebar.button("Format Idea")

    if format_button:
        formatted_ideas = format_idea(selected_idea)
        if formatted_ideas:
            option = st.radio("Choose a formatted version to save:", formatted_ideas)
            if st.button("Save"):
                save_idea(selected_idea_id, option)
                st.success("Idea updated in database.")


def format_idea(idea):
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


if __name__ == "__main__":
    main()
