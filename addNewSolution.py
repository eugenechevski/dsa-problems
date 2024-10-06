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

# Step 6: Update the README.md file
readme_file = os.path.join(os.getcwd(), "README.md")
if os.path.exists(readme_file):
    with open(readme_file, "r") as f:
        lines = f.readlines()

    # Find the section header
    section_header = f"## {subfolder_name.replace('-', ' ').title()}\n"
    if section_header not in lines:
        # If the section does not exist, add it at the end of the file
        lines.append(f"\n{section_header}\n")

    # Find the line index to insert the new problem entry
    header_index = lines.index(section_header)
    
    # Insert new line
    lines.insert(header_index + 1, "\n");
    
    # Create the new problem entry
    problem_entry = f"* {problem_name.replace('-', ' ').title()}\n"
    problem_entry += f"  - [Problem](https://leetcode.com/problems/{problem_name}/)\n"
    problem_entry += f"  - [Solution]({subfolder_name}/{problem_name}/solution.{file_extension})\n"
    
    # Insert the new entry after the header
    lines.insert(header_index + 2, problem_entry)

    # Write the updated content back to the README.md
    with open(readme_file, "w") as f:
        f.writelines(lines)

    print(f"README.md updated with the new problem entry under {subfolder_name.title()} section.")
else:
    print("README.md not found. No changes were made.")
