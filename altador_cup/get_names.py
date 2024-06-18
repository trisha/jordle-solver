import requests
from bs4 import BeautifulSoup

def get_team_roster(url):
    # Send a GET request to the webpage
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all <td> elements
        td_elements = soup.find_all('td')
        
        # Extract names
        # Sample page where we're trying to grab the name of each teammate: https://thedailyneopets.com/altador-cup/altador/
        name_values = []
        for td in td_elements:
            b_name = td.find('b', string="Name:")
            if b_name:
                # Extract the full name text after the <b> tag
                name_text = b_name.next_sibling.strip().strip('" ')
                name_values.append(name_text)
        
        return name_values
    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
        return []

file_path = 'ac_urls.txt'

# Read the URLs from the file
with open(file_path, 'r') as file:
    urls = file.read().splitlines()

names = [] 

# URL of webpage to scrape
for url in urls:
    team_roster = get_team_roster(url)
    names.extend(team_roster)

file_path = 'names.txt'

def check_if_valid(line):
    res = []
    words = line.split(" ")
    for word in words:
        word = word.strip("'")
        word = word.strip('"')
        if len(word) == 5:
            res.append(word)
    return res

# Will overwrite file every time this script is run (w for overwrite)
count = 0
with open(file_path, 'w') as file:
    for name in names:
        valid_names = check_if_valid(name)
        for valid_name in valid_names:
            count += 1
            file.write(f"{valid_name}\n")

print(f"Saved {count} names to {file_path}")