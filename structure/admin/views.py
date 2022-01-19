from flask import render_template,session, request,redirect,url_for,flash,jsonify,Blueprint,current_app
from  structure import app,db,login_manager,photos
from .forms import RegistrationForm,LoginForm,Addtickets
from structure.models import User
from flask_admin.contrib.sqla import ModelView
from structure.models import Ticket,Genre
import secrets
from datetime import datetime
import os




admins = Blueprint('admins',__name__)

@admins.route('/home')
def admin():
#     if 'email' not in session:
#         flash(f'Please Login','danger')
#         return redirect(url_for('admins.login'))
    # products = Addproduct.query.all()
    tickets = Ticket.query.all()
    return render_template('index.html',title ="Admin Page",tickets=tickets)

 
    
@admins.route('/addticket', methods=['GET','POST'])
def addticket():
    form = Addtickets()
    genre = Genre.query.all()
    # form.genre.choices = [(g.id, g.name) for g in Genre.query.filter_by(id='1').all()]
    if request.method == 'POST' and 'image_1' in request.files:
        name = form.name.data
        price = form.price.data
        date = form.date.data
        discount = form.discount.data
        description = form.description.data
        genre = request.form.get('genre')
        image_1 = photos.save(request.files['image_1'], name=secrets.token_hex(10) + ".")
        status = form.status.data
        showingdates = form.showingdates.data
        ticket = Ticket(name= name,price=price,date=date,discount_price=discount,description=description,image_1=image_1,genre=genre,userr_id='1',pub_date=datetime.utcnow(),genre_id=1,status=status,showingdates=showingdates)
        db.session.add(ticket)
        db.session.commit()
        flash(f'Ticket added successfully','success')
        return redirect(url_for('admins.admin'))
    return render_template('addticket.html',title ="Add Ticket",form=form,genres=genre)



@admins.route('/updateticket/<int:ticket_id>', methods=['GET','POST'])
def updateticket(ticket_id):
    form = Addtickets(request.form)
    ticket = Ticket.query.get_or_404(ticket_id)
    genres = Genre.query.all()
    genre = request.form.get('geenre')

    category = request.form.get('genre')
    if request.method =="POST":
        ticket.name = form.name.data 
        ticket.price = form.price.data
        ticket.discount_price = form.discount.data
        ticket.date = form.date.data 
        ticket.description = form.description.data
        ticket.genre = genre
        ticket.status = form.status.data
        ticket.showingdates = form.showingdates.data
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + ticket.image_1))
                ticket.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                ticket.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")

        flash('The ticket was updated','success')
        db.session.commit()
        return redirect(url_for('admins.admin'))
    form.name.data = ticket.name
    form.price.data = ticket.price
    form.discount.data = ticket.discount_price
    form.date.data = ticket.date
    form.description.data = ticket.description
    genre = ticket.genre
    form.status.data = ticket.status
    form.showingdates.data = ticket.showingdates
    return render_template('addticket.html', form=form, title='Update ticket',getticket=ticket,genres=genres)  

    
    
@admins.route("/<int:ticket_id>/delete_ticket", methods=['POST','GET'])
def delete_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    flash('Post has been deleted')
    return redirect(url_for('admins.admin'))        

    
    
    
    
    
    
    
    
    
    
