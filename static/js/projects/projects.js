const newProjectPopup = document.getElementById('new-project-popup');
const cancelBtn = document.getElementById('cancel-btn');
const createProjectPopBtn = document.getElementById('create-new-project-pop');
const createProjectAPIBtn = document.getElementById('create-btn')

function deleteProject(project_id){
    main = document.getElementById('projectsList')
    fetch(`/projects/delete/${project_id}`, {
        method: 'POST'
    })
    .then(() => {
        regenerateProjectsData()
    })
}

createProjectAPIBtn.addEventListener('click', () =>{
    main = document.getElementById('projectsList')

    data = {
        'user_id': 1,
        'project_name': document.getElementById('project-name').value,
        'project_status': document.getElementById('project-status').value,
        'project_details': document.getElementById('project-notes').value
    }

    fetch('/projects/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(() => {
        fetch('/projects/get-projects', {
            method: 'GET'
        })
        .then(response => {
            return response.text();
        })
        .then(html => {
            main.innerHTML = html
        })
    })

    newProjectPopup.style.display = 'none'
})

createProjectPopBtn.addEventListener('click', () => {
    newProjectPopup.style.display = 'block';
    newProjectPopup.classList.add('animate-slide-down');
})

cancelBtn.addEventListener('click', () => {
    newProjectPopup.style.display = 'none';
    newProjectPopup.classList.remove('animate-slide-down');
});

function createNewLine(project_id){
    const linesTable = document.querySelector(`#table-content-${project_id} tbody`);
    const linesExists = document.querySelector(`#no-lines-${project_id}`)
    if(linesExists){
        const row = linesExists.closest('tr')
        row.remove()
    }

    temp_data = {
        "project_id": project_id,
        "line_name": "",
        "line_details": ""
    }
    fetch('/project-lines/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(temp_data) 
    })
    .then(() => {
        regenerateProjectLines(project_id)
    })
}

function deleteLine(project_id){
    const linesTable = document.querySelector(`#table-content-${project_id} tbody`);
    const row = event.target.closest("tr")
    const line_id = row.querySelectorAll('.project-line-item')[0].value
    fetch(`/project-lines/delete/${line_id}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    row.remove()
}


function saveProject(project_id){
    const wrapper = document.getElementById(`project-wrapper-${project_id}`)
    const projectLines = wrapper.querySelectorAll('.project-line-data')
    const data = wrapper.querySelectorAll('.project-data-item')
    let inputs = []
    let lines = []

    data.forEach(elem => {
        if (elem.tagName === 'SPAN') {
            inputs.push(elem.innerText)            
        }
        if (elem.tagName === 'TEXTAREA'){
            inputs.push(elem.value)
        }
    })

    project = {
        "user_id": 1,
        "project_id": project_id,
        "project_name": inputs[0],
        "project_status": inputs[1],
        "project_details": inputs[2],
    }
    
    projectLines.forEach(line => {
        inputs = line.querySelectorAll('.project-line-item')
        result = {
            "line_id": parseInt(inputs[0].value), 
            "project_id": parseInt(project_id),
            "line_name": inputs[1].value, 
            "line_details": inputs[2].value
        }
        lines.push(result)
    })

    fetch('/projects/save', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(project)
    })
    .then(() => {
        fetch('/project-lines/save', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(lines) 
        })
    }) 
}


function regenerateProjectsData (){
    main = document.getElementById('projectsList')
    fetch('/projects/get-projects', {
        method: 'GET'
    })
    .then(response => {
        return response.text();
    })
    .then(html => {
        main.innerHTML = html
    })
}

function regenerateProjectLines(project_id){
    main = document.querySelector(`.project-lines-${project_id}`)
    fetch(`/project-lines/get-lines/${project_id}`, {
        method: 'GET'
    })
    .then(response => {
        return response.text();
    })
    .then(html => {
        main.innerHTML = html
    })
}