from bs4 import BeautifulSoup
import requests

URL = "http://www.yougowords.com/5-letters"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

word_table = soup.find(id='sortable-display')

results = word_table.find_all('a')

for result in results:
    print(result.text)