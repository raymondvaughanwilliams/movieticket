from flask import render_template,request,Blueprint,redirect,url_for,flash,jsonify,Blueprint,current_app
from  structure import app,db,login_manager,photos

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
from structure.models import Ticket,Genre,OrderItem
from structure.core.forms import Addorder
core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''
    page = request.args.get('page', 1, type=int)
    newtickets = Ticket.query.order_by(desc(Ticket.pub_date)).limit(3).all()
    tickets = Ticket.query.order_by(desc(Ticket.pub_date)).all()
    # posts = Post.query.order_by(desc(post.date)).limit(3).all()
 
    return render_template('main.html',title='Home',tickets=tickets,page=page,newtickets=newtickets)


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
    # form.genre.choices = [(g.id, g.name) for g in Genre.query.filter_by(id='1').all()]
    if request.method == 'POST':
        quantity = form.quantity.data
        date = form.date.data
        time = form.time.data
        coupon = form.coupon.data
        order = OrderItem(ticket=ticket_id,quantity=quantity,date=date,time=time,coupon=coupon)
        db.session.add(order)
        db.session.commit()
        flash(f'Ticket added successfully','success')
        return redirect(url_for('admins.admin'))
    return render_template('order.html',title ="Add Ticket",form=form,genres=genre,tid=tid,tickets = ticket)



@core.route('/updateorder/<int:order_id>/<int:ticket_id>', methods=['GET','POST'])
def updateorder(order_id,ticket_id):
    form = OrderItem()
    order = OrderItem.query.get_or_404(order_id)
    genres = Genre.query.all()
    tid = ticket_id

    category = request.form.get('genre')
    if request.method =="POST":
        order.ticket = form.ticket.data 
        order.quantity = form.quantity.data
        order.date = form.date.data
        order.time = form.time.data
        order.coupon = form.coupon.data
        flash('The ticket was updated','success')
        db.session.commit()
        return redirect(url_for('admins.admin'))
    form.ticket.data = order.ticket
    form.quantity = order.quantity
    form.date = order.date
    form.time = order.time
    form.coupon = order.coupon
    return render_template('order.html', form=form, title='Update order',getorder=order,genres=genres,tid=tid)

 # <a href="{{ url_for('admins.updateticket',ticket_id=ticket.id,order_id=order.id )}}" class="btn btn-primary">Edit Feature</a> 


