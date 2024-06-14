import requests
from bs4 import BeautifulSoup


def get_altador_cup_image_urls(url):
    # Send a GET request to the webpage
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all anchor tags that contain image tags
        anchor_tags = soup.find_all('a')

        # Debug: Print the number of anchor tags found
        # print(f"Found {len(anchor_tags)} anchor tags.")
        
        # Extract URLs from the href attribute of anchor tags that contain images
        altador_cup_urls = [a['href'] for a in anchor_tags if a.find('img') and 'altador-cup' in a['href']]
        
        # Debug: Print the number of filtered URLs
        # print(f"Found {len(altador_cup_urls)} anchor URLs with 'altador-cup' and an image inside.")

        return altador_cup_urls
    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
        return []

# URL of webpage to scrape
page_url = 'https://thedailyneopets.com/altador-cup/altador-cup-teams'

# Get the Altador Cup team URLs from the page
urls = get_altador_cup_image_urls(page_url)

# for url in urls:
#     print(url)

file_path = 'ac_urls.txt'

# Will overwrite file every time this script is run
with open(file_path, 'w') as file:
    for url in urls:
        file.write(f"{url}\n")

print(f"Saved {len(urls)} URLs to {file_path}")