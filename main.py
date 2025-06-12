from flask import redirect, url_for
from core import create_app


app = create_app()


@app.route("/")
def index():
    return redirect(url_for("dashboard.workbenches"))


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="127.0.0.1")
