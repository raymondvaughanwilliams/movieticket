import email
from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError, HiddenField,FloatField,IntegerField,SubmitField,SelectField,SelectMultipleField,TextAreaField,FileField,Form,DateTimeField
from flask_wtf import FlaskForm, Form
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField,FileRequired,FileAllowed
from structure.models import User

class RegistrationForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    group = HiddenField('Email Address',default='customer')
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

        
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
            


class LoginForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [validators.DataRequired()])
 


class Addtickets(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = FloatField('Price', [validators.DataRequired()])
    date = DateField('Date', [validators.DataRequired()] ,format='%Y-%m-%d')
    discount = IntegerField('Discount', default=0)
    description = TextAreaField('Discription', [validators.DataRequired()])
    genre = SelectField('Genre', choices=[])
    status = SelectField('Status', choices=[('active','Active'),('inactive','Inactive')])
    # status = StringField('Status', default=True)
    showingdates = TextAreaField('Showing Dates and Times', [validators.DataRequired()])
    display = SelectField('Display', choices=[('yes','Yes'),('no','No')])   


    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    submit = SubmitField('SUBMIT')


class Addcoupon(Form):
    code = StringField('Code', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    status = SelectField('Status', choices=[('active','Active'),('inactive','Inactive')])
    submit = SubmitField('SUBMIT')
    # status = StringField('Status', default=True)
    # showingdates =

class ProcessForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    email = StringField('Email Address', [validators.DataRequired()])
    submit = SubmitField('SUBMIT')
