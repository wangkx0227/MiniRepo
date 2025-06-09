import os
import subprocess
from flask import Flask, request, Response

app = Flask(__name__)

GIT_PROJECT_ROOT = os.path.abspath('./repos')
GIT_HTTP_BACKEND = 'git-http-backend'


@app.route('/<path:repo_path>', methods=['GET', 'POST'])
def git_service(repo_path):
    env = os.environ.copy()
    env['GIT_PROJECT_ROOT'] = GIT_PROJECT_ROOT
    env['GIT_HTTP_EXPORT_ALL'] = '1'
    env['REMOTE_USER'] = 'user'
    env['PATH_INFO'] = '/' + repo_path
    env['REQUEST_METHOD'] = request.method
    env['QUERY_STRING'] = request.query_string.decode()
    env['CONTENT_TYPE'] = request.content_type or ''
    env['REMOTE_ADDR'] = request.remote_addr
    env['AUTH_TYPE'] = 'Basic'

    input_data = request.get_data()

    p = subprocess.Popen(
        [GIT_HTTP_BACKEND],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env
    )
    stdout, stderr = p.communicate(input_data)

    status_line = stdout.split(b'\r\n')[0].decode()
    status_code = int(status_line.split(' ')[1]) if ' ' in status_line else 200

    return Response(stdout, status=status_code)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
