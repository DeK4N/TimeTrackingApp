from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.services.projects_service import ProjectsService
from app.services.projectLines_service import ProjectLines

projects_service = ProjectsService()
project_lines_service = ProjectLines()

projects = Blueprint('projects', __name__, url_prefix='/projects')


@projects.route('/', methods=['GET'])
def projects_home():
    data = projects_service.get_projects()
    project_lines = project_lines_service.get_lines()
    return render_template('projects/projects.html', data = data, project_lines=project_lines)


@projects.route('/get-projects', methods=['GET'])
def get_projects():
    data = projects_service.get_projects()
    return render_template('projects/regenerate_projects.html', data = data)


@projects.route('/save', methods=['POST'])
def save_project():
    data = request.get_json()
    projects_service.save_project(data)
    return data

@projects.route('/create', methods=['POST'])
def create_project():
    data = request.get_json()
    projects_service.create_project(data)
    return data


@projects.route('/delete/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    projects_service.delete_project(project_id)
    data = projects_service.get_projects()
    return data