from flask import Flask, render_template

app = Flask(__file__)


@app.route('/')
def index():
    lis = 150
    return render_template("index.html")


@app.route('/u/home')
def home():
    lis = 150
    return render_template("home.html")


@app.route('/u/setting')
def setting():
    lis = 150
    return render_template("setting.html")


@app.route('/u/todos')
def todos():
    return render_template("todos.html")


@app.route('/u/related')
def related():
    return render_template("related.html")


@app.route('/u/stars')
def stars():
    return render_template("stars.html")


@app.route('/u/repos')
def repos():
    return render_template("repos.html")


if __name__ == '__main__':
    app.run(debug=True)
