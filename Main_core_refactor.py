from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Define the tools and models
groq = ChatGroq(model_name='llama3-8b-8192', temperature=0.5)
model = groq  # Select the model to use
search_tool = SerperDevTool()

# Define agents
melchior = Agent(
    role='Melchior-1',
    goal='Conduct technical analysis and provide logical conclusions.',
    backstory='Evangelion lore: Melchior: Born from the mind of Dr. Naoko Akagi, ...',
    verbose=False,
    allow_delegation=True,
    llm=model,
    output='melchior.txt'
)

balthasar = Agent(
    role='Balthasar-2',
    goal='Develop defense strategies and oversee tactical operations.',
    backstory='Evangelion lore: Balthasar, the second of the Magi, was imbued with the persona of Dr. Akagi as a mother....',
    verbose=True,
    allow_delegation=True,
    llm=model
)

casper = Agent(
    role='Casper-3',
    goal='Evaluate ethical implications and make balanced decisions.',
    backstory='Evangelion lore: The last of the Magi, Caspar, was created from Dr. Akagi’s persona as a woman....',
    verbose=True,
    allow_delegation=True,
    llm=model
)

def process_question(question):
    # Define tasks
    scientific_analysis_task = Task(
        description=f'Analyze the technical data provided and extract conclusions about "{question}".',
        expected_output='Detailed report with conclusions based on the data analysis.',
        tools=[search_tool],
        agent=melchior
    )

    strategy_task = Task(
        description=f'Formulate a strategic plan based on current threats about "{question}".',
        expected_output='A comprehensive defense strategy.',
        tools=[search_tool],
        agent=balthasar
    )

    diplomacy_task = Task(
        description=f'Assess the ethical implications of a proposed action about "{question}".',
        expected_output='A summary of all the analysis done before with a reasoned judgment on the ethical acceptability of the action.',
        tools=[search_tool],
        agent=casper
    )

    # Form the crew
    magi_system = Crew(
        agents=[melchior, balthasar, casper],
        tasks=[scientific_analysis_task, strategy_task, diplomacy_task],
        memory=True,
        cache=True,
        verbose=1,
    )

    result = magi_system.kickoff()
    return result