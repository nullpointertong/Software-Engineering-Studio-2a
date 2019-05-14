var selectedDate = null;

function selectDate (formatted_date) {
  var time_select = document.getElementById("sess_time_select");
  time_select.style.display = "block";

  var date_input = document.querySelector('input[type="date"]');
  date_input.value = formatted_date;
  var day_cells = document.getElementsByTagName('td')
  for (var i = 0; i < day_cells.length; i++) {
    day_cells[i].style.backgroundColor = "#ffffff00";;
  }
  var newSelectedDate = document.getElementById(formatted_date);
  newSelectedDate.style.backgroundColor = "#a7bdf5";
  selectedDate = newSelectedDate;
}

function book () {
  alert("Book it!")
}