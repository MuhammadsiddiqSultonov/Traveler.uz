from flask_admin.contrib.sqla import ModelView
from app.db_models import PackDay, ToursCat, ToursInfo, Team, Travlio, Question, Answer, User
from app import db
from . import admins

res = db.session.query(packday, toursinfo).join(packday, toursinfo.id == packday.pack_id).all()

admins.add_view(ModelView(PackDay, db.session, 'Пакеты'))
admins.add_view(ModelView(ToursCat, db.session, 'Категории'))
admins.add_view(ModelView(ToursInfo, db.session, 'Tours'))
admins.add_view(ModelView(Team, db.session, 'Команда'))
admins.add_view(ModelView(Travlio, db.session, 'О компании'))
admins.add_view(ModelView(Question, db.session, 'Ч.З.Вопросы'))
admins.add_view(ModelView(Answer, db.session, 'Ответы'))
admins.add_view(ModelView(User, db.session, 'Админы'))