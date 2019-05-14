function selectDate (formatted_date) {
  var time_select = document.getElementById("sess_time_select");
  time_select.style.display = "block";

  var date_input = document.querySelector('input[type="date"]');
  date_input.value = formatted_date;
  var day_cells = document.getElementsByTagName('td');
  for (var i = 0; i < day_cells.length; i++) {
    if (day_cells[i].id.toString() == formatted_date) {
      day_cells[i].style.borderWidth = "3px";
    }
    else
    {
      day_cells[i].style.borderWidth = "1px";
    }
  }
  // var obj = document.getElementById(formatted_date);
  // obj.style.borderStyle = "inset";
}