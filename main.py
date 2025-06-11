from flask import Flask, render_template

app = Flask(__file__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/u/home')
def home():
    return render_template("user/home.html")


@app.route('/u/setting')
def setting():
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


# 侧边栏路由
@app.route('/dashboard/workbenches')
def dashboard_workbenches():
    return render_template("dashboard/workbenches.html")


@app.route('/dashboard/projects')
def dashboard_projects():
    return render_template("dashboard/projects.html")


@app.route('/dashboard/groups')
def dashboard_groups():
    return render_template("dashboard/groups.html")


@app.route('/dashboard/merge_requests')
def dashboard_merge_requests():
    return render_template("dashboard/merge_requests.html")


@app.route('/dashboard/todos')
def dashboard_todos():
    return render_template("dashboard/todos.html")


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
