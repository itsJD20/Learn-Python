import requests
from bs4 import BeautifulSoup

html_page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
html = html_page.text

soup = BeautifulSoup(html, "html.parser")


forecast =(soup.find_all('div', class_ ='row row-odd row-forecast'))
with open("file.csv", "w") as f:

    f.write("Day" + ';' + "Description" + '\n')

    for data in forecast:

        r1 = data.find('div', class_ = 'col-sm-2 forecast-label').get_text()
        r2 = data.find('div', class_ = 'col-sm-10 forecast-text').get_text()

        f.write(r1 + ';' + r2 + '\n')







