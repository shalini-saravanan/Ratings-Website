fetch("http://127.0.0.1:5500/Ratings-Website/data.json")
    .then(response => response.json())
    .then(data => {
        console.log(data)
        for (let i = 0; i < data.ratings.length; i++) {
            document.getElementById("b1").innerHTML += getDoc(data.ratings[i].name, data.ratings[i].ratings);
        }
    });

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