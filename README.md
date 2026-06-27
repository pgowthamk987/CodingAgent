# 🧠 CodingAgent — AI Coding Assistant

> An intelligent coding assistant agent built with **Google ADK** and **Groq**, featuring 4 specialized tools for code explanation, debugging, generation, and DSA problem solving.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Google ADK](https://img.shields.io/badge/Google%20ADK-latest-orange?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-LLaMA%203.1-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)

---

## ✨ Features

- 📖 **Code Explainer** — Breaks down any code snippet step by step in simple language
- 🐛 **Code Debugger** — Identifies bugs, explains root cause, and provides fixed code
- ⚙️ **Code Generator** — Generates clean, commented code from natural language descriptions
- 🧠 **DSA Solver** — Solves algorithm problems with time and space complexity analysis
- 💬 **Conversation Memory** — Remembers context across the entire session
- 🏗️ **Multi-Agent Design** — Researcher and Coder specialist agents architecture

---

## 🏗️ Architecture

```
User Input
    ↓
CodingAgent (Google ADK + Groq LLaMA 3.1)
    ├── explain_code tool     → Code explanation
    ├── debug_code tool       → Bug diagnosis + fix
    ├── generate_code tool    → Code generation
    └── dsa_solver tool       → DSA + complexity analysis
    ↓
ADK Session (Conversation Memory)
    ↓
Response
```

### Multi-Agent Design (Designed)
```
Orchestrator (coding_agent)
    ├── researcher_agent   → Explains code, solves DSA
    └── coder_agent        → Debugs, generates code
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Agent Framework | Google ADK |
| LLM | Groq — LLaMA 3.1 8B Instant |
| Tool System | ADK FunctionTools |
| Memory | ADK InMemory Session |
| Language | Python 3.10+ |

---

## 📁 Project Structure

```
CodingAgent/
├── src/
│   ├── agent.py              ← Root agent +orchestrator
│   ├── tools.py              ← 4 custom FunctionTools
│   ├── prompts.py            ← Prompt templates
│   ├── researcher_agent.py   ← Researcher specialist agent
│   └── coder_agent.py        ← Coder specialist agent
├── .env                      ← API keys (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Groq API key — [Get free key](https://console.groq.com)
- Google ADK — [Docs](https://google.github.io/adk-docs)

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/pgowthamk987/CodingAgent.git
cd CodingAgent

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Add your API keys to .env
```

### Environment Variables

Create a `.env` file in the root:
```
GROQ_API_KEY=your_groq_api_key_here
```

### Run

```bash
adk web
```

Opens at `http://localhost:8000` — chat with your agent in the browser.

---

## 💡 Usage Examples

**Explain code:**
```
Explain this code: def factorial(n): return 1 if n==0 else n * factorial(n-1)
```

**Debug code:**
```
Debug this: print(x) — error: NameError: name 'x' is not defined
```

**Generate code:**
```
Generate a Python function to check if a string is a palindrome
```

**Solve DSA:**
```
Solve binary search with time and space complexity
```

---

## 🧠 How It Works

CodingAgent uses Google ADK's **ReAct (Reason + Act)** pattern:

1. User sends a query
2. Agent reasons about which tool fits best
3. Agent calls the appropriate `FunctionTool`
4. Tool returns structured prompt to the LLM
5. LLM generates the response
6. ADK Session stores context for follow-up questions

---

## 📊 Tool Routing Logic

| User Query Contains | Tool Used |
|---|---|
| "explain", "what does this do" | `explain_code` |
| "debug", "error", "broken", "fix" | `debug_code` |
| "generate", "write", "create" | `generate_code` |
| "DSA", "algorithm", "complexity" | `dsa_solver` |

---

## 🗺️ Roadmap

- [x] 4 core FunctionTools
- [x] Conversation memory
- [x] Multi-agent architecture design
- [ ] Streamlit UI
- [ ] Web search tool integration
- [ ] Deploy on Streamlit Cloud
- [ ] Multi-agent with Gemini orchestrator

---

## 👨‍💻 Author

**Gowtham**
- 2nd Year CSE Student — VIT-AP University
- GitHub: [@pgowthamk987](https://github.com/pgowthamk987)

---

## 📄 License

MIT License — feel free to use and build on this project.