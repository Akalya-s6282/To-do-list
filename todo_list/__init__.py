

from flask import Flask, render_template, request

# these
from .clear import clear_bp
from .db import db
from .manage import manage_bp
from .models import Todo
from .update import update_bp


def create_app():
   
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning
    
    
    db.init_app(app) 



    app.register_blueprint(manage_bp)
    app.register_blueprint(update_bp)
    app.register_blueprint(clear_bp)
    
    with app.app_context():
        db.create_all() 
    
    # okay the imports 
    @app.route("/", methods=['GET','POST'])
    def index():
        if request.method=="POST":
            task = request.form.get("Task")
            progress =  "Not started"
            p = Todo(task=task, status=progress)
            db.session.add(p)
            db.session.commit()
        profiles = Todo.query.all()
        return render_template("index.html",profiles=profiles)
    
    
    
    return app


