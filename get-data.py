import os
import requests

# Define the folder where you want to save the CSV files
folder_name = "data"

# Ensure the folder exists or create it if not
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Define an array of GitHub CSV file URLs
github_csv_urls = [
    "https://raw.githubusercontent.com/cj-holmes/columbo/main/raw-data/columbo-first-appearances-mark-longair.csv",
    "https://raw.githubusercontent.com/cj-holmes/columbo/main/columbo_data.csv",
    # Add more URLs as needed
]

# Iterate through the list of URLs and download each CSV file
for github_csv_url in github_csv_urls:
    # Extract the filename from the URL
    file_name = os.path.join(folder_name, github_csv_url.split("/")[-1])

    # Send an HTTP GET request to download the file
    response = requests.get(github_csv_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the CSV file to the specified folder
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"CSV file '{file_name}' downloaded and saved successfully.")
    else:
        print(f"Failed to download CSV file '{github_csv_url}'. Status code: {response.status_code}")
