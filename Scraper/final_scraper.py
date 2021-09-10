import requests
from bs4 import BeautifulSoup


html_page = requests.get('https://realpython.github.io/fake-jobs/')
html = html_page.text

soup = BeautifulSoup(html, "html.parser")

cards = (soup.find_all('div',class_ = 'card-content'))
with open("new_file.csv", "w") as f:

    f.write("Post"+';'+"Company"+';'+"Location"+';'+"Time"+';'+"Learn"+';'+"Apply"+'\n')
    for card in cards:
        p1 = card.find('h2').get_text()
        p2 = card.find('h3').get_text() 
        p3 = card.find('p', class_ = 'location').get_text().strip() 
        p4 = card.find('time').get_text() 
        footer = card.find('footer')
        l = footer.find_all('a')
        learn = l[0]['href'] 
        apply = l[1]['href']
        f.write(p1+';'+p2+';'+p3+';'+p4+';'+learn+';'+apply+'\n')
        

