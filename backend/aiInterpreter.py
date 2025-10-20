#This is where it will handle the user's requests and translate it into actual instructors for python script to undersatnd

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#will let ai determine what your command is 
def interpret_instruction(instruction_command):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",  
        headers={
            "Authorization": f"Bearer {os.getenv('API_KEY')}",  
        },
        json={  
            "model": "openai/gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": "Convert this automation testing request to JSON commands: " + instruction_command + ". Format as JSON array: [{\"type\": \"go_page\", \"url\": \"url\"}, {\"type\": \"click_button\", \"buttonName\": \"button\"}, {\"type\": \"fill_form\", \"formType\": \"textbox\", \"formName\": \"field\", \"inputData\": \"data\"}]"
                }
            ]
        }
    )
    
    # Debug: Print response for testing
    result = response.json()
    print(f"AI Response Status: {response.status_code}")
    print(f"AI Response: {result}")
    
    return result['choices'][0]['message']['content']

def main():
    instruction = "help me login into wellsfargo workday account, my email is jamesma765@gmail.com, and password is Dugong05!"
    interpret_instruction(instruction)
    
if __name__ == "__main__":
    main()