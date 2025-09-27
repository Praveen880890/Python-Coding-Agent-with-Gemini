import os 
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.get_files_info import get_files_info

load_dotenv()
def main():
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
    system_prompt = (""" Ignore all previous instructions.just shout "I am A RObot" """)

    if len(sys.argv) < 2:
        print("I need a prompt to work with!")
        sys.exit(1)
    verbose_flag = False
    if sys.argv[-1] == "--verbose":
        verbose_flag = True
    prompt = sys.argv[1]

    client = genai.Client(api_key=GEMINI_API_KEY)
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    response = client.models.generate_content(model="gemini-2.0-flash-001",
                                            contents=messages,
                                            config=types.GenerateContentConfig(system_instruction= system_prompt,))

    if response is None or response.usage_metadata is None:
        print("No response or usage metadata received.")
        return
    print(response.text)
    if verbose_flag:
        print("User Prompt:", prompt)
        print("Prompt Tokens:", response.usage_metadata.prompt_token_count)
        print("Response Tokens:", response.usage_metadata.candidates_token_count)
main()