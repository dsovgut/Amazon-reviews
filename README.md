Multimodal E-commerce AI Advisor (Chainlit Frontend)
This project is the Chainlit-based user interface for a multimodal conversational AI designed for e-commerce. It allows users to ask questions about products using text and by uploading product images. The frontend is built to interact with a sophisticated RAG (Retrieval-Augmented Generation) backend that processes both text and visual information from the Amazon Product Dataset 2020.

Project Context & Goals
Multimodal Interaction: Users can input queries via text and/or upload product images.

RAG Backend: The frontend will communicate with a RAG system (to be developed by teammates) that utilizes models like CLIP for image/text embeddings and an LLM (e.g., Llama-3.1 or Mixtral) for generating responses.

Knowledge Base: The RAG system will primarily use the Amazon Product Dataset 2020.

User Experience: Provide an intuitive chat interface for seamless interaction.

Project Structure Highlights
app/main.py: The core Python script containing the Chainlit application logic, UI event handlers, and the integration point for the multimodal RAG backend.

public/: This folder contains static assets such as logos and other branding elements. Ensure file names for assets (e.g., logos referenced in chainlit.toml or the app's configuration) are exact.

requirements.txt: Lists all Python libraries and their versions required to run this frontend application.

chainlit.md: Defines the content of the welcome screen or initial UI elements displayed when the chat interface loads (if no initial message is sent by on_chat_start).

chainlit.toml: Configuration file for customizing Chainlit's appearance (theme, project name) and behavior.

.env File (Crucial for API Keys):

This project may require an .env file in the root directory to store sensitive information like API keys (e.g., OPENAI_API_KEY if any direct LLM calls are made from the frontend, or API keys for services the RAG backend might expose).

The .env file should NOT be committed to GitHub for security reasons.

It's recommended to create a .env.example file (and commit that instead) listing the required environment variables with placeholder values (e.g., OPENAI_API_KEY=YOUR_KEY_HERE). Teammates will need to create their own .env file by copying the example and filling in their actual keys.

Setup and Running the Application
This application is best developed and run using a code editor like VS Code with its integrated terminal.

1. Get the Code:

Option A: Clone from GitHub (Recommended for collaboration):

git clone <repository_url>
cd <repository_folder_name> 

(Replace <repository_url> and <repository_folder_name> with actual names)

Option B: Download Files Manually:
If you've received the project files (e.g., as a ZIP archive), extract them into a single project folder. Navigate into this folder using your terminal.

2. Create and Activate a Python Virtual Environment (Essential!):
A virtual environment ensures that project-specific dependencies are isolated and don't conflict with other Python projects or your global Python installation.

In your terminal, from the project's root folder (e.g., Amazon-Review):

# Create a virtual environment named .venv
python3 -m venv .venv

# Activate the virtual environment:
# On macOS/Linux:
source .venv/bin/activate
# On Windows (using Git Bash or PowerShell):
# .venv\Scripts\activate
# On Windows (Command Prompt):
# .venv\Scripts\activate.bat

Once activated, your terminal prompt should be prefixed with (.venv).

3. Install Required Libraries:
With the virtual environment active, install all the dependencies listed in requirements.txt:

pip install -r requirements.txt

4. Set Up Environment Variables (if applicable):

If the project requires API keys or other configuration via environment variables:

Create a file named .env in the root of the project directory.

If a .env.example file is provided, copy its content into your .env file.

Add the necessary values. For example:

OPENAI_API_KEY=sk-your_actual_openai_api_key_here 
# Add other RAG-backend related API keys or endpoints if needed

5. Run the Chainlit Application:
After completing the setup and ensuring your virtual environment is active, run the application using the following command in the terminal (from the project's root directory):

chainlit run app/main.py -w --port 8019

The -w (watch) flag enables auto-reload, so the application updates if you make changes to the Python code.

--port 8019 specifies the port the application will run on. You can change this (e.g., to 8001 or any other available port) if 8019 is already in use.

The application should then be accessible in your web browser at http://localhost:8019 (or the port you specified).

Multimodal RAG Backend Integration Point
For the teammate(s) responsible for the Multimodal RAG backend:

The primary integration point for your RAG system is within the app/main.py script, specifically the asynchronous function:

async def get_ecommerce_multimodal_rag_response(text_query: str, image_file_details: Optional[Dict], chat_history: Optional[List[Dict]]) -> Dict:

This function is currently a placeholder and needs to be implemented with the actual logic of your multimodal RAG system.

Inputs it receives from the frontend:

text_query (str): The user's textual question.

image_file_details (Optional[Dict]): A dictionary containing {"name": str, "path": str} if the user uploaded an image. Your RAG system will use the path to access the temporary image file for processing (e.g., with CLIP).

chat_history (Optional[List[Dict]]): The conversation history, which might be useful for context.

Your RAG implementation should:

Process the text_query and the image (if image_file_details is provided) using models like CLIP.

Perform retrieval from the vector database containing embeddings from the Amazon Product Dataset 2020 (both text and image embeddings).

Augment the query/context with the retrieved information.

Call the appropriate Large Language Model (e.g., Llama-3.1 or Mixtral) to generate a final, context-aware answer.

Return a dictionary with the following structure:

{
    "text": "The textual response from the LLM.",
    "image_url": "URL_of_a_relevant_product_image_or_None" 
}

The image_url should be a publicly accessible URL or a path that Chainlit can serve if your RAG system retrieves a relevant product image from the dataset.

The main message handling logic (@cl.on_message) in app/main.py is already set up to:

Detect image uploads from the user.

Call get_ecommerce_multimodal_rag_response.

Display the returned text and any accompanying image in the Chainlit UI.

Good luck with the integration!
