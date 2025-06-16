from flask import Blueprint, render_template
from Table import Profile

manage_bp = Blueprint('manage_bp', __name__)
@manage_bp.route("/Manage.html", methods=['GET','POST'])
def manage():
    profiles = Profile.query.all()
    return render_template("Manage.html",profiles=profiles )

