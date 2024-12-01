from flask import Blueprint, render_template, request
# from ..services import TimesheetService

notes = Blueprint('notes', __name__, url_prefix='/notes')

# api_client = TimesheetService()

@notes.route('/', methods=['GET'])
def notes_home():
    return render_template('notes-base.html')