# 🤖 Agentic AI Python Coding Agent

This project implements a basic Agentic AI Python Coding Agent using the Google Gemini Flash API. Inspired by the freeCodeCamp.org tutorial "Guide to Agentic AI – Build a Python Coding Agent with Gemini" by Lane Wagner from boot.dev, this agent is designed to understand coding tasks, interact with a project's codebase, and modify/execute code autonomously to achieve a given goal.

## ✨ Features

* **Intelligent Task Execution:** Utilizes the Gemini Flash API to process user prompts and decide on appropriate actions.
* **Tool Calling:** The agent can "call" specific functions (tools) to interact with the file system and execute code.
* **Agentic Loop:** Continuously evaluates its actions, processes feedback from tool calls, and iterates until the user's request is satisfied.
* **File System Interaction:**
    * **`get_files_info`**: Lists files and directories within a specified path.
    * **`get_file_content`**: Reads and returns the content of a file, with truncation for large files.
    * **`write_file`**: Creates new files or overwrites existing ones.
* **Code Execution:**
    * **`run_python_file`**: Executes Python scripts and captures their standard output and error. Includes a timeout for safety.
* **Security Guardrails:** All file system and code execution operations are constrained to the project's working directory to prevent unauthorized access.
* **Verbose Output:** An optional `--verbose` flag for developers to see detailed agent prompts, token usage, and tool call arguments.

## ⚠️ Security Disclaimer

**This project is for educational purposes only and demonstrates fundamental concepts of AI agents. It is not intended for production use.** The agent's ability to execute arbitrary Python code, even within a constrained directory, carries inherent security risks. Always exercise caution when giving AI agents access to your file system or execution environment.

## 🚀 Getting Started

Follow these instructions to set up and run the Agentic AI.

### Prerequisites

* **Python 3.10+**
* **`uv` Package Manager:** Install `uv` for efficient dependency management.
    ```bash
    # Install uv (if not already installed)
    curl -proto '=https' --tlsv1.2 -sSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
    ```
* **Unix-like Shell:** (e.g., zsh, bash, or WSL on Windows)

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/agentic-ai-coding-agent.git](https://github.com/your-username/agentic-ai-coding-agent.git)
    cd agentic-ai-coding-agent
    ```

2.  **Initialize `uv` Project and Virtual Environment:**
    ```bash
    uv init
    uv venv
    source .venv/bin/activate # On Windows: .venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    uv add google-generativeai python-dotenv
    ```

4.  **Google Gemini API Key:**
    * Go to [Google AI Studio](https://aistudio.google.com/) and create a new API key.
    * Create a `.env` file in the root of your project:
        ```
        GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```
    * **Add `.env` to `.gitignore`** to prevent committing your API key:
        ```
        echo ".env" >> .gitignore
        ```

5.  **Set up the Calculator Project:**
    * Create a directory `calculator` in the root of your project.
    * Inside `calculator`, create a `pkg` directory.
    * Create the following files in their respective directories (copy content from the tutorial or provided examples):
        * `calculator/main.py`
        * `calculator/tests.py`
        * `calculator/pkg/calculator.py`
        * `calculator/pkg/render.py`
        * `calculator/lauram.txt` (fill with at least 20,000 characters of dummy text, e.g., from [Lorem Ipsum Generator](https://www.lipsum.com/))
    * You can verify the calculator works by navigating to the `calculator` directory and running:
        ```bash
        cd calculator
        uv run main.py "3 + 5"
        # Expected output: 8
        cd .. # Go back to root
        ```

### Running the Agent

You can interact with the agent via the command line.

RESULT :

<img width="1542" height="313" alt="image" src="https://github.com/user-attachments/assets/59b350ea-3d25-46b9-b181-5c146d1a04a8" />


```bash
uv run main.py "Your coding task or question here"
