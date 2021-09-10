import requests

html_page = requests.get('https://realpython.github.io/fake-jobs/')
print("Status Code:", html_page.status_code)

with open("fake_jobs.html", "w") as f:
    f.write(html_page.text)








