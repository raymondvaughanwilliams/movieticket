from flask import render_template,session, request,redirect,url_for,flash,jsonify,Blueprint
from  structure import app,db,login_manager,photos
from .forms import RegistrationForm,LoginForm,Addtickets
from structure.models import User
from flask_admin.contrib.sqla import ModelView
from structure.models import Ticket,Genre
import secrets
from datetime import datetime




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
        ticket = Ticket(name= name,price=price,date=date,discount_price=discount,description=description,image_1=image_1,genre=genre,userr_id='1',pub_date=datetime.utcnow(),genre_id=1)
        db.session.add(ticket)
        db.session.commit()
        flash(f'Ticket added successfully','success')
        return redirect(url_for('admins.admin'))
    return render_template('addticket.html',title ="Add Ticket",form=form,genres=genre)
#     form = Addproducts(request.form)
#     brands = Brand.query.all()
#     categories = Category.query.all()
#     if request.method=="POST"and 'image_1' in request.files:
#         name = form.name.data
#         price = form.price.data
#         discount = form.discount.data
#         stock = form.stock.data
#         colors = form.colors.data
#         desc = form.discription.data
#         brand = request.form.get('brand')
#         category = request.form.get('category')
#         image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
#         image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
#         image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
#         addproduct = Addproduct(name=name,price=price,discount=discount,stock=stock,colors=colors,desc=desc,category_id=category,brand_id=brand,image_1=image_1,image_2=image_2,image_3=image_3)
#         db.session.add(addproduct)
#         flash(f'The product {name} was added in database','success')
#         db.session.commit()
#         return redirect(url_for('admin'))
#     return render_template('products/addproduct.html', form=form, title='Add a Product', brands=brands,categories=categories)


# @app.route('/updateproduct/<int:id>', methods=['GET','POST'])
# def updateproduct(id):
#     form = Addproducts(request.form)
#     product = Addproduct.query.get_or_404(id)
#     brands = Brand.query.all()
#     categories = Category.query.all()
#     brand = request.form.get('brand')
#     category = request.form.get('category')
#     if request.method =="POST":
#         product.name = form.name.data 
#         product.price = form.price.data
#         product.discount = form.discount.data
#         product.stock = form.stock.data 
#         product.colors = form.colors.data
#         product.desc = form.discription.data
#         product.category_id = category
#         product.brand_id = brand
#         if request.files.get('image_1'):
#             try:
#                 os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
#                 product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
#             except:
#                 product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
#         if request.files.get('image_2'):
#             try:
#                 os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
#                 product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
#             except:
#                 product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
#         if request.files.get('image_3'):
#             try:
#                 os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
#                 product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
#             except:
#                 product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

#         flash('The product was updated','success')
#         db.session.commit()
#         return redirect(url_for('admin'))
#     form.name.data = product.name
#     form.price.data = product.price
#     form.discount.data = product.discount
#     form.stock.data = product.stock
#     form.colors.data = product.colors
#     form.discription.data = product.desc
#     brand = product.brand.name
#     category = product.category.name
#     return render_template('products/addproduct.html', form=form, title='Update Product',getproduct=product, brands=brands,categories=categories)  

    
    
    
    
    
    
    
    
    
    
    
    
    #if form.validate_on_submit():
    #     hash_password = bcrypt.generate_password_hash(form.password.data)
    #     user = User(name=form.name.data,username=form.username.data, email=form.email.data,
    #                 password=hash_password)
    #     db.session.add(user)
    #     flash(f'welcome {form.name.data} Thanks for registering','success')
    #     db.session.commit()
    #     return redirect(url_for('login'))
    # return render_template('admin/register.html',title='Register user', form=form# )