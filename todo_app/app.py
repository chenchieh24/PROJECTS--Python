from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    if todo:
        todos.append({'task': todo, 'done': False})
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        todos[todo_id]['done'] = True
    return redirect(url_for('index'))

@app.route('/delete_completed')
def delete_completed():
    global todos
    todos = [todo for todo in todos if not todo['done']]
    return redirect(url_for('index'))

@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)

