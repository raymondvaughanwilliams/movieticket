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

    # def get_add_to_cart_url(self):
    #     return reverse("core:add-to-cart", kwargs={
    #         'slug': self.slug
    #     })

    # def get_remove_from_cart_url(self):
    #     return reverse("core:remove-from-cart", kwargs={
    #         'slug': self.slug
    #                 })


    def __repr__(self):
        return f"Username {self.username}"

# GENRE_CHOICES = (
#     ('S', 'Shirt'),
#     ('SW', 'Sport wear'),
#     ('OW', 'Outwear')
# )
class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Brand %r>' % self.name



class Ticket(db.Model):
    __tablename__ = 'tickets'
    __seachbale__ = ['name','description']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=True)
    description = db.Column(db.String(255), nullable= True)
    price = db.Column(db.Float, nullable=False)
    discount_price = db.Column(db.Float, nullable=True)
    status = db.Column(db.Text, default='True')
    showingdates = db.Column(db.String(255), nullable=True)


    genre = db.Column(db.String(255), nullable= True)

    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'),nullable=False)
    # genree = db.relationship('Genre',backref=db.backref('genres', lazy=True))

    # category = db.relationship('Category',backref=db.backref('category', lazy=True))

    userr_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    # orders = db.relationship('OrderItem', backref='ticket', lazy=True)
    # userr = db.relationship('User',backref=db.backref('users', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')


    def __repr__(self):
        return '<Addproduct %r>' % self.name
    
    
# admin.add_view(ModelView(Report,db.session))



# class Item(models.Model):
#     title = models.CharField(max_length=100)
#     price = models.FloatField()
#     discount_price = models.FloatField(blank=True, null=True)
#     category = models.CharField(choices=GENRE_CHOICES, max_length=2)
#     label = models.CharField(choices=LABEL_CHOICES, max_length=1)
#     slug = models.SlugField()
#     description = models.TextField()
#     image = models.ImageField()

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse("core:product", kwargs={
#             'slug': self.slug
#         })

#     def get_add_to_cart_url(self):
#         return reverse("core:add-to-cart", kwargs={
#             'slug': self.slug
#         })

#     def get_remove_from_cart_url(self):
#         return reverse("core:remove-from-cart", kwargs={
#             'slug': self.slug
#         })


class OrderItem(db.Model):
    __tablename__ = 'order_items'

    # ordered = models.BooleanField(default=False)
    id = db.Column(db.Integer, primary_key=True)
    ticket = db.Column(db.Integer, db.ForeignKey('tickets.id'),nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(255), nullable= True)
    coupon = db.Column(db.Integer, db.ForeignKey('coupons.id'),nullable=True)    
    refund_requested = db.Column(db.String, nullable=True, default=False)
    refund_reason = db.Column(db.Text, nullable=True)
    refund_granted = db.Column(db.String, nullable=True, default=False)
    ref_code = db.Column(db.String(20), nullable=True)
    totalprice = db.Column(db.Float, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    tickets = db.relationship('Ticket',backref=db.backref('tickets', lazy=True))



    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.ticket.price

    def get_total_discount_item_price(self):
        return self.quantity * self.coupon.amount

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_ref_code(self):
        return self.ref_code

    # def get_final_price(self):
    #     if self.item.discount_price:
    #         return self.get_total_discount_item_price()
    #     return self.get_total_item_price()


# class Order(db.Model):
#     __tablename__ = 'orders'
#     # user = models.ForeignKey(settings.AUTH_USER_MODEL,
#     #                          on_delete=models.CASCADE)
#     ref_code = db.Column(db.String(20), nullable=True)
#     # ticket = db.ManyToManyField(OrderItem)
#     ordertickets = db.Column(db.Integer, db.ForeignKey('order_items.id'),nullable=False)
#     # date = db.DateTimeField()
#     date = db.Column(db.DateTime, nullable=False)
#     time = db.Column(db.String(255), nullable= True)

#     # ordered = models.BooleanField(default=False)
#     # shipping_address = models.ForeignKey(
#     #     'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
#     # billing_address = models.ForeignKey(
#     #     'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
#     # payment = models.ForeignKey(
#     #     'Payment', on_delete=models.SET_NULL, blank=True, null=True)
#     # coupon = db.ForeignKey(
#     #     'Coupon', on_delete=db.SET_NULL, blank=True, null=True)
#     coupon = db.Column(db.Integer, db.ForeignKey('coupons.id'),nullable=True)    
#     # received = db.BooleanField(default=False)
#     received = db.Column(db.Boolean, nullable=False, default=False)
#     # refund_requested = db.BooleanField(default=False)
#     refund_requested = db.Column(db.Boolean, nullable=False, default=False)
#     # refund_granted = db.BooleanField(default=False)
#     refund_granted = db.Column(db.Boolean, nullable=False, default=False)

#     '''
#     1. Item added to cart
#     2. Adding a billing address
#     (Failed checkout)
#     3. Payment
#     (Preprocessing, processing, packaging etc.)
#     4. Being delivered
#     5. Received
#     6. Refunds
#     '''

#     def __str__(self):
#         return self.user.username

#     def get_total(self):
#         total = 0
#         for order_item in self.items.all():
#             total += order_item.get_final_price()
#         if self.coupon:
#             total -= self.coupon.amount
#         return total



class Coupon(db.Model):
    __tablename__ = 'coupons'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(15), nullable=False, primary_key=True)
    amount = db.Column(db.Float, nullable=False)

    def __str__(self):
        return self.code

# class Refund(db.Model):
#     # order = db.ForeignKey(Order, on_delete=db.CASCADE)
#     order = db.Column(db.Integer, db.ForeignKey('order_items.id'),nullable=False)
#     # reason = db.TextField()
#     reason = db.Column(db.String(255), nullable=False)
#     # accepted = db.BooleanField(default=False)
#     accepted = db.Column(db.Boolean, nullable=False, default=False)
#     # email = db.EmailField()
#     email = db.Column(db.String(255), nullable=False)


#     def __str__(self):
#         return f"{self.pk}"

# class Cart(db.Model):
#     __table_args__ = {'extend_existing': True}
#     ticketid = db.Column(db.Integer, db.ForeignKey('product.productid'), nullable=False, primary_key=True)
#     quantity = db.Column(db.Integer, nullable=False)
#     couponid = db.Column(db.Integer, db.ForeignKey('coupons.id'),nullable=True)

#     def __repr__(self):
#         return f"Cart('{self.userid}', '{self.productid}, '{self.quantity}')"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
