from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError, HiddenField,FloatField,IntegerField,SubmitField,SelectField,SelectMultipleField,TextAreaField,FileField,Form,DateTimeField
from flask_wtf import FlaskForm, Form
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField,FileRequired,FileAllowed
from structure.models import User


 


class Addorder(FlaskForm):
    ticket = StringField('Ticket', [validators.DataRequired()])
    quantity = FloatField('Quantity', [validators.DataRequired()])
    date = DateField('Choose Date', [validators.DataRequired()] ,format='%Y-%m-%d')
    time = StringField('Choose Time', [validators.DataRequired()])
    coupon = StringField('Coupon code', [validators.DataRequired()])
    refund_request = BooleanField('Refund Request', default=False)
    genre = SelectField('Genre', choices=[])
    status = SelectField('Status', choices=[('active','Active'),('inactive','Inactive')])
    # status = StringField('Status', default=True)
    showingdates = TextAreaField('Showing Dates and Times', [validators.DataRequired()])


    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    submit = SubmitField('SUBMIT')