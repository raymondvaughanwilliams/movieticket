from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError, HiddenField,FloatField,IntegerField,SubmitField,SelectField,SelectMultipleField,TextAreaField,FileField,Form,DateTimeField
from flask_wtf import FlaskForm, Form
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField,FileRequired,FileAllowed
from structure.models import User


 


class Addorder(FlaskForm):
    ticket = StringField('Ticket', [validators.DataRequired()])
    quantity = FloatField('Quantity', [validators.DataRequired()])
    date = DateField('Choose Date', [validators.DataRequired()] ,format='%Y-%m-%d')
    time = SelectField('Choose Time', choices=[('2pm','2pm'),('4pm','4pm'),('6pm','6pm'),('8pm','8pm'),('10pm','10pm')])
    coupon = StringField('Coupon code')
    # refund_request = BooleanField('Request Refund', default=False)
    refund_request = SelectField('Request Refund', choices=[('no','No'),('yes','Yes')])
    refund_reason = TextAreaField('Refund Reason')
    approve_refund = SelectField('Approve Refund', choices=[('no','No'),('yes','Yes')])
    genre = SelectField('Genre', choices=[('active','Active'),('inactive','Inactive')])
    status = SelectField('Status', choices=[('active','Active'),('inactive','Inactive')])
    ref_code = StringField('Referal Code', [validators.DataRequired()])
    # status = StringField('Status', default=True)
    showingdates = TextAreaField('Showing Dates and Times', [validators.DataRequired()])


    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    submit = SubmitField('SUBMIT')