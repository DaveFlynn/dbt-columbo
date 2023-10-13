import os
import requests

# Define the folder where you want to save the CSV files
folder_name = "data"

# Ensure the folder exists or create it if not
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Define an array of GitHub CSV file URLs along with their desired filenames
github_csv_urls = [
    ("https://raw.githubusercontent.com/cj-holmes/columbo/main/raw-data/columbo-first-appearances-mark-longair.csv", "../data/cjholmes__columbo-first-appearances-mark-longair.csv"),
    ("https://raw.githubusercontent.com/cj-holmes/columbo/main/columbo_data.csv", "../data/cjholmes__columbo_data.csv"),
    # Add more URLs and filenames as needed
]

# Iterate through the list of URLs and download each CSV file with specified filename
for url, filename in github_csv_urls:
    # Combine the folder name and specified filename to get the full file path
    file_name = os.path.join(folder_name, filename)

    # Send an HTTP GET request to download the file
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the CSV file to the specified folder with the specified filename
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"CSV file '{file_name}' downloaded and saved successfully.")
    else:
        print(f"Failed to download CSV file '{url}'. Status code: {response.status_code}")
