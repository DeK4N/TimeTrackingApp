let before_edit;

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
    .catch(error => {
        console.error("Error fetching timesheet data:", error);
    });

    const table = document.querySelector('.timesheet-wrapper');

    fetch(`/timesheets-entries/${timesheet_id}`, {
        method: 'GET'
    })
    .then(response => {
        return response.text()
    })
    .then(html => {
        table.innerHTML = html
    })
    .catch(error => {
        console.error("Error fetching timesheet entries:", error);
    });
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
        "notes": "",
        "date": ""
    }
    fetch('/timesheets-entries/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(temp_data) 
    })
    .then(response => {
        return response.text()
    })
    .then(html => {
        table.insertAdjacentHTML('afterbegin', html);
    })
}

function addNewItemToTable(data){
    const table = document.querySelector('.timeentires-table')
    const table_body = table.querySelector('tbody')
    const new_row = document.createElement('tr')
    new_row.setAttribute('data-entry-id', data.id);

    new_row.innerHTML = `
        <td><input type="date" class="form-control form-control-sm entry-input" value="${data.date}" /></td>
        <td><input type="number" class="form-control form-control-sm entry-input" value="${data.project_id}" /></td>
        <td><input type="number" class="form-control form-control-sm entry-input" value="${data.project_line_id}" /></td>
        <td><input type="text" class="form-control form-control-sm entry-input" value="${data.ticket}" /></td>
        <td><input type="number" class="form-control form-control-sm entry-input" value="${data.time_spent}" /></td>
        <td><input type="text" class="form-control form-control-sm entry-input" value="${data.notes}" /></td>
        <td>
            <button class="btn btn-danger btn-sm delete-entry">Delete</button>
        </td>
    `;
    table_body.prepend(new_row)
}


function deleteTimeEntry(event, entry_id) {
    fetch(`/timesheets-entries/delete/${entry_id}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => {
        if(response.ok){
            const button = event.target
            const row = button.closest('tr')
            row.remove()
        }
    })
}

function saveEntryData(entry_id, field_name, new_value) {
    fetch(`/timesheets-entries/update/${entry_id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "field_name": field_name,
            "value": new_value
        })
    })
}

document.addEventListener('DOMContentLoaded', () => {
    const main = document.querySelector('.timesheet-wrapper');
    
    main.addEventListener('click', (event)=> {
        if (event.target.classList.contains('delete-entry')) {
            const row = event.target.closest('tr')
            entry_id = row.getAttribute('data-entry-id')
            deleteTimeEntry(event, entry_id)
        }
    })

    main.addEventListener('focusin', (event) => {
        if (event.target.classList.contains('entry-input')) {
            before_edit = event.target.value
        }
    })

    main.addEventListener('focusout', (event) => {
        let new_value;
        if (event.target.classList.contains('entry-input')) {
            new_value = event.target.value
            if (new_value != before_edit) {

                const row = event.target.closest('tr')
                const field_name = event.target.getAttribute('name')

                const entry_id = row.getAttribute('data-entry-id')

                saveEntryData(entry_id, field_name, new_value)

                if (event.target.getAttribute('name') == 'project_id') {
                    const project_id = event.target.value
                    fetch(`/project-lines/get-lines/${project_id}/data`, {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    })
                    .then(response => {
                        return response.json()
                    })
                    .then(data => {
                        const lines_dropdown = row.querySelector('#project-line-dropdown')
                        lines_dropdown.innerHTML = ''
                        const default_option = document.createElement('option');
                        default_option.value = 0
                        default_option.textContent = 'Select a project line'
                        default_option.setAttribute('selected', true);
                        default_option.setAttribute('disabled', true)
                        lines_dropdown.appendChild(default_option)
                        
                        saveEntryData(entry_id, 'project_line_id', '0')

                        data.forEach(line => {
                            const new_option = document.createElement('option');
                            new_option.value = line.id;
                            new_option.textContent = line.line_name;

                            lines_dropdown.appendChild(new_option);
                        });
                    })
                }
            }
        } 
    })
});


