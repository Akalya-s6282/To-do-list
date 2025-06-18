from flask import Blueprint, render_template

from .models import Todo

manage_bp = Blueprint('manage_bp', __name__)
@manage_bp.route("/Manage.html", methods=['GET','POST'])
def manage():
    profiles = Todo.query.all()
    return render_template("Manage.html",profiles=profiles )

