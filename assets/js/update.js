fetch("http://127.0.0.1:5500/Ratings-Website/data.json")
    .then(response => response.json())
    .then(data => {
        console.log(typeof data)
        const arr = data.ratings;

        let mostViewed = arr;
        let editorsChoice = [];
        let viewersChoice = [];
        let reviewersChoice = [];

        for (const i of data.ratings) {
            switch (i.choiceBy) {
                case "editorsChoice":
                    editorsChoice.push(i);
                    break;
                case "viewersChoice":
                    viewersChoice.push(i);
                    break;
                case "reviewersChoice":
                    reviewersChoice.push(i);
                    break;
            }

        }
        mostViewed.sort((a, b) => {
            return b.views - a.views;
        })
        mostViewed = mostViewed.slice(0, 10);
        for (const i of mostViewed) {
            document.getElementById("mostViewed").innerHTML += getDocViews(i.name, i.views, arr[0].views);
        }
        addData({ name: "viewersChoice", arr: viewersChoice.slice(0, 10) });
        addData({ name: "reviewersChoice", arr: reviewersChoice.slice(0, 10) });
        addData({ name: "editorsChoice", arr: editorsChoice.slice(0, 10) });
    });

function addData(data) {
    for (const i of ratingSort(data.arr)) {
        document.getElementById(`${data.name}`).innerHTML += getDoc(i.name, i.ratings);
    }
}

function ratingSort(arr) {
    arr.sort((a, b) => {
        return b.ratings - a.ratings;
    });
    return arr;
}

function getDoc(name, ratings) {
    resStr = '<div class="row items">' +
        '<div class="col-xl-4 col-lg-4">' +
        '<input class="form-check-input checks" onClick="myfunc()" type="checkbox">' +
        '<a class="badge fs-sm text-nav bg-secondary text-decoration-none rank"># </a>' +
        `<strong class="name">${name} &nbsp;</strong>` +
        '</div> ' +
        '<div class="fs-sm mb-2 checkBox col-xl-8 col-lg-8">' +
        ' <div class="progress mb-3">' +
        `<div class="progress-bar bg-gradient-primary percentage" role="progressbar" style="width: ${ratings}%" aria-valuenow="${ratings}" aria-valuemin="0" aria-valuemax="100">${ratings}%</div>` +
        ' </div>' +
        '</div> ' +
        '</div>'
    return resStr;

}

function getDocViews(name, views, max) {
    resStr = '<div class="row items">' +
        '<div class="col-xl-4 col-lg-4">' +
        '<input class="form-check-input checks" onClick="myfunc()" type="checkbox">' +
        '<a class="badge fs-sm text-nav bg-secondary text-decoration-none rank"># </a>' +
        `<strong class="name">${name} &nbsp;</strong>` +
        '</div> ' +
        '<div class="fs-sm mb-2 checkBox col-xl-8 col-lg-8">' +
        ' <div class="progress mb-3">' +
        `<div class="progress-bar bg-gradient-primary percentage" role="progressbar" style="width: ${(views/max)*100}%" aria-valuenow="${views}" aria-valuemin="0" aria-valuemax="${max}">${views}</div>` +
        ' </div>' +
        '</div> ' +
        '</div>'
    return resStr;

}