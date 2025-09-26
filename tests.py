from functions.get_files_info import get_files_info

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

main()