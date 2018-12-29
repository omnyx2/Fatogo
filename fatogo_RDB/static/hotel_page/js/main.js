// $("input:checkbox").click(function() {
//   if ($(this).checked == false) {
//     $(this).checked = true;
//   } else {
//     $(this).checked = false;
//   }
// });

$(document).ready(function() {
  $(".room_name").hide();
});




  var f; //floor 변수
var i; //room_id 변수
for (var f = 1; f <= 5; f++) {
  var floor = document.createElement("fieldset");
  floor.className = "floor";
  floor.setAttribute("id", "floor_" + f);
  floor.setAttribute("style", "display:none;");

  document.getElementById('hotel_room_map').appendChild(floor);

  var floor_select = document.createElement("INPUT");
  floor_select.setAttribute("type", "radio");
  floor_select.setAttribute("name", "floor_select");
  floor_select.setAttribute("id", "btn_floor" + f);
  floor_select.setAttribute("onclick", "floorselection('" + f + "')");
  floor_select.className = "floor_select";

  var str = f;
  $('<style>#btn_floor' + f + ':after{content:"' + str + 'F"}</style>').appendTo('head');

  function floorselection(f) {
    $(".floor").hide('600');
    $("#floor_" + f + "").show('600');
  }

  document.getElementById('hotel_room_map').appendChild(floor_select);
  $(floor_select).appendTo('.hotel_room_map legend');

  // $('<style>#floor' + f + ':after{content:"' + f + '"}</style>').appendTo('head');



  for (var i = 1; i < 3; i++) {
    var n = i;
    var room_box = document.createElement("INPUT");
    room_box.setAttribute("id", "room" + n);
    room_box.setAttribute("type", "checkbox");
    room_box.setAttribute("name", "room_floor" + f + "");
    room_box.className = "room_box";
    room_box.style.top = "10%";
    room_box.style.left = "10%";
    room_box.style.width = "20%";
    room_box.style.height = "40%";
    room_box.setAttribute("onclick", "roomselection(" + n + ")");

    var room_name_list = document.createElement("div");
    room_name_list.setAttribute("id", "room_name_list" + n);
    room_name_list.setAttribute("style", "display:none;");
    $(room_name_list).appendTo('#selected_room');
    $("#room_name_list" + n + "").append("" + n + "호");

    function roomselection(n) {

      $('#room_name_list' + n + '').toggle('600');

      if ($(".room_box:checked").length > 0) {
        $(".purchace").show('600');
        $(".room_name").hide('600');
        $("#room_" + n + "").show('600');
      } else {
        $(".purchace").hide('600');
        $(".room_name").hide('600');
      }

      // if ($("#room" + n + "").prop('checked') == true) {
      //   $("#selected_room").append("" + n + "호");
      // } else {
      //   $("#selected_room").remove(":contains('" + n + "호')");
      // }
    }

    document.getElementById('floor_' + f).appendChild(room_box); //class로 변경 후

    var str = n;
    $('<style>#room' + i + ':after{content:"' + str + '"}</style>').appendTo('head');

  }


}

// var rn;
//
// $(".room_box").on("click", function(){
//   for (var rn = 1; rn <= $(".room_box").length; rn++) {
//     if ($("#room" + rn + "").prop('checked') == true) {
//       $("#selected_room").append("" + rn + "호");
//     } else {
//       $("#selected_room").remove(":contains('" + rn + "호')");
//     }
//   }
//
// });



var hotel_star = document.getElementsByClassName('hotel_star');

var k;

for (var k = 0; k < hotel_star.length; k++) {
  var hotel_stars = document.getElementsByClassName('hotel_star')[k];

  function full_stars() {
    var full_star = document.createElement("I");
    full_star.className = "fas fa-star";
    hotel_stars.appendChild(full_star);
  }

  function half_stars() {
    var half_star = document.createElement("I");
    half_star.className = "fas fa-star-half-alt";
    hotel_stars.appendChild(half_star);
  }

  function no_stars() {
    var no_star = document.createElement("I");
    no_star.className = "far fa-star";
    hotel_stars.appendChild(no_star);
  }

  var grade = document.getElementsByClassName('hotel_grade')[k].textContent;
  grade = Number(grade);
  grade = grade * 2;
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
}
