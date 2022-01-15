from flask import render_template,session, request,redirect,url_for,flash,jsonify,Blueprint
from  structure import app,db
from .forms import RegistrationForm,LoginForm
from structure.models import User
from flask_admin.contrib.sqla import ModelView
# from structure.models import Ticket
admins = Blueprint('admins',__name__)

@admins.route('/')
def admin():
#     if 'email' not in session:
#         flash(f'Please Login','danger')
#         return redirect(url_for('admins.login'))
    # products = Addproduct.query.all()
    # tickets = Ticket.query.all()
    return render_template('index.html',title ="Admin Page")


    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    #if form.validate_on_submit():
    #     hash_password = bcrypt.generate_password_hash(form.password.data)
    #     user = User(name=form.name.data,username=form.username.data, email=form.email.data,
    #                 password=hash_password)
    #     db.session.add(user)
    #     flash(f'welcome {form.name.data} Thanks for registering','success')
    #     db.session.commit()
    #     return redirect(url_for('login'))
    # return render_template('admin/register.html',title='Register user', form=form# )