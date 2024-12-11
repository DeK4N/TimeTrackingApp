import requests as req
import json
from datetime import datetime

class TimesheetService():
    def __init__(self):
        self.url = 'http://127.0.0.1:8000/timesheets'

    def get_timesheets(self):
        response = req.get(self.url).json()
        sorted_response = sorted(response, key=lambda x: (x['year'], datetime.strptime(x['month'], '%B').month))
        return sorted_response
    
    def get_timesheet_data(self, timesheet_id):
        get_data_url = self.url + '/' + str(timesheet_id)
        return req.get(get_data_url).json()

    def create_timesheet(self, data):
        create_url = self.url + '/create'
        return req.post(create_url, json=data)
    
    def delete_timesheet(self, timesheet_id):
        delete_url = self.url + '/delete/' + str(timesheet_id)
        return req.post(delete_url)
    
    def get_timesheet_details(self, timesheet_id):
        details_url = self.url + '/details/' + str(timesheet_id)
        return req.get(details_url).json()

