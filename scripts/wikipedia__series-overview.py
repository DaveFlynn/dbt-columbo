import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the web page you want to scrape
url = 'https://en.wikipedia.org/wiki/List_of_Columbo_episodes'  # Replace with the actual URL

# Send an HTTP GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first table with the class 'wikitable'
    table = soup.find('table', {'class': 'wikitable'})

    if table:
        # Create a CSV file for writing
        with open('data/wikipedia__series-overview.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)

            # Extract column headers from the first two rows
            header_rows = table.find_all('tr')[:2]
            headers = [header.text for row in header_rows for header in row.find_all(['th', 'td'])]

            # Filter out the "Originally aired" header
            headers = [header for header in headers if header != "Originally aired"]
            writer.writerow(headers)

            # Extract data from the table, starting from the third row
            last_row_values = []  # Store the last row's values

            for row in table.find_all('tr')[2:]:
                columns = [row.find('th').text]  # Use the first column as the row header
                columns.extend(column.text for column in row.find_all('td'))

                if len(columns) < 5:
                    # If there are fewer than 5 values in the row, use values from the last row
                    columns.extend(last_row_values[len(columns):])

                # Update the last row's values for the next row
                last_row_values = columns[-5:]

                # Limit the row to exactly 5 values
                columns = columns[:5]

                writer.writerow(columns)

        print('CSV file created successfully')
    else:
        print('No table with class "wikitable" found on the web page.')

else:
    print('Failed to fetch the web page. Status code:', response.status_code)
