from flask import Blueprint, render_template, request, redirect, url_for
from ..services.timesheet_service import TimesheetService
from datetime import datetime

timesheets = Blueprint('timesheets', __name__, url_prefix='/timesheets')

api_client = TimesheetService()

@timesheets.route('/', methods=['GET'])
def timesheets_home():
    timesheets = api_client.get_timesheets()
    return render_template('timesheets-base.html', timesheets=timesheets)


@timesheets.route('/create', methods=['POST'])
def create_timesheet():
    new_timesheet = {
        'user_id': '1',
        'year': datetime.now().year,
        'month': request.form['month'],
        'status': 'Pending',
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    api_client.create_timesheet(data=new_timesheet)
    return redirect(url_for('timesheets.timesheets_home'))


@timesheets.route('/delete/<int:timesheet_id>', methods=['POST'])
def delete_timesheet(timesheet_id):
    api_client.delete_timesheet(timesheet_id)
    return redirect(url_for('timesheets.timesheets_home'))


@timesheets.route('/timesheet/<int:timesheet_id>', methods=['GET'])
def timesheet_data(timesheet_id):
    result = api_client.get_timesheet_details(timesheet_id)
    print(result)
    return render_template('timesheets-content.html', data = result)
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
