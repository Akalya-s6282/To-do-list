from flask import Blueprint,  redirect
from Table import db, Profile

clear_bp = Blueprint('clear_bp',__name__)
@clear_bp.route('/clear/', methods=['GET','POST'])
def clear():
    Profile.query.delete()
    db.session.commit()
    return redirect('/')

