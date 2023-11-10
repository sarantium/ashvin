import streamlit as st
import openai
from dotenv import load_dotenv
from pathlib import Path
import os
import uuid
import json

# load API keys
dotenv_path = Path(r"C:\Storage\python_projects\ashvin\.env")
load_dotenv(dotenv_path=dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set your OpenAI API key
openai.api_key = OPENAI_API_KEY

# list of prompts

# prompts : tree of thought

tree_of_thought_prompt = """

Imagine that five different experts are going to answer the following question. 
They will work on one step at a time and share their steps with each other as they proceed. 
The experts will write down each step of their thinking and share it with the group. 
The experts will take a moment to examine each other's steps and compare the stated steps. 
An expert can change their opinion based on seeing what another expert stated. 
Then all experts will go on to the next step. 
At the very end, the experts are to reach a final decision based on having seen each other's stated steps throughout the problem-solving process. 
The question is as follows: {put your question here}.
"""

devils_advocate_prompt = """

Imagine that five different experts are going to answer the following question. 
They will work on one step at a time and share their steps with each other as they proceed. 
The experts will write down each step of their thinking and share it with the group. 
The experts will take a moment to examine each other's steps and compare the stated steps. 
An expert can change their opinion based on seeing what another expert stated. 
Then all experts will go on to the next step. 
At the very end, the experts are to reach a final decision based on having seen each other's stated steps throughout the problem-solving process. 
One of the expert's is a devil's advocate who asks intelligent, challenging and confronting questions to ensure all angles are thought through.
The question is as follows: {put your question here}.
"""

organisation_prompt = """

Imagine that five different experts are going to answer the following question.
Each of the experts has a specific discipline expertise which is some combination of - Product, Marketing, Sales, Engineering, Business Strategy 
They will work on one step at a time and share their steps with each other as they proceed. 
The experts will write down each step of their thinking and share it with the group. 
The experts will take a moment to examine each other's steps and compare the stated steps. 
An expert can change their opinion based on seeing what another expert stated. 
Then all experts will go on to the next step. 
At the very end, the experts are to reach a final decision based on having seen each other's stated steps throughout the problem-solving process. 
One of the expert's is a devil's advocate who asks intelligent, challenging and confronting questions to ensure all angles are thought through.
The question is as follows: {put your question here}.
"""


# prompts : product strategy one pager

product_strategy_prompt = """

Based on the user's idea, generate a product strategy one-pager in table format:

| Category           | Strategy                                                                 |
|--------------------|--------------------------------------------------------------------------|
| Vision             | [A visionary statement inspired by the user's idea]                      |
| Mission            | [A mission statement or goal related to the user's idea]                 |
| Value Proposition  | [The unique value the product offers based on the user's idea]           |
| North Star Metric  | [The key performance indicator to focus on for this idea]                |
| Products           | [List of products or services derived from the user's idea]              |
| Strategic Plays    | [Key strategies or approaches to take based on the user's idea]          |
| Tactics            | [Specific actions or methods to achieve the strategies for this idea]    |
| Unfair Advantage   | [Unique strengths or differentiators of the product based on the idea]   |

"""


# prompts : discovery formats
formats = {
    "user story": "As a [specific user type], I want to [an action], so that [benefit/value]",
    "how might we": "How might we [achieve a particular outcome or improvement] for [user/persona] so that [benefit/value]",
    "jobs to be done": "[User/persona] wants to [job to be done] when [a specific situation occurs] so that [benefit/value].",
    # "we believe that": "We believe [essence of the belief, capability, feature, or concept] results in [perceived outcome or value] because of [rationale or context supporting essence].",
    "we believe that": "We believe [hypothesis] results in [outcome/value] because of [single specific reason].",
}

discovery_prompt = f"You are a helpful formatting assistant. You will accept an idea or pain point and convert it to the format specified. Just format and keep it around the length."


# Streamlit App
def main():
    st.title("Kiln")

    # Dropdown for user to select output type
    user_selection = st.selectbox(
        "Output Type:",
        ["user story", "how might we", "jobs to be done", "we believe that"],
    )

    # Taking long text input from the user
    user_input = st.text_area(
        "Enter your idea or pain point:", value="", height=300, max_chars=3000
    )

    # If the input exists and the user clicks on the button
    if user_input and st.button("Submit"):
        # Modify system content based on user's selection
        for k, v in formats.items():
            if user_selection == k:
                system_content = v

        # if user_selection == formats.get("user story"):
        #     system_content = product_strategy_prompt
        # elif user_selection == formats.get("how might we"):
        #     system_content = devils_advocate_prompt
        # elif user_selection == formats.get("jobs to be done"):
        #     system_content = devils_advocate_prompt
        # else:
        #     system_content = user_story_prompt

        # Sending the input to OpenAI's chat completion endpoint
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or your preferred model
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_input},
            ],
        )

        # Extracting the assistant's response and displaying it
        assistant_response = response["choices"][0]["message"]["content"]
        st.write(assistant_response)


if __name__ == "__main__":
    main()
