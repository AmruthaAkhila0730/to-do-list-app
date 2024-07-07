from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks, enumerate=enumerate)

@app.route('/add', methods=['POST'])
def add_task():
    task_description = request.form.get('task')
    if task_description:
        new_task = Task(description=task_description)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/remove/<int:task_id>')
def remove_task(task_id):
    task_to_remove = Task.query.get_or_404(task_id)
    db.session.delete(task_to_remove)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task_to_complete = Task.query.get_or_404(task_id)
    task_to_complete.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        new_description = request.form.get('task')
        if new_description:
            task.description = new_description
            db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', task=task, task_id=task_id)

if __name__ == "__main__":
    app.run(debug=True)
