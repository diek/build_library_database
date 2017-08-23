from bs4 import BeautifulSoup
import requests

url = 'https://www.wikidata.org/wiki/Q5230760'
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')
# Get Date of Birth
p569 = soup.find("div", {"id": 'P569'})
dob = p569.find_all(class_="wikibase-snakview-variation-valuesnak")[0].get_text()
print(dob)

# Date of Death

p570 = soup.find("div", {"id": 'P570'})
print(p570)

# div id = P569 date of birth
# div id = P570 date of death
# div = soup.find(id="P569")
