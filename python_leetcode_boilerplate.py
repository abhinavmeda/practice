"""
A simple Python program that creates a leetcode solution file.  
Flags: -f <python_function_signature>
"""
import argparse
import os

FILE_CONTENTS = """
class Solution:
    {signature}
        pass


if __name__ == "__main__":
    sol = Solution() 
"""

class CreateLeetcodeSolutionFile:

    def __init__(self, function_signature: str):
        
        self.function_signature = function_signature
        fss = function_signature.split(" ")
        
        file_name = fss[1][:fss[1].index("(")]
        self.file_name = file_name + ".py"
    
    def check_file_exists(self) -> bool:
        current_dir = os.getcwd()
        exists = os.path.abspath(current_dir + f"/{self.file_name}")
        return exists
    
    def create_file(self):
        file_contents = FILE_CONTENTS.format(signature=self.function_signature)

        with open(self.file_name, "w") as f:
            f.write(file_contents)

if __name__ == "__main__":
     
    parser = argparse.ArgumentParser(description="Create Leetcode solution file in Python")
    parser.add_argument("-f", help="Function definition of leetcode problem", required=True)
    args = parser.parse_args()

    leetcode_file = CreateLeetcodeSolutionFile(args.f)
    if leetcode_file.check_file_exists():
        leetcode_file.create_file()
    else:
        print("File already exists!")
        
