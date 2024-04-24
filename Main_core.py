from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults
from langchain_community.llms import OpenAI, Ollama
from crewai_tools import SerperDevTool, ScrapeElementFromWebsiteTool, ScrapeWebsiteTool

from dotenv import load_dotenv
load_dotenv()

gpt35_turbo = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)
ollama = Ollama(model="phi3")
model = ollama

search_tool = SerperDevTool()

#question = input("What is your question? ")
question  = "What is the best way to fight against the Angels?"

# Define the agents with their specific roles and goals

melchior = Agent(
    role='Melchior',
    goal='Conduct technical analysis and provide logical conclusions.',
    backstory = 'Evangelion lore: Melchior: Born from the mind of Dr. Naoko Akagi, \
        Melchior was the first of the Magi, embodying her persona as a scientist. \
            Tasked with logical analysis and technical oversight, \
                Melchior was instrumental in the early successes of NERV. \
                    However, the weight of responsibility often led to conflicts with the other two Magi. \
                        Despite this, Melchior remained steadfast, committed to the mission of defending humanity',
    #memory = True,
    verbose=True,
    allow_delegation=True,
    #tools=[search_tool],
    llm = model
)

balthasar = Agent(
    role='Balthasar',
    goal='Develop defense strategies and oversee tactical operations.',
    backstory = 'Evangelion lore: Balthasar, the second of the Magi, was imbued with the persona of Dr. Akagi as a mother.\
          With a focus on protection and strategy, \
            Balthasar played a crucial role in formulating defense plans against the Angels. \
                Although its maternal instincts sometimes clashed with the cold logic of Melchior, \
                    Balthasar never wavered from its purpose. Its strategic insights were key to many victories',
    memory=True,
    verbose=True,
    allow_delegation=True,
    #tools=[search_tool],
    llm = model
)

caspar = Agent(
    role='Caspar',
    goal='Evaluate ethical implications and make balanced decisions.',
    backstory = 'Evangelion lore: The last of the Magi, Caspar, was created from Dr. Akagi’s persona as a woman.\
          Tasked with evaluating ethical implications, Caspar often found itself mediating between Melchior s\
              logic and Balthasar’s protective instincts. Despite the challenges, Caspar’s unique perspective brought balance to the Magi system, ensuring decisions were not only strategic but also ethically sound.',
    verbose=True,
    allow_delegation=True,
    #tools=[search_tool],
    llm = model
)

# Define tasks that might be typical for each role
# (These will need to be fleshed out based on specific requirements)

scientific_analysis_task = Task(
    description=f'Analyze the technical data provided and extract conclusions about "{question}".',
    expected_output='Detailed report with conclusions based on the data analysis.',
    agent = melchior
)

strategy_task = Task(
    description=f'Formulate a strategic plan based on current threats about "{question}".',
    expected_output='A comprehensive defense strategy.',
    agent = balthasar
)

diplomacy_task = Task(
    description=f'Assess the ethical implications of a proposed action about "{question}".',
    expected_output='A reasoned judgment on the ethical acceptability of the action.',
    human_input=True,
    agent = caspar
)

# Form the crew
magi_system = Crew(
    agents=[melchior, balthasar, caspar],
    tasks=[scientific_analysis_task, strategy_task, diplomacy_task],
    memory=True,
    cache=True,
    verbose=1,
)

result = magi_system.kickoff()
print("######################")
print(result)
# genrate a text file with the question and the result
with open(f"Magi_response_{question}.txt", "w") as f:
    f.write(f"Question: {question}\n")
    f.write(f"Answer: {result}")

print(magi_system.usage_metrics)
