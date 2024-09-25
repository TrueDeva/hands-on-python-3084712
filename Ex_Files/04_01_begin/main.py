import requests

# Base URL for the API
base_url = "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?format=json"

# Initialize variables to hold all the data and for pagination
all_data = []
page = 1

while True:
    # Make the API request for the current page
    response = requests.get(f"{base_url}&page={page}")

    try:
        # Check if the response is empty
        if not response.content.strip():
            print(f"Empty response at page {page}. Ending pagination.")
            break

        # Attempt to parse the JSON response
        data = response.json()

        # Validate the response structure
        if response.status_code == 200 and len(data) > 1:
            # Add the data from this page to all_data
            all_data.extend(data[1])
            
            # Check if there are more pages to fetch
            if len(data[1]) == 0 or page >= data[0]['pages']:
                break
            
            # Increment the page number to fetch the next page
            page += 1
        else:
            print(f"Unexpected data format or error on page {page}: {response.text}")
            break

    except requests.exceptions.JSONDecodeError as e:
        print(f"JSON decode error on page {page}: {e}")
        print(f"Response content: {response.text}")
        break

# Extract the last 20 years of data (or as many as available)
last_twenty_years = all_data[:20]

# Print the data with bars
for year in last_twenty_years:
    display_width = year["value"] // 10_000_000 if year["value"] else 0
    print(year["date"], "=" * display_width)
