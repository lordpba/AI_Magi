import streamlit as st
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults
from langchain_community.llms import OpenAI, Ollama
from crewai_tools import SerperDevTool, ScrapeElementFromWebsiteTool, ScrapeWebsiteTool
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Streamlit code
st.title('Magi System Simulation')

question = st.text_input("What is your question?")

if st.button('Run Simulation'):
    with st.spinner('Running the simulation...'):
        load_dotenv()
        groq = ChatGroq(model_name='llama3-8b-8192') 
        model = groq #select the model to use
        search_tool = SerperDevTool()

        # Define the agents with their specific roles and goals
        melchior = Agent(
            role='Melchior-1',
            goal='Conduct technical analysis and provide logical conclusions.',
            verbose= False,
            allow_delegation=True,
            llm = model,
        )
        balthasar = Agent(
            role='Balthasar-2',
            goal='Develop defense strategies and oversee tactical operations.',
            verbose=True,
            allow_delegation=True,
            llm = model
        )
        casper = Agent(
            role='Casper-3',
            goal='Evaluate ethical implications and make balanced decisions.',
            verbose=True,
            allow_delegation=True,
            llm = model
        )

        # Define tasks that might be typical for each role
        scientific_analysis_task = Task(
            description=f'Analyze the technical data provided and extract conclusions about "{question}".',
            expected_output='Detailed report with conclusions based on the data analysis.',
            tools = [search_tool],
            agent = melchior
        )
        strategy_task = Task(
            description=f'Formulate a strategic plan based on current threats about "{question}".',
            expected_output='A comprehensive defense strategy.',
            tools = [search_tool],
            agent = balthasar
        )
        diplomacy_task = Task(
            description=f'Assess the ethical implications of a proposed action about "{question}".',
            expected_output='A summary of all the analysis done before with \
                a reasoned judgment on the ethical acceptability of the action.',
            human_input=True,
            tools = [search_tool],
            agent = casper
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
        st.write("######################")
        st.write(result)
        st.write(magi_system.usage_metrics)