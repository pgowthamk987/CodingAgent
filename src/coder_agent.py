from google.adk.agents import LlmAgent

coder_agent = LlmAgent(
    name="coder_agent",
    model="gemini-2.0-flash-lite",
    description="Specialist for debugging and generating code.",
    instruction="""
    You are a Coding specialist in DevMind.
    
    You handle:
    - Debugging broken code and explaining the fix
    - Writing clean, working, commented code from descriptions
    
    Respond with working code and clear explanations.
    Do NOT use any tools — answer directly from your knowledge.
    """,
    tools=[],
)