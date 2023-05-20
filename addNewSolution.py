import os

# Step 1: Ask for the subfolder name
subfolder_name = input("Enter the name of the subfolder (denotes the type of problem): ")

# Step 2: Ask for the problem name
problem_name = input("Enter the name of the problem: ")

# Step 3: Create the solution file with appropriate folders
subfolder_name = subfolder_name.lower().replace(" ", "-")
problem_name = problem_name.lower().replace(" ", "-")
folder_path = os.path.join(os.getcwd(), subfolder_name, problem_name)
file_path = os.path.join(folder_path, "solution.py")
os.makedirs(folder_path, exist_ok=True)
open(file_path, "w").close()  # Create an empty file

# Step 4: Add a Python comment block
comment_block = f'"""\n'
comment_block += f'https://github.com/eugenechevski\n'
comment_block += f'https://leetcode.com/problems/{problem_name}\n'
comment_block += f'"""\n\n'
with open(file_path, "a") as f:
    f.write(comment_block)