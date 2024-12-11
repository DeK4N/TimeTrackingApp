import requests as req
import json
from datetime import datetime

class ProjectsService():
    def __init__(self):
        self.url = 'http://127.0.0.1:8000/projects'

    def get_projects(self):
        response = req.get(self.url).json()
        return response
    
    def save_project(self, data):
        save_url = self.url + '/save'
        response = req.post(save_url, json=data)
        return response
    
    def create_project(self, data):
        create_url = self.url + '/create'
        response = req.post(create_url, json=data)
        return response
    
    def delete_project(self, project_id):
        delete_url = self.url + '/delete/' + str(project_id)
        response = req.delete(delete_url)
        return response
    


