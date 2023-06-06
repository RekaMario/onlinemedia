function updateCalendar() {
    var date = new Date();
    var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    var formattedDate = date.toLocaleDateString('en-US', options);

    document.getElementById('calendar').innerText = formattedDate;
}

// Update the calendar on page load
updateCalendar();

// Update the calendar every second (1000 milliseconds)
setInterval(updateCalendar, 1000);