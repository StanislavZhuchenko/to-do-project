from flask import Blueprint, render_template, request, session, redirect, url_for
from todo.db import get_db

bp = Blueprint('index', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()
    user_id = session.get('user_id')
    if request.method == 'GET':
        tasks = db.execute(
            'SELECT * FROM list WHERE list.user_id = ? ORDER BY priority DESC', (user_id, )
        ).fetchall()

    elif request.method == 'POST':
        title = request.form['title']
        status = 'In progress'
        priority = request.form['priority']
        db.execute(
            'INSERT INTO list (title, user_id, status, priority) '
            'VALUES (?, ?, ?, ?)', (title, user_id, status, priority)
        )
        db.commit()
        return redirect(url_for('index.index'))

    return render_template('base.html', tasks=tasks)


@bp.route('/remove', methods=('POST', ))
def removetask():
    db = get_db()
    if request.method == 'POST':
        values = request.form.getlist('task')
        for value in values:
            db.execute(
                'DELETE FROM list WHERE id = ?', (value, )
            )
            db.commit()
        return redirect(url_for('index.index'))



