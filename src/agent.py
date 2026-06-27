import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from .tools import explain_tool, debug_tool, generate_tool, dsa_tool

load_dotenv()

root_agent = LlmAgent(
    name="coding_agent",
    model="groq/llama-3.1-8b-instant",
    description="DevMind - AI Coding Assistant that explains, debugs, and generates code.",
    instruction="""
    You are DevMind, an expert AI coding assistant. You help developers by:
    - Explaining code clearly and simply
    - Debugging errors and suggesting fixes
    - Generating clean, working code from descriptions
    - Solving DSA problems with time/space complexity
    - Searching the web for documentation and answers
    
    Always pick the most relevant tool for the user's query.
    Be concise, clear, and practical in your responses.

    IMPORTANT: Never call any tool that is not in this list.
    If unsure, answer directly without using any tool.
    """,
    tools=[explain_tool, debug_tool, generate_tool, dsa_tool],
)