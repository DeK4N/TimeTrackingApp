from flask import Blueprint, render_template, request, redirect, url_for
from ..services.timesheetEntry_service import timesheetEntryService
from ..services.projects_service import ProjectsService
from datetime import datetime

timesheet_entries = Blueprint('timesheet_entries', __name__, url_prefix='/timesheets-entries')

api_client = timesheetEntryService()
api_client_project = ProjectsService()

@timesheet_entries.route('/', methods=['GET'])
def timesheets_home():
    entries = api_client.get_entries()
    return render_template('timesheets/timesheets.html', entries=entries, )

@timesheet_entries.route('/<int:timesheet_id>', methods=['GET'])
def get_entries(timesheet_id):
    entries = api_client.get_timesheet_entries(timesheet_id)
    return render_template('timesheets/regenerate_timesheets_wrapper.html', entries=entries)

@timesheet_entries.route('/create', methods=['POST'])
def create_entry():
    data = request.get_json()
    projects = api_client_project.get_projects()
    entry = api_client.create_entry(data).json()['entry']
    print(entry)
    return render_template('timesheets/new_row.html', projects=projects, entry=entry)

@timesheet_entries.route('/delete/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    response = api_client.delete_entry(entry_id)
    return response.json()

@timesheet_entries.route('/update/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    data = request.get_json()
    response = api_client.update_entry(entry_id, data)
    return response.json()