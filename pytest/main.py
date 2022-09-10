import json
from bs4 import BeautifulSoup as bs
import os
import re


def add_content(id, content):
    html = open("/home/sugan/Documents/GitHub/Ratings-Website/progress.html")
    soup = bs(html, 'html.parser')

    old = soup.find("tbody", {"id": id})
    txt = bs(content, "html.parser")
    new = old.find(text=re.compile("")).replace_with(txt)
    with open("/home/sugan/Documents/GitHub/Ratings-Website/progress.html", "wb") as f_output:
        f_output.write(soup.prettify("utf-8"))


def getDoc(name, ratings, rank) -> str:

    res = """<tr class="checkBox">
                <td><input class="form-check-input checks" onClick="myfunc()" type="checkbox"></td>
                <td class="name">{0}</td>
                <td class="rank">{2}</td>
                <td class="percentage">{1}</td>
            </tr>""".format(name, ratings, rank)

    return res


def getDocViews(name, views, rank) -> str:
    res = """<tr class="checkBox">
                <td><input class="form-check-input checks" onClick="myfunc()" type="checkbox"></td>
                <td class="name">{0}</td>
                <td class="rank">{2}</td>
                <td class="percentage">{1}</td>
            </tr>""".format(name, views, rank)
    return res


editor = ""
viewers = ""
reviewer = ""
view = ""
with open("/home/sugan/Documents/GitHub/Ratings-Website/data.json", "r") as js_file:
    data = json.load(js_file)
    editorsChoice = []
    viewersChoice = []
    reviewersChoice = []
    views = []

    for i in data["ratings"]:
        if (i["choiceBy"] == "viewersChoice"):
            viewersChoice.append(i)
        elif (i["choiceBy"] == "reviewersChoice"):
            reviewersChoice.append(i)
        elif (i["choiceBy"] == "editorsChoice"):
            editorsChoice.append(i)
        views.append(i)

    editorsChoice = sorted(
        editorsChoice, key=lambda x: int(x["ratings"]), reverse=True
    )[:10]
    viewersChoice = sorted(
        viewersChoice, key=lambda x: int(x["ratings"]), reverse=True
    )[:10]
    reviewersChoice = sorted(
        reviewersChoice, key=lambda x: int(x["ratings"]), reverse=True
    )[:10]

    views = sorted(
        views, key=lambda x: int(x["views"]), reverse=True
    )[:10]
    rank = 1

    for i in editorsChoice:
        editor = editor + getDoc(i["name"], i["ratings"], rank)
        rank = rank + 1
    rank = 1
    for i in viewersChoice:
        viewers = viewers + getDoc(i["name"], i["ratings"], rank)
        rank = rank + 1
    rank = 1
    for i in reviewersChoice:
        reviewer = reviewer + getDoc(i["name"], i["ratings"], rank)
        rank = rank + 1
    rank = 1

    for i in views:
        view = view + getDocViews(i["name"], i["views"], rank)
        rank = rank + 1

    add_content("viewers", viewers)
    add_content("view", view)
    add_content("editor", editor)
    add_content("reviewer", reviewer)
