from flask_restful import Resource, reqparse
from models.user import UserModel
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from blacklist import BLACKLIST

attribute = reqparse.RequestParser()
attribute.add_argument('login', type=str, required=True, help="The field 'login' is required.")
attribute.add_argument('password', type=str, required=True, help="The field 'password' is required.")


class User(Resource):
    # /usuario
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404

    @jwt_required
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            user.delete_user()
            return {'message: ': 'User deleted'}
        return {'message': 'User not found.'}, 404


class UserRegister(Resource):
    # /cadastro
    def post(self):
        data = attribute.parse_args()
        if UserModel.find_by_login(data['login']):
            return {'message': 'The login {} already exists'.format(data['login'])}

        user = UserModel(**data)
        user.save_user()
        return {'message': 'User created successfully.'}, 201  # Created


class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = attribute.parse_args()
        user = UserModel.find_by_login(data['login'])
        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.user_id)
            return {'access_token': access_token}, 200
        return {'message': 'The username or password is incorrect.'}, 401  # Unauthorized


class UserLogout(Resource):

    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti']  # JWT Token Identifier (jti)
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out successfully.'}, 200
