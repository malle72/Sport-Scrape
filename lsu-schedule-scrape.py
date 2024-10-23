import requests
from bs4 import BeautifulSoup

# Base URL for Louisiana State's schedule, with the year placeholder
base_url = "https://www.sports-reference.com/cfb/schools/louisiana-state/{year}-schedule.html"

# Loop through the years 2018 to 2023
for year in range(2018, 2024):
    # Format the URL for the specific year
    url = base_url.format(year=year)

    # Make the HTTP request to get the page content
    response = requests.get(url)

    # If the request is successful (status code 200)
    if response.status_code == 200:
        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all elements with data-stat="date_game" and get the csk attribute
        date_elements = soup.find_all(attrs={"data-stat": "date_game"})
        print(f"Dates for {year}:")

        # Loop through the found elements and print the 'csk' attribute
        for element in date_elements:
            csk = element.get('csk')
            if csk:
                print(csk)

        print()  # Print a newline for readability between years
    else:
        print(f"Failed to retrieve data for {year}. Status code: {response.status_code}")
