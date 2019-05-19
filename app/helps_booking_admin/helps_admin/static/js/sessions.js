var selectedDate = null;

$(document).on('autocompleteLightInitialize', '[data-autocomplete-light-function=student-autocomplete]', function() {
  // do select2 configuration on $(this)
})

function selectDate (formatted_date) {
  var time_select = document.getElementById("sess_time_select");
  time_select.style.display = "block";

  var date_input = document.querySelector('input[type="date"]');
  date_input.value = formatted_date;
  var day_cells = document.getElementsByTagName('td')
  for (var i = 0; i < day_cells.length; i++) {
    day_cells[i].style.backgroundColor = "#ffffff00";
  }
  var newSelectedDate = document.getElementById(formatted_date);
  newSelectedDate.style.backgroundColor = "#a7bdf5";
  selectedDate = newSelectedDate;
}

function book () {
  var student_input = document.getElementById('student_search');
  var advisor_input = document.getElementById('advisor_search');
  var date_input = document.getElementById('date');
  var sh = document.getElementById('hour-start').value;
  var sm = document.getElementById('min-start').value;
  var sa = document.getElementById('timeofday-start').value;
  var eh = document.getElementById('hour-end').value;
  var em = document.getElementById('min-end').value;
  var ea = document.getElementById('timeofday-end').value;
  var form_incomplete = false;
  if (student_input.value === "")
  {
    student_input.placeholder = "Required field!";
    student_input.style.color = "red";
    form_incomplete = true;
  }
  if (advisor_input.value === "")
  {
    advisor_input.placeholder = "Required field!";
    advisor_input.style.color = "red";
    form_incomplete = true;
  }
  var start_time = ((sa == 'PM' ? 12 : 0) + (sh % 12)) * 100 + 1 * sm;
  var end_time = ((ea == 'PM' ? 12 : 0) + (eh % 12)) * 100 + 1 * em;
  
  // alert(start_time);
  // alert(end_time);
  if (end_time <= start_time)
  {
    document.getElementById('time_error').style.display = "block";
    form_incomplete = true;
  }

  if (form_incomplete) {
    alert("Please check your input!");
  }
  return !form_incomplete;
}
