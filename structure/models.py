#models.py
from structure import db,login_manager,app
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))


    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username {self.username}"



# class Report(db.Model):
#     __seachbale__ = ['name','description']
#     id = db.Column(db.Integer, primary_key=True)
#     color = db.Column(db.Text, nullable=False)
#     pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
#     description = db.Column(db.String(255), nullable= True)
#     car_number = db.Column(db.String(255), nullable= True)
#     car_type = db.Column(db.String(255), nullable= True)
#     # assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=True)

#     pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
#     # category = db.relationship('Category',backref=db.backref('category', lazy=True))

#     userr_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
#     # userr = db.relationship('User',backref=db.backref('users', lazy=True))

#     image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
#     image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
#     image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')

#     def __repr__(self):
#         return '<Addproduct %r>' % self.name
# admin.add_view(ModelView(Report,db.session))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
