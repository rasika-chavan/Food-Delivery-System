from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from fooddelivery.dbmodel import User


class RegistrationForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    contactno = IntegerField('Contact Number')
    addr1 = StringField('Address Line 1', validators=[Length(min=1, max=50)])
    addr2 = StringField('Address Line 2', validators=[Length(max=50)])
    addr3 = StringField('Address Line 3', validators=[Length(max=50)])
    pincode = IntegerField('Pincode')
    city = StringField('City', validators=[Length(max=50)])
    state = StringField('State', validators=[Length(max=50)])
    country = StringField('Country', validators=[Length(max=50)])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class QuantityForm(FlaskForm):
    quantity = IntegerField('Quantity', validators=[DataRequired()], default=1)
    buy = SubmitField('Order Now')
    add = SubmitField('Add to Cart')

class PaymentDetails(FlaskForm):
    upiid = StringField('UPI ID', validators=[DataRequired(), Email()])
    upipin = PasswordField('UPI Pin', validators=[DataRequired()])#, NumberRange(min=0, max=9999)])
    contactno = IntegerField('Contact Number', validators=[DataRequired()])
    addr1 = StringField('Address Line 1', validators=[DataRequired(), Length(min=1, max=50)])
    addr2 = StringField('Address Line 2', validators=[Length(max=50)])
    addr3 = StringField('Address Line 3', validators=[Length(max=50)])
    pincode = IntegerField('Pincode', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired(), Length(max=50)])
    state = StringField('State', validators=[DataRequired(), Length(max=50)])
    country = StringField('Country', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Confirm Details')

class SearchForm(FlaskForm):
    search = StringField('Search for a product', validators=[DataRequired()])

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class ReviewForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Add review')