function openTab(event, tabName) {
    var i, tabcontent, tablinks;

    // Hide all elements with class="tabcontent"
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Remove all "active" class from elements with class="tablinks"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show current tab and add active class to button that opened it
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.className += " active";
}
