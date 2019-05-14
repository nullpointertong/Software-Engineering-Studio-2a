function selectDate (formatted_date) {
  var time_select = document.getElementById("sess_time_select");
  time_select.style.display = "block";

  var date_input = document.querySelector('input[type="date"]');
  date_input.value = formatted_date;
}