from flask import Blueprint, render_template, request, flash, redirect, url_for
from todo.db import get_db

bp = Blueprint('detailstask', __name__, url_prefix='/task')


@bp.route('/<int:id>')
def current_task(id):
    db = get_db()
    cur_task = db.execute(
        'SELECT * FROM list WHERE id = ?', (id, )
    ).fetchone()
    return render_template('tasks/detailstask.html', cur_task=cur_task)


@bp.route('/<int:id>/update', methods=('POST', ))
def update_task(id):
    db = get_db()
    error = None
    # добавить метод Гет чтобы загружались обновленные данные
    if request.method == 'POST':
        priority = request.form['priority']
        title = request.form['title']
        due_date = request.form['due_date']
        description = request.form['description']

        if not title:
            error = 'Title is required'

        if error is not None:
            flash(error)
        else:
            db.execute(
                'UPDATE list SET title = ?, description = ?, due_date = ?, priority =? WHERE id = ?',
                (title, description, due_date, priority, id)
            )
            db.commit()
        return redirect(url_for('index.index', id=id))

    return redirect(url_for('detailstask.current_task', id=id))


@bp.route('/<int:id>/delete', methods=('POST', ))
def delete_current_task(id):
    db = get_db()
    if request.method == 'POST':
        db.execute(
                'DELETE FROM list WHERE id = ?', (id, )
            )
        db.commit()
        return redirect(url_for('index.index'))

