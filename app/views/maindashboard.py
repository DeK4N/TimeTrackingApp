from flask import Blueprint, render_template, request

maindashboard = Blueprint('maindashboard', __name__, url_prefix='/')

@maindashboard.route('/', methods=['GET'])
def dashboard_home():
    return render_template('website-base.html')