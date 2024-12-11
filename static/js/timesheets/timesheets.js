function getTimesheetData(dropdown){
    const timesheet_id = dropdown.value;
    const main = document.querySelector('.timesheet-wrapper');

    fetch(`/timesheets/${timesheet_id}`, {
        method: 'GET'
    })
    .then(response => {
        return response.text();
    })
    .then(html => {
        main.innerHTML = html;
    })
    .then(() => {
        main.removeChild(main.firstChild);
    })

    const table = document.querySelector('.timesheet-wrapper');

    fetch(`/timesheets-entries/${timesheet_id}`, {
        method: 'GET'
    })
    .then(response => {
        return response.text()
    })
    .then((html) => {
        console.log(html)
    })
}



function addNewTimeEntry(){
    const table = document.querySelector('.timeentires-table')
    const timesheet_id = document.getElementById('timesheet-dropdown-item').value
    temp_data = {
        "timesheet_id": parseInt(timesheet_id),
        "user_id": 1,
        "project_id": 0,
        "project_line_id": 0,
        "ticket": "",
        "time_spent": 0,
        "notes": ""
    }
    console.log(temp_data)
    fetch('/timesheets-entries/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(temp_data) 
    })

}