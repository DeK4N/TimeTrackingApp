from flask import Flask
from app.views.maindashboard import maindashboard
from app.views.timesheets import timesheets
from app.views.timesheetsEntries import timesheet_entries
from app.views.projects import projects
from app.views.projectLines import project_lines


app = Flask(__name__)

app.register_blueprint(maindashboard)
app.register_blueprint(timesheets)
app.register_blueprint(timesheet_entries)
app.register_blueprint(projects)
app.register_blueprint(project_lines)

if __name__ == "__main__":
    app.run(debug=False)