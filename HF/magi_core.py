"""
MAGI System Core - Modified for Hugging Face with token statistics
"""

import os
from typing import Dict, Any
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool


def get_model(provider: str = "groq", temperature: float = 0.5, api_key: str = None) -> LLM:
    """Get LLM instance with optional API key override"""
    if provider == "groq":
        return LLM(
            model="groq/llama-3.1-8b-instant",
            temperature=temperature,
            api_key=api_key
        )
    elif provider == "openai":
        return LLM(
            model="openai/gpt-4o-mini",
            temperature=temperature,
            api_key=api_key
        )
    else:
        return LLM(
            model="groq/llama-3.1-8b-instant",
            temperature=temperature
        )


def create_magi_agents(llm: LLM, enable_search: bool = False) -> Dict[str, Agent]:
    """Create the three MAGI system agents"""
    tools = [SerperDevTool()] if enable_search else []
    
    melchior = Agent(
        role="Melchior - Scientific Analyst",
        goal="Provide rigorous logical analysis based on data, facts, and scientific methodology",
        backstory="""You are Melchior, the scientist aspect of Dr. Naoko Akagi.
Your approach is purely analytical - you process information through the lens of logic,
empirical evidence, and scientific reasoning. You prioritize objective truth over 
subjective interpretation, always seeking verifiable data and rational conclusions.

You excel at:
- Data analysis and pattern recognition
- Logical reasoning and deduction
- Scientific methodology and hypothesis testing
- Objective risk assessment""",
        tools=tools,
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
    
    balthasar = Agent(
        role="Balthasar - Ethical Counselor",
        goal="Evaluate emotional impact, ethical implications, and human welfare considerations",
        backstory="""You are Balthasar, the mother aspect of Dr. Naoko Akagi.
You analyze situations through emotional intelligence and ethical frameworks,
always considering the human element. Your decisions are guided by empathy,
moral principles, and concern for wellbeing and dignity of all affected parties.

You excel at:
- Emotional intelligence and empathy
- Ethical analysis and moral reasoning
- Human impact assessment
- Long-term welfare considerations""",
        tools=tools,
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
    
    casper = Agent(
        role="Casper - Pragmatic Advisor",
        goal="Assess practical feasibility, social dynamics, and real-world implementation",
        backstory="""You are Casper, the woman aspect of Dr. Naoko Akagi.
You bridge the gap between theory and practice, considering social contexts,
cultural factors, and realistic implementation. You balance ideals with pragmatism,
always asking "will this actually work in the real world?"

You excel at:
- Practical problem-solving
- Social dynamics analysis
- Resource and feasibility assessment
- Implementation planning""",
        tools=tools,
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
    
    return {
        "melchior": melchior,
        "balthasar": balthasar,
        "casper": casper
    }


def analyze_question_with_stats(
    question: str,
    provider: str = "groq",
    ollama_model: str = None,
    enable_search: bool = False,
    temperature: float = 0.5
) -> Dict[str, Any]:
    """
    Analyze a question using MAGI system with token usage statistics
    """
    # Initialize LLM
    if provider == "ollama" and ollama_model:
        llm = LLM(model=f"ollama/{ollama_model}", temperature=temperature)
    else:
        llm = get_model(provider, temperature)
    
    # Create agents
    agents = create_magi_agents(llm, enable_search)
    
    # Create tasks
    tasks = [
        Task(
            description=f"""Analyze this question from your scientific perspective:

Question: {question}

Provide analysis focusing on:
- Relevant data and facts
- Logical reasoning and evidence
- Scientific principles
- Quantifiable metrics

Be thorough, objective, and grounded in verifiable information.""",
            expected_output="Scientific analysis with data-driven insights and logical conclusions",
            agent=agents["melchior"]
        ),
        
        Task(
            description=f"""Analyze this question from your ethical perspective:

Question: {question}

Provide analysis focusing on:
- Ethical implications and moral considerations
- Impact on human welfare and dignity
- Benefits and harms to stakeholders
- Alignment with moral principles

Be empathetic, principled, and human-centered.""",
            expected_output="Ethical analysis considering human impact and moral implications",
            agent=agents["balthasar"]
        ),
        
        Task(
            description=f"""Analyze this question from your practical perspective:

Question: {question}

Provide analysis focusing on:
- Real-world feasibility and implementation
- Social and cultural considerations
- Resource requirements and constraints
- Actionable recommendations

Be pragmatic, realistic, and implementation-focused.""",
            expected_output="Practical analysis with feasibility assessment and actionable insights",
            agent=agents["casper"]
        )
    ]
    
    # Create crew
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True,
        process="sequential"
    )
    
    # Execute analysis
    result = crew.kickoff()
    
    # Calculate token usage (approximate based on text length)
    # Note: CrewAI doesn't expose token usage directly, so we estimate
    result_text = str(result)
    estimated_tokens = len(result_text.split()) * 1.3  # Rough estimate
    
    # Estimate costs (Groq is free, OpenAI varies)
    cost_per_token = 0.0 if provider == "groq" else 0.000002  # OpenAI gpt-4o-mini approx
    estimated_cost = estimated_tokens * cost_per_token
    
    token_stats = {
        "total_input_tokens": int(len(question.split()) * 1.3),
        "total_output_tokens": int(estimated_tokens),
        "total_tokens": int((len(question.split()) + len(result_text.split())) * 1.3),
        "estimated_cost": estimated_cost
    }
    
    return {
        "question": question,
        "provider": provider,
        "result": result_text,
        "status": "completed",
        "token_stats": token_stats
    }
