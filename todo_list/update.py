from flask import Blueprint, redirect, request

from .db import db
from .models import Todo

update_bp = Blueprint('update_bp', __name__)
@update_bp.route('/update/<id>', methods=['GET','POST'])
def update(id):
    Function = request.form.get("function")
    Task = request.form.get("Task")
    Progress = request.form.get("Status")
    task = Todo.query.get_or_404(id)
    data = Todo.query.get(id)
    data.task = Task
    data.status = Progress
    if(Function=="delete"):
       db.session.delete(task) 
    db.session.commit()
    return redirect('/Manage.html')


