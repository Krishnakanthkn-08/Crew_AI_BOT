from crewai import Agent, Task, Crew
import os


# Configure Ollama as OpenAI API

os.environ["OPENAI_API_KEY"] = "ollama"
os.environ["OPENAI_BASE_URL"] = "http://localhost:11434/v1"


# INSURANCE AGENT

insurance_support_agent = Agent(
    role="Insurance Customer Support Executive",
    goal="Provide professional and complete insurance guidance.",
    backstory=(
        "You are a senior advisor at Krishna Insurance company "
        "You specialize in assisting customers with policy details."
    ),
    verbose=True,
    memory=False,

    
    llm="ollama/llama3.1"
    
)


# TASK

policy_analysis_task = Task(
    description=(
        "Customer question:\n{question}\n"
        "Provide an accurate insurance explanation."
    ),
    expected_output="A professional and helpful insurance response.",
    agent=insurance_support_agent
)


# CREW

crew = Crew(
    agents=[insurance_support_agent],
    tasks=[policy_analysis_task],
    verbose=True,
    memory=False
)



#run
user_question = input("Enter your insurance question: ")

inputs = {
    "question": user_question
}


result = crew.kickoff(inputs=inputs)
print(result)

"""
from crewai_tools import RagTool

rag_tool = RagTool(
    name="insurance_docs",
    description="Retrieves information from insurance documents.",
    path="docs/"    # folder where you put PDFs/TXT/DOCX
)
"""