from flask import render_template,request,Blueprint,redirect,url_for,flash,jsonify,Blueprint,current_app
from  structure import app,db,login_manager,photos
import string,random
import json
import requests
# from structure.models import User,About,Price, WebFeature,Faq,Testimonial,Team,Appearance,Block
# # from structure.team.views import team
# from structure.web_features.forms import WebFeatureForm
# from structure.team.forms import UpdateTeamForm
# from structure.about.forms import UpdateAboutForm
# from structure.faq.forms import FaqForm
# from structure.pricing.forms import PriceForm
# from structure.testimonial.forms import TestimonialForm
# from structure.about.forms import AboutForm
# from structure.block.forms import BlockForm
# from sqlalchemy.orm import load_only
from sqlalchemy import desc
from flask_login import login_required
# from structure.appearance.forms import AppearanceForm
# from structure.block.forms import BlockForm
# from structure.appearance.views import appearance
from structure.models import Ticket,Genre,OrderItem, Couponn
from structure.core.forms import Addorder
core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''
    req = requests.get('https://cat-fact.herokuapp.com/facts')
    data = json.loads(req.content)
    form = Addorder()
    page = request.args.get('page', 1, type=int)
    newtickets = Ticket.query.order_by(desc(Ticket.pub_date)).limit(3).all()
    tickets = Ticket.query.order_by(desc(Ticket.pub_date)).all()
    # posts = Post.query.order_by(desc(post.date)).limit(3).all()
 
    return render_template('main.html',title='Home',tickets=tickets,page=page,newtickets=newtickets,form=form,data=data)


# @core.route('/order')
# def order():
#     # use orderitem model to create new orderitems
#     # orderitems = OrderItem.query.all()




@core.route('/addorder/<int:ticket_id>', methods=['GET','POST'])
def addorder(ticket_id):
    form = Addorder()
    order = OrderItem.query.all()
    genre = Genre.query.all()
    ticket = Ticket.query.all()
    tid = ticket_id
    theticket = Ticket.query.get(tid)
    ticketprice = theticket.price
    ref_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))
    # form.genre.choices = [(g.id, g.name) for g in Genre.query.filter_by(id='1').all()]
    if request.method == 'POST':
        quantity = form.quantity.data
        date = form.date.data
        time = form.time.data
        coupon = form.coupon.data
        # coup = Couponn.query.filter_by(code=coupon).first()
        coupondb = Couponn.query.filter_by(code=coupon).first()
        if coupondb and coupondb.status == 'active':
            coupon_price = coupondb.amount
            total =  (int(ticketprice) * int(form.quantity.data) - int(coupon_price))
            

            order = OrderItem(ticket_id=ticket_id,quantity=quantity,date=date,time=time,coupon=coupon,ref_code=ref_code,totalprice=total)
            db.session.add(order)
            db.session.commit()
            flash(f'Ticket added successfully','success')
            return redirect(url_for('core.index'))
        else:
            flash(f'Coupon is not active','danger')
            print('coupon is not active')
    return render_template('order.html',title ="Add Ticket",form=form,genres=genre,tid=tid,tickets = ticket)



@core.route('/updateorder/<int:ticket_id>/<int:order_id>', methods=['GET','POST'])
def updateorder(ticket_id,order_id):
    form = Addorder()
    order = OrderItem.query.filter_by(id=order_id).first() 
    genres = Genre.query.all()
    ticketprice = order.ticket.price

    category = request.form.get('genre')
    if request.method =="POST":
        order.quantity = form.quantity.data
        order.date = form.date.data
        order.time = form.time.data
        order.coupon = form.coupon.data
        order.refund_requested = form.refund_request.data
        order.refund_reason = form.refund_reason.data
        order.refund_granted = 'no'
        # total =  (int(ticket.price) * int(form.quantity.data))
        # order.totalprice = total

        flash('The ticket was updated','success')
        db.session.commit()
        return redirect(url_for('core.index'))
    
    form.ticket.data = order.ticket
    form.quantity.data = order.quantity
    form.date.data = order.date
    form.time.data = order.time
    form.coupon.data = order.coupon
    form.refund_request.data = order.refund_requested   
    form.refund_reason.data = order.refund_reason
  
    return render_template('updateorder.html', form=form, title='Update order',getorder=order,genres=genres)

 # <a href="{{ url_for('admins.updateticket',ticket_id=ticket.id,order_id=order.id )}}" class="btn btn-primary">Edit Feature</a> 


#add route to take coupon code and check if it is valid
@core.route('/checkcoupon/', methods=['GET','POST'])
def checkcoupon():
    form = Addorder()
    
    if request.method =="POST":
        ref_codee = form.ref_code.data
        order = OrderItem.query.filter_by(ref_code=ref_codee).first()
        if order.ref_code:
            ref_id = order.id
            ticket_id = order.ticket_id
            return redirect(url_for('core.updateorder',ticket_id=ticket_id,order_id=ref_id))
        else:
            flash('Invalid coupon','danger')
            return redirect(url_for('core.index'))
    # return render_template('order.html', form=form, title='Update order',getorder=order)

# route to approve refund
@core.route('/approverefund/<int:order_id>', methods=['GET','POST'])
def approverefund(order_id):
    form = Addorder()
    order = OrderItem.query.filter_by(id=order_id).first()
    if request.method =="POST":
        order.refund_granted = form.approve_refund.data
        order.handled = 'yes'
  
        flash('The refund was approved','success')
        db.session.commit()
        return redirect(url_for('admins.admin'))
    form.approve_refund.data = order.refund_granted
    return render_template('index.html', form=form, title='Approve refund',getorder=order)


# @app.route(, methods=['GET'])
# def index():
#        requests.get('https://cat-fact.herokuapp.com/facts')
#         json. loads ( req.content)
#      return render_template('index.html', data=data)
#   req 
#  data

#function to add calculate total price

# def totalprice(order_id):
#     order = OrderItem.query.filter_by(id=order_id).first()
#     ticket = order.ticket
#     quantity = order.quantity
#     price = ticket.price
#     total = price * quantity
#     return total