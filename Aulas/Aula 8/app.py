from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tks = []


@app.route('/')
def home():
    nomepage = 'ToDo List'
    return render_template('index.html', nomepage=nomepage, tks=tks)


@app.route('/nova', methods=['POST', 'GET'])
def new_task():
    if request.method == 'POST':
        tks.append(request.form['task'])
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
