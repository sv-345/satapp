from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, current_user
from . import db
from .models import Problem
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    showex = False
    current_problem = Problem.query.all()
    if request.method == 'POST':
        choice = int(request.form.get('options')) 
        print(choice)
        correct = db.session.query(Problem).first()
        print(correct.answer)
        if choice == correct.answer:
            flash("You are correct!", category='success')    
            return render_template('home.html', current_problem=current_problem, showex=True)
        else:
            flash("Try again!", category='error')
   
    return render_template('home.html', current_problem=current_problem, showex=False)
    

@views.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    if request.method == 'POST':
        db.session.query(Problem).delete()

        pdf = request.form.get('pdf')
        question = request.form.get('question')
        option1 = request.form.get('option1')
        option2 = request.form.get('option2')
        option3 = request.form.get('option3')
        option4 = request.form.get('option4')
        answer = request.form.get('answer')
        iexplanation = request.form.get('iexplanation')
        new_problem = Problem(question=question, option1=option1, option2=option2, option3=option3, option4=option4, answer=answer, iexplanation=iexplanation, pdf=pdf)
        db.session.add(new_problem)
        db.session.commit()
        flash("Problem updated!", category='success')
    return render_template('edit.html')

