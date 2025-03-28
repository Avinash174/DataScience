from bs4 import BeautifulSoup
import requests

page_url = "https://www.google.com"
page = requests.get(page_url)

soup = BeautifulSoup(page.content, 'html.parser')

for link in soup.find_all('a'):  # Extract all anchor tags
    print(link.get('href'))
