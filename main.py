from bs4 import BeautifulSoup
from urllib import request
import os

ttb_url = "https://web.archive.org/web/20230906095156/https://www.ttb.gov/beer/statistics"

if not os.path.exists("ttb_stats.json"):
    with open("ttb_page.html", "wb") as f:
        resp = request.urlopen(ttb_url)
        body = resp.read()
        f.write(body)
else:
    with open("ttb_page.html") as f:
        body = f.read()

# change this to lxml intead of html5lib if you can't use it
soup = BeautifulSoup(body, "html5lib")
print(soup.title)