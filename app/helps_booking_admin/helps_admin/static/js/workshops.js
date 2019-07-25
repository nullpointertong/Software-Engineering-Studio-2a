$(document).ready(function(){
    $('sesssion_table').DataTable();
  });
  
  var selectedDate = null;
  
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
    var title_input = document.getElementById('workshop_title');
    var skill_input = document.getElementById('workshop_skillset');
    var capacity_input = document.getElementById('workshop_capacity');
    var advisor_input = document.getElementById('advisor_search');
    var location_input = document.getElementById('location_input');
    var date_input = document.getElementById('date');
    var sh = document.getElementById('hour-start').value;
    var sm = document.getElementById('min-start').value;
    var eh = document.getElementById('hour-end').value;
    var em = document.getElementById('min-end').value;
    var form_incomplete = false;
    if (title_input.value === "")
    {
      title_input.placeholder = "Required field!";
      title_input.style.color = "red";
      form_incomplete = true;
    }
    if (advisor_input.value === "")
    {
      advisor_input.placeholder = "Required field!";
      advisor_input.style.color = "red";
      form_incomplete = true;
    }
    if (location_input.value === "")
    {
        location_input.placeholder = "Required field!";
        location_input.style.color = "red";
        form_incomplete = true;
    }
    if (skill_input.value === "")
    {
        skill_input.placeholder = "Required field!";
        skill_input.style.color = "red";
        form_incomplete = true;
    }
    if (capacity_input.value === "")
    {
        capacity_input.placeholder = "Required field!";
        capacity_input.style.color = "red";
        form_incomplete = true;
    }

    var start_time = 100 * sh + 1 * sm;
    var end_time =  100 * eh + 1 * em;
    
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
  
  
  function setTime() {
    var sh = document.getElementById('hour-start').value;
    var sm = document.getElementById('min-start').value;
    var eh = document.getElementById('hour-end').value;
    var em = document.getElementById('min-end').value;
    var s_disp = document.getElementById('start_time_disp');
    var e_disp = document.getElementById('end_time_disp');
    s_disp.innerHTML = convert_to_twelve_hour(sh, sm);
    e_disp.innerHTML = convert_to_twelve_hour(eh, em);
  }
  
  function convert_to_twelve_hour(hour, minute) {
    var tod = hour < 12 ? 'AM' : 'PM';
    hour = (1 * hour) % 12;
    if (hour === 0) hour = 12;
    return hour + ':' + minute + ' ' + tod;
  }
  
  
  function formElementChange() {
    setTime();
    try {
      document.getElementById('booking_span').style.display = 'none';
    } catch (e) { }
  }
  
  function confirmBooking() {
    var form = document.forms['create_workshop'];
    document.getElementById('confirm_hidden').value = 'yes';
    form.submit();
  }
  
  
  function toMonth(month) {
    month = month.split('month=')
  }
  
  function popup(mylink, windowname) { 
    if (! window.focus)return true;
    var href;
    if (typeof(mylink) == 'string') href=mylink;
    else href=mylink.href; 
    window.open(href, windowname, 'width=400,height=200,scrollbars=yes'); 
    return false; 
  }
  
  function deleteBooking(sesid) {
    var form = document.forms['delete_session'];
    form.submit();
  }