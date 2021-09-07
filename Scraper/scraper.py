from bs4 import BeautifulSoup

html = ""

with open("fake_jobs.html", "r") as f:
    html= f.read()

soup = BeautifulSoup(html, 'html.parser')
cards = (soup.find_all('div',class_ = 'card-content'))
for card in cards:
    print('job role:', card.find('h2').get_text())
    print('description:', card.find('h3').get_text())
    print('\n\n')
