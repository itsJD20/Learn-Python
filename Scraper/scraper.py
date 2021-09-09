from bs4 import BeautifulSoup

html = ""

with open("fake_jobs.html", "r") as f:
    html= f.read()

soup = BeautifulSoup(html, 'html.parser')
cards = (soup.find_all('div',class_ = 'card-content')) #find_all(give the whole list of all matching tags)
with open("new_file.csv", "w") as f: #(csv =comma seperated value) (if we use "w" - it'll rewrite the file from the beginning, but in 'a' it'll start writing from the last line)

    f.write("Post"+';'+"Company"+';'+"Location"+';'+"Time"+';'+"Learn"+';'+"Apply"+'\n')
    for card in cards:
        p1 = card.find('h2').get_text()
        p2 = card.find('h3').get_text() #find(first matching tag only)
        p3 = card.find('p', class_ = 'location').get_text().strip() #get_text(get output in a text form), strip(string function,remove extra lines,wide gap etc)
        p4 = card.find('time').get_text() 
        footer = card.find('footer')
        l = footer.find_all('a')
        learn = l[0]['href'] #href = it'll extract the link only
        apply = l[1]['href']
        f.write(p1+';'+p2+';'+p3+';'+p4+';'+learn+';'+apply+'\n')
        
        

