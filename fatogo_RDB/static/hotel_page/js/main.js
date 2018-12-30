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




// var arr = [{
//     room_type_id: 1,
//     room_num: 101,
//     room_floor: 1,
//     room_height: 10,
//     room_width: 10,
//     room_position_x: 10,
//     room_position_y: 10
//   },

//   {
//     room_type_id: 2,
//     room_num: 102,
//     room_floor: 1,
//     room_height: 20,
//     room_width: 20,
//     room_position_x: 20,
//     room_position_y: 20
//   },
//   {
//     room_type_id: 1,
//     room_num: 201,
//     room_floor: 2,
//     room_height: 10,
//     room_width: 10,
//     room_position_x: 10,
//     room_position_y: 10
//   },
//   {
//     room_type_id: 2,
//     room_num: 202,
//     room_floor: 2,
//     room_height: 20,
//     room_width: 20,
//     room_position_x: 20,
//     room_position_y: 20
//   }
// ];

function floorselection(f) {
  $(".floor").hide();
  $("#floor_" + f + "").show();
}


function roomselection(i, rt) {

  $('#room_name_list' + i + '').toggle('800');

  if ($(".room_box:checked").length > 0) {
    $(".purchace").show('800');
    $(".room_name").hide('800');
    $("#room_" + rt + "").show('800');
  } else {
    $(".purchace").hide('800');
    $(".room_name").hide('800');
  }

}

$.each(arr, function(index, item) {

  var f = item.room_floor;


  var floor = document.createElement("fieldset");
  floor.className = "floor";
  floor.setAttribute("id", "floor_" + f);
  floor.setAttribute("style", "display:none;");

  document.getElementById('hotel_room_map').appendChild(floor);

  var floor_select = document.createElement("INPUT");
  floor_select.setAttribute("type", "radio");
  floor_select.setAttribute("name", "floor_select");
  floor_select.setAttribute("id", "btn_floor" + f);
  floor_select.setAttribute("onclick", "floorselection(" + f + ")");
  floor_select.className = "floor_select";

  $('<style>#btn_floor' + f + ':after{content:"' + f + 'F"}</style>').appendTo('head');



  document.getElementById('hotel_room_map').appendChild(floor_select);
  $(floor_select).appendTo('.hotel_room_map legend');

  var seen = {};
  $('input#btn_floor' + f + '').each(function() {
    var txt = $(this).text();
    if (seen[txt])
      $(this).remove();
    else
      seen[txt] = true;
  });




  var i = item.room_num;
  var rt = item.room_type_id;

  var room_box = document.createElement("INPUT");
  room_box.setAttribute("id", "room" + i);
  room_box.setAttribute("type", "checkbox");
  room_box.setAttribute("name", "room_floor" + item.room_floor + "");
  room_box.className = "room_box";
  room_box.style.top = "" + item.room_position_y + "%";
  room_box.style.left = "" + item.room_position_x + "%";
  room_box.style.width = "" + item.room_width + "%";
  room_box.style.height = "" + item.room_height + "%";
  room_box.setAttribute("onclick", "roomselection(" + i + "," + rt + ")");

  var room_name_list = document.createElement("div");
  room_name_list.setAttribute("id", "room_name_list" + i);
  room_name_list.setAttribute("style", "display:none;");
  room_name_list.className = "room_name_list"
  $(room_name_list).appendTo('#selected_room');
  $("#room_name_list" + i + "").append("" + i + "호");



  document.getElementById('floor_' + f).appendChild(room_box); //class로 변경 후

  var str = i;
  $('<style>#room' + i + ':after{content:"' + str + '"}</style>').appendTo('head');



})




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
