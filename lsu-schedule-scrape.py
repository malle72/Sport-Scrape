import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL for LSU's schedule
base_url = "https://www.sports-reference.com/cfb/schools/louisiana-state/{year}-schedule.html"

# Empty lists
all_dates = []
all_locs = []

# Loop through the years 2018 to 2023
for year in range(2018, 2024):
    # Format the URL for the specific year
    url = base_url.format(year=year)

    # Make request to get page content
    response = requests.get(url)

    # Check if the request is successful
    if response.status_code == 200:
        # Parse page content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all elements with data-stat="date_game" and get the csk attribute
        date_elements = soup.find_all(attrs={"data-stat": "date_game"})

        # Loop through the found elements and add the 'csk' attribute to dataframe
        for element in date_elements:
            csk = element.get('csk')
            if csk:
                all_dates.append(csk)

        # Find all elements with data-stat="game_location"
        loc_elements = soup.find_all(name='td',attrs={"data-stat": "game_location"})
        for loc in loc_elements:
            location = loc.string
            if location:
                location = "Away"
            else:
                location = "Home"
            all_locs.append(location)

    else:
        print(f"Failed to retrieve data for {year}. Status code: {response.status_code}")

df = pd.DataFrame(zip(all_dates,all_locs),columns=['date','location'])
print(df.to_string())
df.to_csv('data/lsu-schedule-scrape-18-23.csv')
