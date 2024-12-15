from flask import Blueprint, render_template, request, redirect, url_for
from ..services.timesheet_service import TimesheetService
from ..services.timesheetEntry_service import timesheetEntryService
from ..services.projects_service import ProjectsService
from ..services.projectLines_service import ProjectLines
from datetime import datetime

timesheets = Blueprint('timesheets', __name__, url_prefix='/timesheets')

api_client = TimesheetService()
api_client_entries = timesheetEntryService()
api_client_projects = ProjectsService()
api_client_projects_lines = ProjectLines()

@timesheets.route('/', methods=['GET'])
def timesheets_home():
    timesheets = api_client.get_timesheets()
    return render_template('timesheets/timesheets.html', timesheets=timesheets)

@timesheets.route('/<int:timesheet_id>')
def refresh_timesheet(timesheet_id):
    timesheets = api_client.get_timesheets()
    timesheet = api_client.get_timesheet_data(timesheet_id)
    entries = api_client_entries.get_timesheet_entries(timesheet_id)
    projects = api_client_projects.get_projects()
    project_lines = api_client_projects_lines.get_lines()
    return render_template(
        'timesheets/regenerate_timesheets_wrapper.html', 
        timesheets=timesheets,
        timesheet=timesheet, 
        entries=entries, 
        projects=projects, 
        project_lines=project_lines
    )
