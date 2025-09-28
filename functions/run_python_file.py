import os 
from google.genai import types
import subprocess
def run_python_file(working_directory, file_path:str,args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: {file_path} is not in the working directory.'

    if not os.path.isfile(abs_file_path):
        return f'Error: {file_path} is not a valid file path.'
    if not file_path.endswith('.py'):
        return f'Error: {file_path} is not a Python file.'
    try:
        final_args = ['python', file_path]
        final_args.extend(args)
        output = subprocess.run(final_args,timeout=30, capture_output=True, 
                                cwd=working_directory)
        final_srting = f"""
        STDOUT : {output.stdout}
        STDERR : {output.stderr}
        """
        if output.stdout=="" and output.stderr=="":
            final_srting = "No output is produced.\n"
        if output.returncode !=0:
            final_srting += f"Process exited with code {output.returncode}\n"
        return final_srting
    except Exception as e:
        return f'Error running file {file_path}: {str(e)}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file with the python interpreter, Accepts additional CLI agrs as an optional array.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional array of strings to be used for CLI args for the python file.",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
    ),
)