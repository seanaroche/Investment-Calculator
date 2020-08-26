from flask import render_template, flash, redirect, request
from app import app
from app.forms import Login


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Home")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        flash('Login requested for user {}')
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/calculator', methods=['GET', 'POST'])
def calculator(investment=None):
    if request.method == 'POST':
        years = request.form['years']
        initial = request.form['initial']
        roi = request.form['roi']
        contribution = request.form['contribution']
        investment = 0
        for i in range(int(years)):
            if i == 0:
                investment = int(initial)
            investment += int(contribution)
            investment = investment + investment * int(roi) * .01
        investment = round(investment, 2)
    return render_template("calculator.html", investment=investment)
