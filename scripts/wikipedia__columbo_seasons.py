from bs4 import BeautifulSoup
import csv
import requests
import re

# List of URLs for the 10 pages
base_url = "https://en.wikipedia.org/wiki/Columbo_(season_"
urls = [f"{base_url}{season})" for season in range(1, 11)]

# Define the headers
headers = ["No. in series", "No. in season", "Title", "Directed by", "Written by", "Murderer played by", "Victim(s) played by", "Original air date", "Runtime", "Description"]

# Create a CSV file
with open('data/wikipedia__columbo_seasons.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Add the headers to the CSV file
    writer.writerow(headers)

    # Define a function to clean the description text
    def clean_description(description_cell):
        # Remove all HTML tags except <p>
        cleaned_text = re.sub(r'(<(?!p).*?>)', '', str(description_cell))
        # Replace <p> tags with newline characters
        cleaned_text = cleaned_text.replace('<p>', '\n')
        cleaned_text = cleaned_text.replace('</p>', '')
        return cleaned_text

    # Loop through the URLs
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find('table', {'class': 'wikitable'})

            # Find all rows in the table
            rows = table.find_all('tr')

            # Iterate every other row
            for i in range(1, len(rows), 2):
                current_row = rows[i]
                next_row = rows[i + 1]

                data = [cell.get_text(separator=' ', strip=True).replace('\n', ' ').replace('\r', '') for cell in current_row.find_all(['th', 'td'])]

                # Find the corresponding description in the next row
                description_cell = next_row.find('td', {'class': 'description'})
                if description_cell:
                    #description = description_cell.get_text(separator=' ', strip=True).replace('\n', ' ').replace('\r', '')
                    description = clean_description(description_cell)
                    data.append(description)
                else:
                    data.append('')  # If no description, add an empty cell

                # Write the row to the CSV
                writer.writerow(data)

print("CSV file generated successfully.")
