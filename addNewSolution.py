import os

# Step 1: Ask for the subfolder name
subfolder_name = input("Enter the name of the subfolder (denotes the type of problem): ")

# Step 2: Ask for the problem name
problem_name = input("Enter the name of the problem: ")

# Step 3: Ask for the programming language (to determine the file extension)
programming_language = input("Enter the programming language (e.g., java, python, c, js, etc.): ").strip().lower()

# Determine the file extension based on the programming language
extensions = {
    "python": "py",
    "java": "java",
    "c": "c",
    "cpp": "cpp",
    "javascript": "js",
    "typescript": "ts",
    "ruby": "rb",
    "go": "go",
    "php": "php",
    "html": "html",
    "css": "css",
    "swift": "swift",
    "kotlin": "kt",
    # Add more languages and extensions if needed
}

# Set the default extension to the programming language input if not in the list
file_extension = extensions.get(programming_language, programming_language)

# Step 4: Create the solution file with appropriate folders and file extension
subfolder_name = subfolder_name.lower().replace(" ", "-")
problem_name = problem_name.lower().replace(" ", "-")
folder_path = os.path.join(os.getcwd(), subfolder_name, problem_name)
file_path = os.path.join(folder_path, f"solution.{file_extension}")
os.makedirs(folder_path, exist_ok=True)
open(file_path, "w").close()  # Create an empty file

# Step 5: Add a comment block appropriate for the programming language
if programming_language in ["python", "ruby"]:
    comment_block = f'"""\n'
elif programming_language in ["c", "cpp", "java", "js", "go", "typescript"]:
    comment_block = f'/*\n'
elif programming_language == "php":
    comment_block = f'<?php\n/*\n'
else:
    comment_block = f'<!--\n'  # default for HTML/CSS

comment_block += f'https://github.com/eugenechevski\n'
comment_block += f'https://leetcode.com/problems/{problem_name}\n'

if programming_language in ["python", "ruby"]:
    comment_block += f'"""\n\n'
elif programming_language in ["c", "cpp", "java", "js", "go", "typescript", "php"]:
    comment_block += f'*/\n\n'
else:
    comment_block += f'-->\n\n'

# Write the comment block to the file
with open(file_path, "a") as f:
    f.write(comment_block)

print(f"File created: {file_path}")
