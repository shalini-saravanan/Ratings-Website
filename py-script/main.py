import json
from bs4 import BeautifulSoup as bs
import os
import re


def add_content(id, content, tag):
    html = open("/home/sugan/Documents/GitHub/Ratings-Website/progress.html")
    soup = bs(html, 'html.parser')

    old = soup.find(tag, {"id": id})
    txt = bs(content, "html.parser")
    new = old.find(text=re.compile("#")).replace_with(txt)
    with open("/home/sugan/Documents/GitHub/Ratings-Website/progress.html", "wb") as f_output:
        f_output.write(soup.prettify("utf-8"))


def getDocTable(name, ratings, rank) -> str:

    res = """<tr class="checkBox">
                <td><input class="form-check-input checks" onClick="myfunc()" type="checkbox"></td>
                <td class="name">{0}</td>
                <td class="rank">{2}</td>
                <td class="percentage">{1}</td>
            </tr>""".format(name, ratings, rank)

    return res


def getDocViews(name, views, mx) -> str:
    perc = (views/mx)*100

    res = """<div class="row items">
           <div class="col-xl-4 col-lg-4">
           <input class="form-check-input checks" onClick="myfunc()" type="checkbox">
           <a class="badge fs-sm text-nav bg-secondary text-decoration-none rank"># </a>
           <strong class="name">{0} &nbsp;</strong>
           </div>
           <div class="fs-sm mb-2 checkBox col-xl-8 col-lg-8">
            <div class="progress mb-3">
           <div class="progress-bar bg-gradient-primary percentage" role="progressbar" style="width: {2}%" aria-valuenow="{2}%" aria-valuemin="0" aria-valuemax="{3}">${1}</div>
            </div>
           </div>
           </div>""".format(name, views, perc, mx)

    return res


def getDoc(name, percentage) -> str:
    res = """<div class = "row items">
            <div class="col-xl-4 col-lg-4" >
            <input class="form-check-input checks" onClick = "myfunc()" type="checkbox">
            <strong class = "name">{0}&nbsp;</strong>
            </div>
            <div class="fs-sm mb-2 checkBox col-xl-8 col-lg-8">
            <div class="progress mb-3">
            <div class="progress-bar bg-gradient-primary percentage" role="progressbar" style="width: {1}%" aria-valuenow="{1}" aria-valuemin="0" aria-valuemax="100">{1}%</div>
            </div>
            </div>
            </div>""".format(name, percentage)
    return res


editor = ""
viewers = ""
reviewer = ""
view = ""
os.system('cp ./template.html ../progress.html')

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

    for i in viewersChoice:
        viewers = viewers + getDocTable(i["name"], i["ratings"], rank)
        rank = rank + 1
    rank = 1
    for i in reviewersChoice:
        reviewer = reviewer + getDocTable(i["name"], i["ratings"], rank)
        rank = rank + 1

    for i in editorsChoice:
        editor = editor + getDoc(i["name"], i["ratings"])
        rank = rank + 1

    mx = views[0]["views"]
    for i in views:
        if mx < i["views"]:
            mx = i["views"]
    for i in views:
        view = view + getDocViews(i["name"], i["views"], mx)

    add_content("viewers", viewers, "tbody")
    add_content("reviewer", reviewer, "tbody")
    add_content("editor", editor, "div")
    add_content("view", view, "div")
