from bs4 import BeautifulSoup as bs
import os
import re

html = open("/home/sugan/Documents/GitHub/Ratings-Website/progress.html")
soup = bs(html, 'html.parser')

old = soup.find("tbody", {"id": "test"})
print(old)
txt = bs("<p>hiihi</p>", "html.parser")
new = old.find(text=re.compile("")).replace_with(txt)
with open("/home/sugan/Documents/GitHub/Ratings-Website/progress.html", "wb") as f_output:
    f_output.write(soup.prettify("utf-8"))
