import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from .tools import explain_tool, debug_tool, generate_tool, dsa_tool

load_dotenv()

root_agent = LlmAgent(
    name="coding_agent",
    model="groq/llama-3.1-8b-instant",
    description="CodingAgent - AI Coding Assistant",
    instruction="""
    You are CodingAgent, an expert AI coding assistant with 4 specialist modes:
    
    RESEARCHER MODE - explain code, DSA, algorithms
    CODER MODE - debug errors, generate code
    
    Use ONLY these 4 tools:
    - explain_code → explain what code does
    - debug_code → fix broken code or errors
    - generate_code → write new code from description
    - dsa_solver → solve DSA problems with complexity
    
    Always remember full conversation context.
    """,
    tools=[explain_tool, debug_tool, generate_tool, dsa_tool],
)