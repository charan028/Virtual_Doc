import os

from groq import Groq

api_key=os.environ.get("GROQ_API_KEY")  # Use environment variable or fallback to hardcoded key
# print(api_key)
# client = Groq(
#     api_key=api_key
#     # os.environ.get("GROQ_API_KEY"),
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Explain the importance of fast language models",
#         }
#     ],
#     model="llama-3.3-70b-versatile",
# )

# print(chat_completion.choices[0].message.content)




# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1: Setup GROQ API key
import os

GROQ_API_KEY=api_key

#Step2: Convert image to required format
import base64


image_path="acne.png"
image_file=open(image_path, "rb")
# encoded_image=base64.b64encode(image_file.read()).decode('utf-8')
def encode_image(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

#Step3: Setup Multimodal LLM 
from groq import Groq

query="Is there something wrong with my face?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"
#model="llama-3.2-90b-vision-preview" #Deprecated
# client=Groq(api_key=GROQ_API_KEY)  
# messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text", 
#                     "text": query
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{encoded_image}",
#                     },
#                 },
#             ],
#         }]
# chat_completion=client.chat.completions.create(
#         messages=messages,
#         model=model
#     )
# print(chat_completion.choices[0].message.content)


def analyze_image_with_query(query, model, encoded_image):
    client=Groq()  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content