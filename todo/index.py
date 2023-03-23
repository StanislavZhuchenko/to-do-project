from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from todo.db import get_db

bp = Blueprint('index', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()
    user_id = session.get('user_id')
    error = None
    status = 'In progress'
    if request.method == 'GET':
        tasks = db.execute(
            'SELECT * FROM list WHERE list.user_id = ? AND status = ?', (user_id, status )
        ).fetchall()
    elif request.method == 'POST':
        title = request.form['title']
        priority = request.form['priority']

        if not title:
            error = 'Title is required'

        if error is not None:
            flash(error)
        else:
            db.execute(
                'INSERT INTO list (title, user_id, status, priority) '
                'VALUES (?, ?, ?, ?)', (title, user_id, status, priority)
            )
            db.commit()
        return redirect(url_for('index.index'))
    return render_template('tasks/listoftasks.html', tasks=tasks)


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


@bp.route('/done', methods=('POST', ))
def mark_as_done():
    db = get_db()
    if request.method == 'POST':
        values = request.form.getlist('task')
        status = 'Done'
        for value in values:
            db.execute(
                'UPDATE list SET status = ? WHERE id = ?', (status, value)
            )
            db.commit()
        return redirect(url_for('index.index'))


@bp.route('/sort_by_date_down')
def sort_task_by_date_desc():
    db = get_db()
    user_id = session.get('user_id')
    status = 'In progress'
    if request.method == 'GET':
        tasks = db.execute(
            'SELECT * FROM list WHERE list.user_id = ? AND status = ? ORDER BY due_date DESC', (user_id, status )
        ).fetchall()
    return render_template('tasks/listoftasks.html', tasks=tasks)


@bp.route('/sort_by_date_asc')
def sort_task_by_date_asc():
    db = get_db()
    user_id = session.get('user_id')
    status = 'In progress'
    if request.method == 'GET':
        tasks = db.execute(
            'SELECT * FROM list WHERE list.user_id = ? AND status = ? ORDER BY due_date ASC', (user_id, status )
        ).fetchall()
    return render_template('tasks/listoftasks.html', tasks=tasks)


@bp.route('/sort_by_priority_asc')
def sort_by_priority_asc():
    db = get_db()
    user_id = session.get('user_id')
    status = 'In progress'
    if request.method == 'GET':
        tasks = db.execute(
            'SELECT * FROM list WHERE list.user_id = ? AND status = ? ORDER BY priority ASC', (user_id, status )
        ).fetchall()
    return render_template('tasks/listoftasks.html', tasks=tasks)


@bp.route('/sort_by_priority_desc')
def sort_by_priority_desc():
    db = get_db()
    user_id = session.get('user_id')
    status = 'In progress'
    if request.method == 'GET':
        tasks = db.execute(
            'SELECT * FROM list WHERE list.user_id = ? AND status = ? ORDER BY priority DESC', (user_id, status )
        ).fetchall()
    return render_template('tasks/listoftasks.html', tasks=tasks)
