from flask import Blueprint, render_template, request, redirect, url_for
from ..services.timesheet_service import TimesheetService
from ..services.timesheetEntry_service import timesheetEntry
from datetime import datetime

timesheets = Blueprint('timesheets', __name__, url_prefix='/timesheets')

api_client = TimesheetService()
api_client_entries = timesheetEntry()

@timesheets.route('/', methods=['GET'])
def timesheets_home():
    timesheets = api_client.get_timesheets()
    return render_template('timesheets/timesheets.html', timesheets=timesheets)

@timesheets.route('/<int:timesheet_id>')
def refresh_timesheet(timesheet_id):
    timesheet = api_client.get_timesheet_data(timesheet_id)
    entries = api_client_entries.get_timesheet_entries(timesheet_id)
    print(entries)
    return render_template('timesheets/regenerate_timesheets_wrapper.html', timesheet=timesheet, entries=entries)
