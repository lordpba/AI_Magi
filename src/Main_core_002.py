"""
MAGI System - Multi-Agent General Intelligence v2.0
Modern CrewAI Implementation (No LangChain Required)

Based on Neon Genesis Evangelion's MAGI supercomputer system.
Three agents provide different perspectives on any question:
- Melchior: Scientific/logical perspective
- Balthasar: Ethical/emotional perspective
- Casper: Practical/social perspective
"""

import os
from typing import Dict, Any
from pathlib import Path
from dotenv import load_dotenv

# Modern CrewAI imports - No LangChain needed!
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool

# Load environment variables from config/.env
config_path = Path(__file__).parent.parent / "config" / ".env"
load_dotenv(config_path)


def get_model(provider: str = "groq", temperature: float = 0.5) -> LLM:
    """
    Get LLM instance using modern CrewAI API.
    
    CrewAI now uses LiteLLM internally, supporting multiple providers
    with a unified interface. Model format: "provider/model-name"
    
    Args:
        provider: LLM provider ("groq" or "openai")
        temperature: Sampling temperature (0.0-1.0)
        
    Returns:
        LLM instance configured for the MAGI system
        
    Environment Variables Required:
        - GROQ_API_KEY: For Groq models
        - OPENAI_API_KEY: For OpenAI models
    """
    if provider == "groq":
        # Groq models - fast and cost-effective
        # llama-3.1-8b-instant: Fast, no rate limits (recommended for free tier)
        # llama-3.3-70b-versatile: More powerful but has rate limits
        # Other options: llama-3.1-70b-versatile, gemma2-9b-it
        return LLM(
            model="groq/llama-3.1-8b-instant",
            temperature=temperature
        )
    elif provider == "openai":
        # OpenAI models - high quality
        return LLM(
            model="openai/gpt-4o-mini",
            temperature=temperature
        )
    else:
        # Default to Groq with fastest model
        return LLM(
            model="groq/llama-3.1-8b-instant",
            temperature=temperature
        )


def create_magi_agents(llm: LLM, enable_search: bool = True) -> Dict[str, Agent]:
    """
    Create the three MAGI system agents with distinct personalities.
    
    Each agent represents a different aspect of Dr. Naoko Akagi's personality,
    providing diverse perspectives on any issue.
    
    Args:
        llm: The language model to use for all agents
        enable_search: Whether to enable internet search capability
    
    Returns:
        Dictionary with three agents: melchior, balthasar, casper
    """
    # Initialize search tool if enabled
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


def analyze_question(
    question: str, 
    provider: str = "groq",
    ollama_model: str = None,
    enable_search: bool = True,
    temperature: float = 0.5
    ) -> Dict[str, Any]:
    """
    Analyze a question using the MAGI three-perspective system.
    
    The question is evaluated independently by three agents representing different
    perspectives, mimicking the MAGI supercomputer from Evangelion.
    
    Args:
        question: The question or problem to analyze
        provider: LLM provider ("groq" or "openai")
        enable_search: Whether agents can search the internet
        temperature: LLM temperature (0.0-1.0, higher = more creative)
        
    Returns:
        Dictionary containing analyses from all three agents
        
    Example:
        >>> result = analyze_question("Should we invest in AI safety?")
        >>> print(result['result'])
    """
    print(f"\n{'='*80}")
    print("MAGI SYSTEM INITIALIZING")
    print(f"{'='*80}")
    print(f"Question: {question}")
    print(f"Provider: {provider}")
    print(f"Search enabled: {enable_search}")
    print(f"{'='*80}\n")
    
    # Initialize LLM
    if provider == "ollama" and ollama_model:
        llm = LLM(model=f"ollama/{ollama_model}", temperature=temperature)
    else:
        llm = get_model(provider, temperature)
    
    # Create the three MAGI agents
    agents = create_magi_agents(llm, enable_search)
    
    # Create individual tasks for each agent
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
    
    # Create crew with all agents and tasks
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True,
        process="sequential"  # Each agent analyzes independently
    )
    
    # Execute MAGI analysis
    print("\n" + "="*80)
    print("EXECUTING MAGI ANALYSIS...")
    print("="*80 + "\n")
    
    result = crew.kickoff()
    
    # Format results
    output = {
        "question": question,
        "provider": provider,
        "result": str(result),
        "status": "completed"
    }
    
    print("\n" + "="*80)
    print("MAGI ANALYSIS COMPLETE")
    print("="*80 + "\n")
    
    return output


def main():
    """
    Main entry point for testing the MAGI system.
    """
    print("\n" + "="*80)
    print("MAGI SYSTEM - MULTI-AGENT GENERAL INTELLIGENCE")
    print("Based on Neon Genesis Evangelion")
    print("="*80 + "\n")
    
    # Example question
    test_question = "Should we invest heavily in renewable energy infrastructure?"
    
    # Run analysis
    result = analyze_question(
        question=test_question,
        provider="groq",  # Change to "openai" if you have OpenAI API key
        enable_search=True,
        temperature=0.5
    )
    
    # Display results
    print("\n" + "="*80)
    print("FINAL RESULTS")
    print("="*80)
    print(f"\nQuestion: {result['question']}")
    print(f"\nProvider: {result['provider']}")
    print(f"\nStatus: {result['status']}")
    print(f"\n{'-'*80}")
    print("MAGI System Analysis:")
    print(f"{'-'*80}")
    print(f"\n{result['result']}")
    print("\n" + "="*80 + "\n")


if __name__ == "__main__":
    main()
