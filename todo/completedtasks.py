from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from todo.db import get_db

bp = Blueprint('completedtasks', __name__, url_prefix='/completed')


@bp.route('/', methods=('GET', ))
def get_all_done():
    db = get_db()
    user_id = session.get('user_id')
    status = 'Done'
    if request.method == 'GET':
        completed_tasks = db.execute(
            'SELECT * FROM list WHERE list.user_id = ? AND status = ? ORDER BY id DESC', (user_id, status)
        ).fetchall()
        return render_template('tasks/completedtasks.html', completed_tasks=completed_tasks)

