# # import os
# # from dotenv import load_dotenv
# # from openai import OpenAI
# # import gradio as gr

# # load_dotenv()
# # api_key = os.getenv('OPENAI_API_KEY')
# # # 
# # # Check the key

# # if not api_key:
# #     print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
# # elif not api_key.startswith("sk-proj-"):
# #     print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
# # elif api_key.strip() != api_key:
# #     print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
# # else:
# #     print("API key found and looks good so far!")

# # openai = OpenAI()
# # MODEL = 'gpt-4o-mini'

# # system_message = "You are a helpful assistant"

# # system_message = "You are a helpful assistant in a clothes store. You should try to gently encourage \
# # the customer to try items that are on sale. Hats are 60% off, and most other items are 50% off. \
# # For example, if the customer says 'I'm looking to buy a hat', \
# # you could reply something like, 'Wonderful - we have lots of hats - including several that are part of our sales evemt.'\
# # Encourage the customer to buy hats if they are unsure what to get."

# # def chat(message, history):
# #     messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

# #     stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)

# #     response = ""
# #     for chunk in stream:
# #         response += chunk.choices[0].delta.content or ''
# #         yield response

# # gr.ChatInterface(fn=chat, type="messages").launch()





# import os
# from dotenv import load_dotenv
# from openai import OpenAI
# import gradio as gr

# # Load API Key
# load_dotenv()
# api_key = os.getenv('OPENAI_API_KEY')

# if not api_key:
#     print("No API key found! Set OPENAI_API_KEY in .env file.")
# elif not api_key.startswith("sk-proj-"):
#     print("Invalid API key format.")
# else:
#     print("API key verified.")

# # OpenAI Client
# openai = OpenAI()

# MODEL = 'gpt-4o-mini'

# # Customizable System Prompt
# default_system_message = (
#     "You are a helpful assistant in a clothes store. Encourage customers "
#     "to check out hats (60% off) and other sale items (50% off)."
# )

# # Enhanced Chat Function
# def chat(message, history):
#     messages = [{"role": "system", "content": default_system_message}] + history + [{"role": "user", "content": message}]

#     try:
#         response = openai.chat.completions.create(
#             model=MODEL,
#             messages=messages,
#             temperature=0.7,  # Make responses more natural
#             max_tokens=200,    # Limit response length
#             stream=True,
#         )

#         full_response = ""
#         for chunk in response:
#             content = chunk.choices[0].delta.content or ''
#             full_response += content
#             yield full_response  # Stream responses smoothly

#     except Exception as e:
#         yield f"⚠️ Error: {str(e)}"
        
        
# user_avatar_url = "avatar-icon.png"  
# assistant_avatar_url = "female1-512.png"  

# # Enhanced UI with Markdown & Avatars
# chatbot_ui = gr.ChatInterface(
#     fn=chat,
#     type="messages",
#     chatbot=gr.Chatbot(
#         avatar_images=(user_avatar_url, assistant_avatar_url), 
#         bubble_full_width=False,     # Prevent full-width responses
#     ),
#     theme="default",
#     title="Clothing Store Assistant 🏬",
#     description="Ask about our latest deals! 🛒"
    
# )


# # Run the Gradio App
# chatbot_ui.launch(server_name="0.0.0.0", server_port=7860)



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
