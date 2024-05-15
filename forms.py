from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class SeatForm(FlaskForm):
    seat = StringField("Pick A Seat (EX. 14A)", validators=[DataRequired()])
    submit = SubmitField("Submit")


class PayForm(FlaskForm):
    total = StringField("Tip")
    #seat = StringField("Seat Number", validators=[DataRequired()])
    card_number = StringField("Enter Card Number: ", validators=[DataRequired()])
    exp_yr = StringField("Expiration Year: ", validators=[DataRequired()])
    cvv = StringField("CVV: ", validators=[DataRequired()])
    submit = SubmitField("Confirm Payment")
