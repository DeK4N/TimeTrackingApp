from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.services.projectLines_service import ProjectLines

project_lines_service = ProjectLines()

project_lines = Blueprint('project_lines', __name__, url_prefix='/project-lines')

@project_lines.route('/get-lines/<int:project_id>', methods=['GET'])
@project_lines.route('/get-lines/<int:project_id>/<string:action>', methods=['GET'])
def get_lines(project_id, action = None):
    project_lines = project_lines_service.get_project_lines(project_id)
    if action == 'data':
        return project_lines
    else:
        return render_template('projects/regenerate_project_lines.html', project_lines = project_lines, project={"id": project_id})

@project_lines.route('/create', methods=['POST'])
def create_line():
    data = request.get_json()
    response = project_lines_service.create_line(data)
    return response

@project_lines.route('/save', methods=['POST'])
def save_lines():
    data = request.get_json()
    project_lines_service.save_lines(data)
    return data

@project_lines.route('/delete/<int:line_id>', methods=['DELETE'])
def delete_line(line_id):
    response = project_lines_service.delete_line(line_id)
    return response