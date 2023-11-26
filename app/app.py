import streamlit as st
import openai
from dotenv import load_dotenv
from pathlib import Path
import os


# load API keys
dotenv_path = Path(r"C:\Storage\python_projects\ashvin\.env")
load_dotenv(dotenv_path=dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set your OpenAI API key
openai.api_key = OPENAI_API_KEY

# constants
GPT_MODEL = "gpt-3.5-turbo"

# streamlit page setup
st.set_page_config(page_title="Kiln")


# prompts : format_prompts
format_prompts = {
    "user story": "As a [specific user type], I want to [an action], so that [benefit/value]",
    "how might we": "How might we [achieve a particular outcome or improvement] for [user/persona] so that [benefit/value]",
    # "jobs to be done": "[User/persona] wants to [job to be done] when [a specific situation occurs] so that [benefit/value].",
    # "jobs to be done": "The [specific user type]] wants [job to be done] when [a specific situation occurs] so that [benefit/value].",
    "jobs to be done": "When [situation] I want to [motivation] so I can [expected outcome].",
    "we believe that": "We believe [hypothesis] results in [outcome/value] because of [single specific reason].",
}


# Streamlit App
def main():
    st.title("Kiln")
    st.sidebar.markdown("## Controls")

    # Dropdown for user to select output type
    user_selection = st.selectbox(
        "Output Type:",
        ["user story", "how might we", "jobs to be done", "we believe that"],
    )

    # Taking long text input from the user
    user_input = st.text_area(
        "Enter your idea or pain point:", value="", height=100, max_chars=300
    )

    # Button to trigger action
    submit_button = st.button("Submit")

    # If the input exists and the user clicks on the button
    if user_input and submit_button:
        # Directly access the system content from the format_prompts dictionary
        system_content = format_prompts.get(user_selection, "")

        # Handling the case when the user_selection is not in format_prompts
        if not system_content:
            st.error("Invalid selection.")
            return

        try:
            response = openai.ChatCompletion.create(
                model=GPT_MODEL,
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": user_input},
                ],
            )

            # Extracting the assistant's response and displaying it
            assistant_response = response["choices"][0]["message"]["content"]
            st.write(assistant_response)
        except Exception as e:
            # Handle exceptions from the API call
            st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
