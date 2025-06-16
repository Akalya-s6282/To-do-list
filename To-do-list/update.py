from flask import  Blueprint, request, redirect
from Table import db, Profile

update_bp = Blueprint('update_bp', __name__)
@update_bp.route('/update/<id>', methods=['GET','POST'])
def update(id):
    Function = request.form.get("function")
    Task = request.form.get("Task")
    Progress = request.form.get("Status")
    task = Profile.query.get_or_404(id)
    data = Profile.query.get(id)
    data.task = Task
    data.status = Progress
    if(Function=="delete"):
       db.session.delete(task) 
    db.session.commit()
    #return render_template("Manage.html",profiles=profiles )
    return redirect('/Manage.html')
