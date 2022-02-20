from flask import render_template,session, request,redirect,url_for,flash,jsonify,Blueprint,current_app
# from movieticket.structure.models import TicketSchema,MovieTicket
from  structure import app,db,login_manager,photos
from .forms import RegistrationForm,LoginForm,Addtickets
from structure.models import User
from flask_admin.contrib.sqla import ModelView
from structure.models import Ticket,Genre,OrderItem,TicketSchema,Couponn
import secrets
from datetime import datetime
import os
from structure.core.forms import Addorder
from structure.admin.forms import Addcoupon





admins = Blueprint('admins',__name__)

@admins.route('/home')
def admin():
#     if 'email' not in session:
#         flash(f'Please Login','danger')
#         return redirect(url_for('admins.login'))
    # products = Addproduct.query.all()
    ROWS_PER_PAGE = 3
    page = request.args.get('page', 1, type=int)
    genre = Genre.query.paginate(page, ROWS_PER_PAGE, False)
    tickets = Ticket.query.paginate(page, ROWS_PER_PAGE, False)
    coupon = Couponn.query.paginate(page, ROWS_PER_PAGE, False)
    form = Addorder()

    refund_orders = OrderItem.query.filter_by(refund_requested='yes').all()
    return render_template('index.html',title ="Admin Page",tickets=tickets,orders=refund_orders,form=form,coupon=coupon,genre=genre)




@admins.route('/tickets')
def tickets():
    tickets = Ticket.query.all()
    results = TicketSchema(many=True)
    output = results.dump(tickets)
    return jsonify(output)


    
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

@admins.route('/addticketapi', methods=['GET','POST'])
def addticketapi():
    form = Addtickets()
    genre = Genre.query.all()
    # form.genre.choices = [(g.id, g.name) for g in Genre.query.filter_by(id='1').all()]
    name = request.json['name']
    price = request.json['price']
    date = request.json['date'] 
    discount = request.json['discount']
    description = request.json['description']
    genre = request.json['genre']
    image_1 = photos.save(request.files['image_1'], name=secrets.token_hex(10) + ".")
    status = request.json['status']
    showingdates = request.json['showingdates']

    ticket = Ticket(name= name,price=price,date=date,discount_price=discount,description=description,image_1=image_1,genre=genre,userr_id='1',pub_date=datetime.utcnow(),genre_id=1,status=status,showingdates=showingdates)
    db.session.add(ticket)
    db.session.commit()
    return TicketSchema.jsonify(ticket)

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

    
    
@admins.route('/addcoupon', methods=['GET','POST'])
def addcoupon():
    form = Addcoupon()
    if request.method == 'POST':
        name = form.code.data
        price = form.discount.data
        print(name)
        print(id)
        coupon = Couponn(code=name,amount=price)
        # print(coupon)
        db.session.add(coupon)
        db.session.commit()
        flash(f'Coupon added successfully','success')
        return redirect(url_for('admins.admin'))
    return render_template('addcoupon.html',form=form)
    
    
    
@admins.route('/updatecoupon/<int:coupon_id>', methods=['GET','POST'])
def updatecoupon(coupon_id):
    form = Addcoupon(request.form)
    coupon = Couponn.query.get_or_404(coupon_id)


    if request.method =="POST":
        coupon.code = form.code.data 
        coupon.amount = form.discount.data
        coupon.status = form.status.data

        flash('The ticket was updated','success')
        db.session.commit()
        return redirect(url_for('admins.admin'))
    form.code.data = coupon.code
    form.discount.data = coupon.amount
    form.status.data = coupon.status
    return render_template('addcoupon.html', form=form)  
    
    
    
@admins.route('/process', methods=['POST'])
def process():
            
    email = request.form['email']
    name = request.form['name']
    print(email)
    print(name)
    if name and email:
        # newName = name[::-1]
        # return jsonify({'name' : newName})
        print(email)
    else:
        print('error')

    return jsonify({'error' : 'Missing data!'})