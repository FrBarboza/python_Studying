from sql_alchemy import database


class UserModel(database.Model):
    __tablename__ = 'users'

    user_id = database.Column(database.Integer, primary_key=True)
    login = database.Column(database.String(40))
    password = database.Column(database.String(40))

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login
        }

    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()
        if user:
            return user
        return None

    @classmethod
    def find_by_login(cls, login):
        user = cls.query.filter_by(login=login).first()
        if user:
            return user
        return None

    def save_user(self):
        database.session.add(self)
        database.session.commit()

    # def update_user(self, nome, estrelas, diaria, cidade):
    #     self.nome = nome
    #     self.estrelas = estrelas
    #     self.diaria = diaria
    #     self.cidade = cidade

    def delete_user(self):
        database.session.delete(self)
        database.session.commit()
