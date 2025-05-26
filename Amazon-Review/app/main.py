# app/main.py

# --- Imports ---
import chainlit as cl
from openai import AsyncOpenAI # Retained if RAG might use it, or for other direct LLM calls.
import os
from dotenv import load_dotenv
import asyncio # For async operations, like simulating RAG delay
from typing import Optional, List, Dict # Import Dict for return type hint

# ... (rest of your imports and setup) ...

ECOMMERCE_SYSTEM_PROMPT = """You are a friendly and knowledgeable AI E-commerce Assistant. 
Your goal is to help users find information about products from our catalog using text and images they provide. 
Prioritize information retrieved from the product database which includes product images and descriptions.
When a user uploads an image, use it to identify the product or understand their query in conjunction with any text provided.
If you can display an image of a product in your response (e.g., from the database), please do so if it's relevant.
Be helpful, concise, and accurate. Clearly state if your answer is based on information from the product database."""

# --- Placeholder for Multimodal RAG System Call ---
async def get_ecommerce_multimodal_rag_response(
    text_query: str,
    # When you identify an image element from msg.elements, it will be an instance of cl.Image
    # So, you can pass that specific type if you've already filtered for it.
    # Or, if you're passing a generic element before checking its type, cl. AbschElement might be more appropriate
    # if cl.Element itself is causing issues. Let's assume you'll pass a cl.Image object.
    image_file_details: Optional[Dict] = None, # Pass relevant details like path and name
    chat_history: Optional[List[Dict]] = None # Make chat_history optional if not always used
) -> Dict: # Return a dictionary
    """
    ### Teammate Integration Point ###
    This function will call the multimodal RAG system for e-commerce.

    Args:
        text_query (str): The user's text query.
        image_file_details (Optional[Dict]): A dictionary with details of the uploaded image 
                                             (e.g., {"name": str, "path": str}) if any.
        chat_history (Optional[List[Dict]]): The history of the conversation.

    Returns:
        dict: A dictionary potentially containing 'text' for the response 
              and 'image_url' if an image should be displayed with the response.
    """
    print(f"--- MULTIMODAL RAG SYSTEM CALL (Placeholder) ---")
    print(f"Text Query: '{text_query}'")
    
    rag_response_text = f"Placeholder RAG response for query: '{text_query}'."
    
    if image_file_details:
        print(f"Uploaded Image Name: {image_file_details['name']}")
        print(f"Uploaded Image Path (temp): {image_file_details['path']}")
        rag_response_text += f" You also uploaded an image named '{image_file_details['name']}'."
        # Teammate: Use image_file_details['path'] to access the image content

    await asyncio.sleep(1) # Simulate RAG processing time
    
    return {"text": rag_response_text, "image_url": None}


# --- Chainlit Event Handlers ---

@cl.on_chat_start
async def start_chat():
    cl.user_session.set("history", [{"role": "system", "content": ECOMMERCE_SYSTEM_PROMPT}])
    welcome_message = "Welcome to the E-commerce AI Advisor! How can I help you with our products today? You can ask questions or upload an image of a product."
    await cl.Message(content=welcome_message).send()
    print("E-commerce chat session started, history initialized with system prompt.")

@cl.on_message
async def handle_message(msg: cl.Message):
    chat_history = cl.user_session.get("history", [])
    
    user_text_query = msg.content if msg.content is not None else ""
    chat_history.append({"role": "user", "content": user_text_query})

    uploaded_image_details: Optional[Dict] = None # Store details as a dict
    
    if msg.elements:
        for element in msg.elements:
            # Check if the element is an image.
            # cl.Image is a more specific type you might expect for an image element.
            if isinstance(element, cl.Image): # Check if it's an Image element
                if element.path:
                    uploaded_image_details = {"name": element.name, "path": element.path}
                    await cl.Message(content=f"Processing your uploaded image: `{element.name}`...").send()
                    print(f"--- User uploaded image: {element.name}, Path: {element.path}, MIME: {element.mime} ---")
                    break 
                else:
                    await cl.Message(content=f"Sorry, there was an issue accessing the uploaded image: `{element.name}`.").send()
            # You could add checks for other element types if needed
            # elif element.mime and "image" in element.mime.lower(): # Fallback MIME check
            #     if element.path:
            #         uploaded_image_details = {"name": element.name, "path": element.path}
            #         # ... (as above) ...
            #         break

    try:
        rag_response_payload = await get_ecommerce_multimodal_rag_response(
            text_query=user_text_query,
            image_file_details=uploaded_image_details,
            chat_history=chat_history
        )

        response_text = rag_response_payload.get("text", "Sorry, I couldn't get a response.")
        response_image_url = rag_response_payload.get("image_url")

        response_ui_elements = []
        if response_image_url:
            response_ui_elements.append(
                cl.Image(url=response_image_url, name="Product Image", display="inline")
            )
        
        await cl.Message(
            content=response_text,
            elements=response_ui_elements if response_ui_elements else None
        ).send()

        chat_history.append({"role": "assistant", "content": response_text})

    except Exception as e:
        error_message = f"Sorry, an error occurred: {e}"
        await cl.Message(content=error_message).send()
        print(f"Error in RAG call or displaying response: {e}")

    cl.user_session.set("history", chat_history)