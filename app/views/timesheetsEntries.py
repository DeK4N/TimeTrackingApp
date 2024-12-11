from flask import Blueprint, render_template, request, redirect, url_for
from ..services.timesheetEntry_service import timesheetEntry
from datetime import datetime

timesheet_entries = Blueprint('timesheet_entries', __name__, url_prefix='/timesheets-entries')

api_client = timesheetEntry()

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
    response = api_client.create_entry(data)
    return response.json()