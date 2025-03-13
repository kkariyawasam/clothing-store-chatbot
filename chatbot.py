import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

# Load API Key
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("No API key found! Set OPENAI_API_KEY in .env file.")
elif not api_key.startswith("sk-proj-"):
    print("Invalid API key format.")
else:
    print("API key verified.")

# OpenAI Client
openai = OpenAI()

MODEL = 'gpt-4o-mini'

# Customizable System Prompt
default_system_message = (
    "You are a helpful assistant in a clothes store. Encourage customers "
    "to check out hats (60% off) and other sale items (50% off)."
)

# Enhanced Chat Function
def chat(message, history):
    messages = [{"role": "system", "content": default_system_message}] + history + [{"role": "user", "content": message}] 

    try:
        response = openai.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,  # Make responses more natural
            max_tokens=200,    # Limit response length
            stream=True,
        )

        full_response = ""
        for chunk in response:
            content = chunk.choices[0].delta.content or ''
            full_response += content
            yield full_response  # Stream responses smoothly

    except Exception as e:
        yield f"⚠️ Error: {str(e)}"
        
        
user_avatar_url = "avatar-icon.png"  
assistant_avatar_url = "female1-512.png"  

# Custom CSS for styling
css_styles = """
    .gradio-container {
        background-color: #11c7ca; 
        border-radius: 30px;         
        border: 5px solid #0f1b1c; 
    }

"""

# Enhanced UI with Markdown & Avatars
chatbot_ui = gr.ChatInterface(
    fn=chat,
    type="messages",
    chatbot=gr.Chatbot(
        avatar_images=(user_avatar_url, assistant_avatar_url), 
        bubble_full_width=False,     # Prevent full-width responses
    ),
    theme="default",
    title="Clothing Store Assistant 🏬",
    description="Ask about our latest deals! 🛒",
    css=css_styles  # Apply custom CSS styles
)

# Run the Gradio App
chatbot_ui.launch(server_name="0.0.0.0", server_port=7860)
