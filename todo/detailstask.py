from flask import Blueprint, render_template
from todo.db import get_db

bp = Blueprint('detailstask', __name__, url_prefix='/task')


@bp.route('/<int:id>')
def current_task(id):
    db = get_db()
    cur_task = db.execute(
        'SELECT * FROM list WHERE id = ?', (id, )
    ).fetchone()
    return render_template('tasks/detailstask.html', cur_task=cur_task)
