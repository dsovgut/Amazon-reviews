# Multimodal E-commerce AI Advisor (Chainlit Frontend)

This project is the Chainlit-based user interface for a multimodal conversational AI designed for e-commerce. It allows users to ask questions about products using text and by uploading product images. The frontend is built to interact with a sophisticated RAG (Retrieval-Augmented Generation) backend that processes both text and visual information from the Amazon Product Dataset 2020.

## Project Context & Goals

* **Multimodal Interaction:** Users can input queries via text and/or upload product images.
* **RAG Backend:** The frontend will communicate with a RAG system (to be developed by teammates) that utilizes models like CLIP for image/text embeddings and an LLM (e.g., Llama-3.1 or Mixtral) for generating responses.
* **Knowledge Base:** The RAG system will primarily use the Amazon Product Dataset 2020.
* **User Experience:** Provide an intuitive chat interface for seamless interaction.

## Project Structure Highlights

* **`app/main.py`**: The core Python script containing the Chainlit application logic, UI event handlers, and the integration point for the multimodal RAG backend.
* **`public/`**: This folder contains static assets such as logos and other branding elements. Ensure file names for assets (e.g., logos referenced in `chainlit.toml` or the app's configuration) are exact.
* **`requirements.txt`**: Lists all Python libraries and their versions required to run this frontend application.
* **`chainlit.md`**: Defines the content of the welcome screen or initial UI elements displayed when the chat interface loads (if no initial message is sent by `on_chat_start`).
* **`chainlit.toml`**: Configuration file for customizing Chainlit's appearance (theme, project name) and behavior.
* **`.env` File (Crucial for API Keys):**
    * This project may require an `.env` file in the root directory to store sensitive information like API keys (e.g., `OPENAI_API_KEY` if any direct LLM calls are made from the frontend, or API keys for services the RAG backend might expose).
    * **The `.env` file should NOT be committed to GitHub for security reasons.**
    * It's recommended to create a `.env.example` file (and commit that instead) listing the required environment variables with placeholder values (e.g., `OPENAI_API_KEY=YOUR_KEY_HERE`). Teammates will need to create their own `.env` file by copying the example and filling in their actual keys.

## Setup and Running the Application

This application is best developed and run using a code editor like VS Code with its integrated terminal.

**1. Get the Code:**

* **Option A: Clone from GitHub (Recommended for collaboration):**
    ```bash
    git clone <repository_url>
    cd <repository_folder_name> 
    ```
    (Replace `<repository_url>` and `<repository_folder_name>` with actual names)
* **Option B: Download Files Manually:**
    If you've received the project files (e.g., as a ZIP archive), extract them into a single project folder. Navigate into this folder using your terminal.

**2. Create and Activate a Python Virtual Environment (Essential!):**
A virtual environment ensures that project-specific dependencies are isolated and don't conflict with other Python projects or your global Python installation.

In your terminal, from the project's root folder (e.g., `Amazon-Review`):
```bash
# Create a virtual environment named .venv
python3 -m venv .venv

# Activate the virtual environment:
# On macOS/Linux:
source .venv/bin/activate
# On Windows (using Git Bash or PowerShell):
# .venv\Scripts\activate
# On Windows (Command Prompt):
# .venv\Scripts\activate.bat
