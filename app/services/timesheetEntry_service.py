import requests as req
import json
from datetime import datetime

class timesheetEntry():
    def __init__(self):
        self.url = 'http://127.0.0.1:8000/timesheet-entries'

    def get_entries(self):
        response = req.get(self.url)
        return response

    def get_timesheet_entries(self, timesheet_id):
        get_entries_url = self.url + "/" + str(timesheet_id)
        response = req.get(get_entries_url)
        print(response)
        return response
    
    def create_entry(self, data):
        create_entry_url = self.url + '/create'
        response = req.post(create_entry_url, data)
        return response