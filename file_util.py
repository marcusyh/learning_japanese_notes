import os
import sys
import shutil

def prepare_file_path(input_path, is_dir=False, delete_if_exists=False, create_if_not_exists=False):
    input_path = os.path.abspath(input_path)
    
    filename = os.path.basename(input_path)
    # Check if file exists
    if os.path.exists(input_path) and delete_if_exists:
        while True:
            user_input = input(f"File {filename} already exists. Delete and continue? (y/n): ").lower()
            if user_input == 'y':
                if os.path.isdir(input_path):
                    shutil.rmtree(input_path)
                else:
                    os.remove(input_path)
                print(f"Deleted existing file: {input_path}")
                break
            elif user_input == 'n':
                print("Exiting program.")
                sys.exit(0)
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
            
    if create_if_not_exists:
        directory = input_path if is_dir else os.path.dirname(input_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")

    return True