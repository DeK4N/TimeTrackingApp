from flask import Blueprint, render_template, request
# from ..services import TimesheetService

maindashboard = Blueprint('maindashboard', __name__, url_prefix='/')

# api_client = TimesheetService()

@maindashboard.route('/', methods=['GET'])
def dashboard_home():
    return render_template('main-dashboard-base.html')