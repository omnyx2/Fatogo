var hotel_star = document.getElementById('hotel_star');

function full_stars() {
  var full_star = document.createElement("I");
  full_star.className = "fas fa-star";
  hotel_star.appendChild(full_star);
}

function half_stars() {
  var half_star = document.createElement("I");
  half_star.className = "fas fa-star-half-alt";
  hotel_star.appendChild(half_star);
}

function no_stars() {
  var no_star = document.createElement("I");
  no_star.className = "far fa-star";
  hotel_star.appendChild(no_star);
}

var grade = document.getElementById('hotel_grade').textContent;
grade = Number(grade);
grade = Math.floor(grade); //7.5 -> 7

var i;

for (i = grade; i >= 2; i = i - 2) {
  full_stars();
}

if (i == 1) {
  half_stars();
}

var l;

for (l = 10 - grade; l >= 2; l = l - 2) {
  no_stars();
}
