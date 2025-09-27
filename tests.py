from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
def main():
    working_directory = "calculator"
    root_contents = get_files_info(working_directory)
    print("Root Directory Contents:\n", root_contents)
    subdirectory = "pkg"
    subdirectory_contents = get_files_info(working_directory, subdirectory)
    print(f"Contents of '{subdirectory}' Directory:\n", subdirectory_contents)
    outside_directory = "../"
    outside_contents = get_files_info(working_directory, outside_directory)
    print(f"Attempt to access outside directory '{outside_directory}':\n", outside_contents)
    bb= get_files_info(working_directory, "/bin")
    print(bb)

    print(get_file_content(working_directory, "lorem.txt"))
    print(get_file_content(working_directory, "main.py"))
    print(get_file_content(working_directory, "tests.py"))
    print(get_file_content(working_directory, "pkg/calcula.py"))
    print(get_file_content(working_directory, "/bin/cat"))

    print(write_file(working_directory, "lorem.txt", "This is a overwritten file."))
    #print(write_file(working_directory, "pkg/newfile.txt", "This is a new file."))
    print(write_file(working_directory, "../outside.txt", "This should fail."))
    print(write_file(working_directory, "/bin/unsafe.txt", "This should also fail."))
    #print(write_file(working_directory, "pkg2/file.txt", "This should create the directory and write the file."))

    print(run_python_file(working_directory, "main.py",["3 + 4"]))
    print(run_python_file(working_directory, "../tests.py"))
main()