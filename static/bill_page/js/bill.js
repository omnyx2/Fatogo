var am; //시설 변수
var h; //시설 이용시간 변수
for (var am = 1; am <= 3; am++) {
  var selected_amenity = $('#amenity_' + am + '');


  for (var h = 16; h <= 24; h++) {
    var hs = am;
    var swiperslide = document.createElement("div");
    swiperslide.className = "swiper-slide";

    $(swiperslide).appendTo('#amenity_' + am + ' .swiper-container .swiper-wrapper');

    var newinput = document.createElement("input");
    newinput.setAttribute("type", "checkbox");
    newinput.setAttribute("name", "hour_select" + am);
    newinput.setAttribute("id", "h" + h);
    newinput.className = "hour_select" + am + "";
    newinput.setAttribute("onclick", "hourselection(" + hs + ")");

    $(newinput).appendTo(swiperslide);





    function hourselection(hs) {
      var checked = $(".hour_select" + hs + ":checked").length;
      checked = Number(checked);
      $('#amenity_' + hs + '_time').text(checked);
    }


  }
}



var swiper = new Swiper('.swiper-container', {
  slidesPerView: 4.9,
  spaceBetween: 9,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
});


// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
