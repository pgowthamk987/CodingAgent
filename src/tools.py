from google.adk.tools import FunctionTool

def explain_code(code: str, language: str = "auto") -> str:
    """Explains what a piece of code does in simple terms."""
    return f"Explain this {language} code step by step in simple terms, covering what each part does:\n\n{code}"

def debug_code(code: str, error: str = "no error message") -> str:
    """Debugs code and suggests a fix."""
    return f"This code has a bug. Error: {error}\n\nCode:\n{code}\n\nDiagnose the root cause and provide a fixed version."

def generate_code(description: str, language: str = "Python") -> str:
    """Generates code from a natural language description."""
    return f"Write clean, working {language} code for: {description}\n\nInclude comments explaining key parts."

def dsa_solver(problem: str) -> str:
    """Solves DSA problems with time and space complexity analysis."""
    return f"Solve this DSA problem step by step:\n{problem}\n\nInclude: approach, code solution, time complexity, space complexity."

# Wrap as ADK FunctionTools
explain_tool = FunctionTool(explain_code)
debug_tool = FunctionTool(debug_code)
generate_tool = FunctionTool(generate_code)
dsa_tool = FunctionTool(dsa_solver)