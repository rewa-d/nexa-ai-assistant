# NEXA — Neural Executive Assistant

**NEXA** is a locally running, tool-enabled AI personal assistant built with Python and Ollama.

The project explores agentic AI by combining a local large language model with conversation memory, function calling, and controlled desktop automation.

NEXA is being developed as a portfolio project, with the long-term goal of creating a JARVIS-style desktop assistant.

## Current Features

- **Local AI conversations:** Powered by Qwen3 4B through Ollama.
- **Conversation memory:** Maintains recent conversation context, with a command to reset memory.
- **Calculator:** Performs addition, subtraction, multiplication, and division.
- **Date and time:** Retrieves local system time and supports international timezones.
- **File search:** Searches filenames within the NEXA project directory.
- **Mac application launcher:** Opens applications from a predefined allowlist.
- **Tool registry:** Centralises approved tools and their execution.
- **Multi-step tool execution:** Supports multiple rounds of model-driven tool calls, with an execution limit.
- **Custom assistant personality:** Designed for clear, professional, conversational responses.

## Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python 3.12 |
| Local language model | Qwen3 4B |
| Model runtime | Ollama |
| Tool calling | Ollama Python SDK |
| Development environment | PyCharm |
| Operating system | macOS |
| Version control | Git and GitHub |

## Project Structure

```text
nexa-ai-assistant/
├── src/
│   ├── main.py
│   ├── llm.py
│   └── tools/
│       ├── __init__.py
│       ├── calculator.py
│       ├── date_time.py
│       ├── file_search.py
│       ├── app_launcher.py
│       └── registry.py
├── tests/
│   ├── test_calculator.py
│   └── test_llm.py
├── README.md
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.12
- macOS
- Ollama installed and running
- Qwen3 4B model downloaded

### Installation

Clone the repository:

```bash
git clone https://github.com/rewa-d/nexa-ai-assistant.git
cd nexa-ai-assistant
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the Ollama Python package:

```bash
python -m pip install ollama
```

Download the language model:

```bash
ollama pull qwen3:4b
```

Ensure Ollama is running, then launch NEXA:

```bash
python -m src.main
```

## Example Commands

```text
You: Hello NEXA!

You: Explain how neural networks work.

You: Calculate 125 multiplied by 48.

You: What is the current time on my Mac?

You: What time is it in Melbourne?

You: Find calculator.py in my project.

You: Open Calculator on my Mac.
```

### CLI Commands

- `help` — Display available commands.
- `clear` — Reset conversation memory.
- `exit` — Close NEXA.

## Architecture

NEXA follows a modular architecture:

```text
User
  |
  v
Command-Line Interface
  |
  v
Conversation Manager
  |
  v
Ollama / Qwen3 4B
  |
  v
Tool Registry
  |
  +-- Calculator
  +-- Date and Time
  +-- File Search
  +-- Application Launcher
  |
  v
Tool Results
  |
  v
Language Model
  |
  v
User Response
```

The language model determines when to request a tool. The registry validates the requested tool name, executes approved functions, and returns results to the model.

## Safety and Limitations

- The application launcher uses an explicit allowlist.
- File search is limited to the project directory and is read-only.
- Tool execution is restricted to registered Python functions.
- A maximum tool-round limit prevents unbounded tool-calling loops.
- Conversation memory is temporary and resets when NEXA closes.
- Model responses and tool selection may occasionally be inaccurate.
- The application launcher currently executes approved requests without an additional confirmation prompt.
- The desktop interface and voice capabilities are not yet implemented.

## Development Roadmap

| Phase | Focus | Status |
|---|---|---|
| Phase 1 | Project setup and local LLM integration | Complete |
| Phase 2 | Personality and short-term memory | Complete |
| Phase 3 | Agentic tools and desktop automation | Implemented; final checks pending |
| Phase 4 | Floating desktop assistant and expandable dashboard | Planned |
| Phase 5 | Voice interaction | Planned |
| Phase 6 | Persistent memory and advanced automation | Planned |

## Future Improvements

- Floating desktop assistant using PySide6.
- Expandable dashboard for assistant interactions.
- Speech recognition and text-to-speech.
- Persistent memory across sessions.
- Confirmation controls for sensitive actions.
- Improved tool execution reliability.
- Expanded macOS integrations.
- Automated integration testing.

## Project Purpose

NEXA is a hands-on exploration of agentic AI, local large language models, function calling, and practical AI application development.

The objective is to build an assistant that goes beyond answering questions and can safely interact with tools and desktop applications.

## Author

**Rewa Dambal**

Master of Artificial Intelligence — RMIT University

[GitHub](https://github.com/rewa-d) | [LinkedIn](https://www.linkedin.com/in/rewa-dambal/)

---

*Currently under active development.*
