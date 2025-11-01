# Multi-Agent Debate DAG: LangGraph System

This repository implements a CLI-based debate simulator using LangGraph, featuring two AI agents (Scientist & Philosopher) debating over a fixed topic with controlled rounds, memory, validation, and automated judging. The workflow leverages modular nodes to structure the debate, memory management, logging, and verdict generation.

---

## Table of Contents

- [Project Overview](#project-overview)
- [File Structure and Analysis](#file-structure-and-analysis)
- [Installation](#installation)
- [Usage](#usage)
- [Node & DAG Structure](#node--dag-structure)
- [Logging](#logging)
- [Debate Example](#debate-example)
- [Deliverables](#deliverables)

---

## Project Overview

This system enables simulation of structured debates between two professional personas (Scientist vs Philosopher) for exactly 8 rounds, with:
- Controlled turn-taking
- Argument uniqueness and memory handling
- Logic-based judgment
- Full logging of all transitions, memory, and responses
- A DAG diagram illustrating workflow

---

## File Structure and Analysis

- **main.py**: Entry point for CLI-based debate simulation. Orchestrates node initialization, manages debate rounds, enforces validation, handles turn alternation, updates memory, interfaces logging, and calls the judge for the final verdict. Defensive error handling is included to skip faulty agent/API responses.

- **user_input_node.py**: Simple input node that prompts user for the debate topic via CLI, returning the topic for downstream nodes.

- **agent_a_node.py** / **agent_b_node.py**: Define the two debate agent personas (`Scientist` and `Philosopher`). Each uses the LLM API to generate arguments conditioned on the topic, turn, and opponent's prior statement, ensuring persuasive, relevant, non-repetitive arguments.

- **memory_node.py**: Centralized debate memory. Stores argument tuples, exposes methods to update memory, retrieve the last opponent's argument for context, and compile a full debate transcript. Ensures each agent only gets relevant past information.

- **judge_node.py**: Automated judging node utilizing an LLM to review the full transcript, produce a summary, declare the debate winner, and explain its logic. Splits and returns summary blocks for integration and logging.

- **llm.py**: Implements LLM interfacing logic for both agent argument construction and judging. Uses OpenRouter API with proper context handling, model selection, system/user prompts, and temperature control. Robust error handling for absent keys or API failures.

- **validation.py**: Debate state validation helpers. Ensures:
    - Turn order is enforced (odd rounds: Scientist, even rounds: Philosopher)
    - Arguments are unique (not repeated)
    - Defensive checks for empty or erroneous responses.

- **logger.py**: Logging utility. Sets up consistent logging with timestamps and levels, appends all transitions/messages to `logs/debate_log.txt`, and prints to CLI for real-time feedback.

- **dg.py**: Generates the static DAG diagram of the debate workflow using `graphviz`. Enumerates nodes (UserInputNode, MemoryNode, AgentA, AgentB, JudgeNode), edges (memory flow, turn logic, judgment), and saves/opens the output.

- **debate_dag.jpg**: Visual representation of DAG architecture, mapping system nodes and their data/control flows (see included image).

- **requirements.txt**: Python dependencies. Required packages include:
    - `langgraph`
    - `graphviz`
    - `logging`
    - `python-dotenv`

---

## Installation

1. **Clone the repository** or unzip the deliverable folder.
2. **Install requirements**:
    ```
    pip install -r requirements.txt
    ```
3. **Setup OpenRouter API Key**:
    - Place your API key in a `.env` file as `OPENROUTERAPIKEY=<your-key>`

---

## Usage

Run the main program from your CLI:
    python main.py

- Enter your debate topic when prompted.
- Follow the round-by-round CLI messages.
- After 8 rounds, the judge node will summarize and declare the winner.
- Logs are written to `logs/debate_log.txt`.

---

## Node & DAG Structure

### Key Nodes:
- **UserInputNode**: Gets debate topic from user.
- **AgentA (Scientist)**
- **AgentB (Philosopher)**
- **MemoryNode**: Tracks argument history.
- **JudgeNode**: Summarizes & evaluates debate.

### Data Flow:
1. **User inputs topic** → stored in MemoryNode.
2. **Agents alternate turns** (exactly 8 rounds).
3. **Each agent receives only relevant argument history** before responding.
4. **MemoryNode updates after each argument**.
5. **JudgeNode reviews full transcript after round 8** → outputs summary, winner, and reasoning.
6. **Logger records all transitions.**
7. **DAG visualized in `debate_dag.jpg`.**

---

## Logging

- Logs are handled in `logger.py`, recording every step, response, memory update, and judgment.
- All logs are output to both CLI and the persistent file (`logs/debate_log.txt`) for review/audit.

---

## Debate Example

- Enter topic for debate: Should AI be regulated like medicine?
- Starting debate between Scientist and Philosopher...
- [Round 1] Scientist: AI must be regulated due to high-risk applications.
- [Round 2] Philosopher: Regulation could stifle philosophical progress and autonomy.
- ...
- [Judge] Summary of debate: ...
- [Judge] Winner: Scientist
- Reason: Presented more grounded, risk-based arguments aligned with public safety principles






