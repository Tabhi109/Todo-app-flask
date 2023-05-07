from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append(task)
    return redirect('/')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        tasks[index] = request.form['task']
        return redirect('/')
    else:
        return render_template('edit.html', task=tasks[index])

@app.route('/delete/<int:index>')
def delete(index):
    tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
