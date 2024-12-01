from flask import Flask
from app.views.maindashboard import maindashboard
from app.views.notes import notes
from app.views.timesheets import timesheets


app = Flask(__name__)

app.register_blueprint(notes)
app.register_blueprint(timesheets)
app.register_blueprint(maindashboard)

if __name__ == "__main__":
    app.run(debug=False)