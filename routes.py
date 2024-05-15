from flask import Flask, render_template, request
from app import obj
from flask import flash
from app.forms import SeatForm, PayForm
from app.models import User, Post
from flask import redirect
from app import db


#to redirect to a different pg after submitting
#different URL the app will implement
@obj.route("/")
def hello():
    return "Hello Mel, you made it to the homepage"

@obj.route("/seats", methods=["GET", "POST"])
def seating():
    current_form = SeatForm()
    if current_form.validate_on_submit():
        flash(f"Your total is $50 for seat {current_form.seat.data}")

        #the three commands that add to database, with help of models.py
        u = User(seat=current_form.seat.data)
        db.session.add(u)
        db.session.commit()

        return redirect('/payment')
    return render_template('seats.html', form=current_form)

#############################################################################################

@obj.route("/payment", methods=["GET", "POST"])
def paying():
    current_form = PayForm()

    p = Post(id=current_form.card_number.data, exp_year='', cvv='')
    db.session.add(p)
    db.session.commit()

    if current_form.validate_on_submit():
        flash(f"Purchase Confirmed {current_form}")

        return redirect('/')
    return render_template('payment.html', form=current_form)
