import requests as req
from datetime import datetime

class ProjectLines():
    def __init__(self):
        self.url = 'http://127.0.0.1:8000/project-line'

    def get_lines(self):
        response = req.get(self.url).json()
        return response
    
    def get_project_lines(self, project_id):
        get_lines_url = self.url + "/" + str(project_id)
        response = req.get(get_lines_url).json()
        return response

    def save_lines(self, data):
        save_url = self.url + "/save"
        response = req.post(save_url, json=data).json()
        return response
    
    def create_line(self, data):
        create_url = self.url + "/create"
        response = req.post(create_url, json=data).json()
        return response
    
    def delete_line(self, line_id):
        delete_url = self.url + '/delete/' + str(line_id)
        response = req.delete(delete_url).json()
        return response