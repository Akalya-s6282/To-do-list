from flask import Flask, render_template, request
from Table import db, Profile
from Manage import manage_bp
from update import update_bp
from Clear import clear_bp
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning
db.init_app(app)
app.register_blueprint(manage_bp)
app.register_blueprint(update_bp)
app.register_blueprint(clear_bp)
@app.route("/", methods=['GET','POST'])
def index():
    if request.method=="POST":
        Task = request.form.get("Task")
        Progress =  "Not started"
        p = Profile(Task=Task, Status=Progress)
        db.session.add(p)
        db.session.commit()
    profiles = Profile.query.all()
    return render_template("index.html",profiles=profiles)



if __name__ == "__main__":
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
    