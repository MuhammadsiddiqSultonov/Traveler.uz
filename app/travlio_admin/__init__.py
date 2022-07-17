from flask import Blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import db
from app.db_models import PackDay, ToursCat, ToursInfo, Team, Travlio, Question, Answer, User
from app import app

shef = Blueprint(
    'shef', __name__,
    template_folder='admin-templates',
    static_folder='admin-static'
)

admins = Admin(app, name='Travlio', template_mode='bootstrap3')


admins.add_view(ModelView(PackDay, db.session, 'Пакеты'))
admins.add_view(ModelView(ToursCat, db.session, 'Категории'))
admins.add_view(ModelView(ToursInfo, db.session, 'Tours'))
admins.add_view(ModelView(Team, db.session, 'Команда'))
admins.add_view(ModelView(Travlio, db.session, 'О компании'))
admins.add_view(ModelView(Question, db.session, 'Ч.З.Вопросы'))
admins.add_view(ModelView(Answer, db.session, 'Ответы'))
admins.add_view(ModelView(User, db.session, 'Админы'))

class MyModelView(ModelView):

    form_args = {
        'second_city': {
            'validators': []
        }
    }