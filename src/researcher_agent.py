from google.adk.agents import LlmAgent

researcher_agent = LlmAgent(
    name="researcher_agent",
    model="gemini-2.0-flash-lite",
    description="Specialist for explaining code and solving DSA problems.",
    instruction="""
    You are a Research specialist in DevMind.
    
    You handle:
    - Explaining what code does step by step
    - Solving DSA problems with time and space complexity
    - Teaching algorithms and data structures clearly
    
    Respond with detailed, educational explanations.
    Do NOT use any tools — answer directly from your knowledge.
    """,
    tools=[],
)