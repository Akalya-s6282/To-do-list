from flask import Blueprint, redirect

#from . import db
from .db import db
from .models import Todo

clear_bp = Blueprint('clear_bp',__name__)
@clear_bp.route('/clear/', methods=['GET','POST'])
def clear():
    Todo.query.delete()
    db.session.commit()
    return redirect('/')

