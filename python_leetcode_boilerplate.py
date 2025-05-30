"""
A simple Python program that creates a leetcode solution file

Flags: --n <name_of_solution>
Exceptions: Raises file exists exception so a previously existing file doesn't
            get overwritten. 

"""
import argparse
import os
class FileExistsException(Exception):
    def __init__(self, message):
        super().__init__(message)

class CreateLeetcodeFile:

    def __init__(self, file_name: str):
        self.file_name = file_name
    
    def check_file_exists(self) -> bool:
        current_dir = os.getcwd()
        return os.path.isfile(current_dir + f"/{self.file_name}.py")

if __name__ == "__main__":
     
    parser = argparse.ArgumentParser(description="Create Leetcode solution file in Python")
    parser.add_argument("--n", required=True, help="Name of leetcode problem")
    args = parser.parse_args()
    print(args.n)
     
        

