
import os
from google.genai import types

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: {file_path} is not in the working directory.'

    if not os.path.isfile(abs_file_path):
        return f'Error: {file_path} is not a valid file path.'
    
    file_content_string = ''
    try:
        with open(abs_file_path, 'r') as file:
            file_content_string = file.read(MAX_CHARS)   
            if len(file_content_string) == MAX_CHARS:
                file_content_string += f"\n...file path {abs_file_path} (truncated)"
        return file_content_string
    except Exception as e:
        return f'Error reading file {file_path}: {str(e)}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of the given file as a string, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to file, from the working directory.",
            ),
        },
    ),
)