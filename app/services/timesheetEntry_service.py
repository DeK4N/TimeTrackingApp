import requests as req
import json
from datetime import datetime

class timesheetEntryService():
    def __init__(self):
        self.url = 'http://127.0.0.1:8000/timesheet-entries'

    def get_entries(self):
        response = req.get(self.url)
        return response.json()

    def get_timesheet_entries(self, timesheet_id):
        get_entries_url = self.url + "/" + str(timesheet_id)
        response = req.get(get_entries_url)
        return response.json()
    
    def create_entry(self, data):
        create_entry_url = self.url + '/create'
        response = req.post(create_entry_url, json=data)
        return response
    
    def delete_entry(self, entry_id):
        delete_entry_url = self.url + '/delete/' + str(entry_id)
        response = req.delete(delete_entry_url)
        return response
    
    def update_entry(self, entry_id, data):
        update_entry_url = self.url + '/update/' + str(entry_id)
        response = req.put(update_entry_url, json=data)
        return response