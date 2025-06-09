from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='MiniRepo API',
          description='A simple API with documentation', doc='/url/docs/')

ns = api.namespace('user', description='用户路由')


@ns.route('/')
class UserList(Resource):
    @ns.doc('list_users')
    def get(self):
        return []

    @ns.doc("post_users")
    def post(self):
        return {}


@ns.route('/<int:user_id>')
@ns.response(404, 'User not found')
@ns.param('user_id', '用户唯一标识')
class User(Resource):
    @ns.doc('get_user')
    def get(self, user_id):
        return {'user_id': user_id}

    @ns.doc('put_user')
    def put(self, user_id):
        return {}

    @ns.doc('delete_user')
    def delete(self, user_id):
        return {'result': True}, 204


if __name__ == '__main__':
    app.run(debug=True)
