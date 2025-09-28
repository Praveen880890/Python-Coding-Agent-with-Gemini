import os 
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file

from call_function import call_function



load_dotenv()
def main():
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=GEMINI_API_KEY)
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Write to files (create parent directories if needed)
- Run Python files with optional arguments
When the user asks about the code project - they are reffering to the files in the working directory.
So you should start by looking at the project's files, and figuring out how to run the project and how to run 
its tests, you'll always want to test the tests and the actual project to verify that behavior is working as expected.


All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    if len(sys.argv) < 2:
        print("I need a prompt to work with!")
        sys.exit(1)
    verbose_flag = False
    if sys.argv[-1] == "--verbose":
        verbose_flag = True
    prompt = sys.argv[1]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file
            ]
    )
    
    config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction= system_prompt,
        )

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    max_iters = 20

    for i in range(max_iters):

        response = client.models.generate_content(model="gemini-2.0-flash-001",
                                                contents=messages,
                                                config=config)

        if response is None or response.usage_metadata is None:
            print("No response or usage metadata received.")
            return
        # print(response.text)
        if verbose_flag:
            print("User Prompt:", prompt)
            print("Prompt Tokens:", response.usage_metadata.prompt_token_count)
            print("Response Tokens:", response.usage_metadata.candidates_token_count)

        if response.candidates:
            for candidate in response.candidates:
                if candidate is None or candidate.content is None:
                    continue
                messages.append(candidate.content)

        if response.function_calls:
            for function_call_part in response.function_calls:
                result = call_function(function_call_part,verbose_flag)
                messages.append(result)
        else:
            #final call
            print(response.text)
            return
main()