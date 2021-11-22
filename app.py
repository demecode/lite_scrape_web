import requests
from bs4 import BeautifulSoup as bsf

""" Lets get the github user name """
github_user = input("Input Github User: ")


""" Lets send a request """
url = 'https://github.com/' + github_user
r = requests.get(url)
scraper = bsf(r.content, 'html.parser')
profile_picture = scraper.find('img', {'alt': 'Avatar'})['src']
print(profile_picture)
