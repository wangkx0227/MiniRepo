from flask import Flask, render_template

app = Flask(__file__)


@app.route('/')
def index():
    lis = 150
    return render_template("index.html")


@app.route('/u/home')
def home():
    lis = 150
    return render_template("user/home.html")


@app.route('/u/setting')
def setting():
    lis = 150
    return render_template("user/setting.html")


@app.route('/u/todos')
def todos():
    return render_template("user/todos.html")


@app.route('/u/related')
def related():
    return render_template("user/related.html")


@app.route('/u/stars')
def stars():
    return render_template("user/stars.html")


@app.route('/u/repos')
def repos():
    return render_template("user/repos.html")

@app.route('/u/projects/new')
def projects():
    return render_template("newadd/projects.html")

@app.route('/u/organizations/new')
def organizations():
    return render_template("newadd/organizations.html")

@app.route('/u/codes/new')
def codes():
    return render_template("newadd/codes.html")
if __name__ == '__main__':
    app.run(debug=True)
