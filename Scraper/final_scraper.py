import requests
from bs4 import BeautifulSoup


html_page = requests.get('https://realpython.github.io/fake-jobs/')
html = html_page.get_text

soup = BeautifulSoup(html, "html.parser")

