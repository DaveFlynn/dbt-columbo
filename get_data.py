import os
import subprocess

# Define the folder where you want to save the CSV files
folder_name = "data"

# Ensure the folder exists or create it if not
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Define the folder containing your Python scripts
script_folder = "scripts"

# List all files in the folder
script_files = [f for f in os.listdir(script_folder) if f.endswith(".py")]

# Define an array of script filenames to ignore
scripts_to_ignore = ["imdb.py"]

# Iterate through the Python script files and run them, except for the ignored scripts
for script_file in script_files:
    if script_file in scripts_to_ignore:
        print(f"Ignoring script '{script_file}' as per your request.")
        continue

    script_path = os.path.join(script_folder, script_file)
    try:
        subprocess.run(["python", script_path], check=True)
        print(f"Script '{script_file}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running script '{script_file}': {e}")
