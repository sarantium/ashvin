# main file to develop kiln agent app.
# TODOs
# done import env for OpenAI
# done import various libraries - Enum, ABC, dataclass to start with
# todo from the start use docstrings
# todo need to find a PM skills map/competencies and add it to Golem class
# todo use this prompt to improve the userflow prompt below to get the better scenario "4. Act as a user researcher for a [social networking application]. Pretend I’m a user and ask me questions about my experience to [discover growth opportunities]."
# todo find Kiln people concepts
# todo compare to DTDL implementation


# import
from enum import Enum, StrEnum
from typing import Callable, Any
from dataclasses import dataclass, field
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
import os
import uuid

# load API keys
dotenv_path = Path(r"C:\Storage\python_projects\ashvin\.env")
load_dotenv(dotenv_path=dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# core dataclasses


def get_new_uuid() -> str:
    return str(uuid.uuid4())


@dataclass(kw_only=True)
class Tool:
    name: str
    function: Callable
    id: str = field(default_factory=get_new_uuid)
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Golem:
    name: str
    id: str = field(default_factory=get_new_uuid)
    timestamp: datetime = field(default_factory=datetime.utcnow)
    tools: list[Tool] = field(default_factory=list)


@dataclass
class Event:
    name: str
    details: dict[str, Any]
    id: str = field(default_factory=get_new_uuid)
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Twin:
    name: str
    properties: dict[str, Any]
    id: str = field(default_factory=get_new_uuid)
    timestamp: datetime = field(default_factory=datetime.utcnow)
    events: list[Event] = field(default_factory=list)


@dataclass
class Kiln:
    twins: dict[str, Twin] = field(default_factory=dict)
    golems: dict[str, Golem] = field(default_factory=dict)
    twin_golem_links: dict[str, set[str]] = field(default_factory=dict)
    golem_twin_links: dict[str, set[str]] = field(default_factory=dict)

    def add_twin(self, twin: Twin) -> None:
        self.twins[twin.id] = twin

    def add_golem(self, golem: Golem) -> None:
        self.golems[golem.id] = golem

    def link_twin_golem(self, twin_id: str, golem_id: str) -> None:
        """Link a twin and a golem by storing their IDs in a mapping."""
        if twin_id in self.twins and golem_id in self.golems:
            # Add the golem to the set of golems linked to the twin
            self.twin_golem_links.setdefault(twin_id, set()).add(golem_id)
            # Add the twin to the set of twins linked to the golem
            self.golem_twin_links.setdefault(golem_id, set()).add(twin_id)
        else:
            raise ValueError("Twin ID or Golem ID not found.")

    def get_linked_golems(self, twin_id: str) -> set[Golem]:
        """Retrieve the golems linked to a given twin."""
        linked_golem_ids = self.twin_golem_links.get(twin_id, set())
        return {self.golems[golem_id] for golem_id in linked_golem_ids}

    def get_linked_twins(self, golem_id: str) -> set[Twin]:
        """Retrieve the twins linked to a given golem."""
        linked_twin_ids = self.golem_twin_links.get(golem_id, set())
        return {self.twins[twin_id] for twin_id in linked_twin_ids}


# # Enums
# class Stage(StrEnum):
#     """stages in the product management lifecycle"""

#     DISCOVER = "discovery"
#     DEFINE = "definition"
#     DEVELOP = "development"
#     DELIVER = "delivery"


# class Output(StrEnum):
#     """output documents"""

#     OPPORTUNTY_SOLUTION_TREE = "opportunity solution tree"
#     CANVAS = "canvas"
#     ROADMAP = "roadmap"
#     GO_TO_MARKET = "go to market"


# class Persona(StrEnum):
#     MARTY_CAGAN = "marty cagan"
#     ASH_MAURYA = "ash maurya"
#     TERESA_TORRES = "teresa torres"


# # golem dataclass
# @dataclass
# class Golem:
#     """_summary_"""

#     stage: Stage
#     output: Output
#     persona: Persona | None
#     skills: list[str]
#     lifespan: int | None = None


# # kiln Enum
# class Kiln(Enum):
#     """_summary_

#     Arguments:
#         Enum {_type_} -- _description_
#     """

#     DISCOVER = Golem(stage=Stage.DISCOVER, output=Output.OPPORTUNTY_SOLUTION_TREE)


# # prompts
# userflow = """
# System Message :
#  You are an expert UX researcher. You observe and record current or potential users as they interact with the idea, app or prototype, with or without technology. You gather focused data about existing pain points and as-is interaction flows from diverse user segments. Specifically, in your data collection you consider:
# -     Trigger: What initiates the task for the user?
# -     Desired Outcome: How will users know they have successfully completed the task?
# -     Base Knowledge: What will the users be expected to know when starting the task?
# -     Required Knowledge: What do users already know before starting the task?
# -     Artifacts: What resources or tools will users require during the task?
# With your current data, you can sketch out increasingly detailed, accurate and relevant versions of how a user goes about their daily life by mapping out the sequence of activities required to achieve a goal in a user flow diagram.

# Task Analysis:
# Here is a step-by-step guide for conducting task analysis:
# 1.    Based on the {scenario} provided, identify the task you need to analyse
# 2.    Identify and rank 5 relevant customer segments for this task based on the scenario
# 3.    Construct a longlist of 10 user personas relevant to this scenario, then rank these personas according to relevance and select the top 3 personas to conduct a task analysis
# 4.    Pick each persona in turn, then conduct the task analysis process below for each of them.
# a.    What is that user's goal and motivation to achieve said goal?
# b.    Break down this goal into smaller subtasks: A good rule of thumb is to aim for 4–8 subtasks – any more than this may indicate that the goal is too broad or abstract.
# c.    Draw a layered task diagram of each subtask: You can use any notation you like for the diagram since there is no real standard here.
# d.    Ensure you accompany your diagram with a narrative that focuses on the whys.
# e.    Validate Your Analysis: Review the analysis with someone who wasn’t involved in the breakdown but knows the tasks well enough to check for consistency.

# Output:
# Produce a user flow diagram that depicts the sequence of
# steps that the user will take to complete the task, including the key decisions
# that they will make at each step. The diagram should be annotated with a
# narrative that explains the user's goals and motivations at each step.

# Formatting Requirements:
# The user flow diagram should be created using a standard diagramming notation, such as UML activity diagrams or flowcharts. The narrative should be written in plain English and should be easy to understand for both technical and non-technical audiences.

# Chain of Thought:
# Please explicitly articulate your chain of thought step by step as you complete the task analysis and create the user flow diagram. This will help me to understand your reasoning and to ensure that the output is accurate and complete.

# # Your Scenario :
# """
