from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import statistics
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

db = SQLAlchemy(app)


class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    gender = db.Column(db.Integer)
    age = db.Column(db.Integer)
    education = db.Column(db.Integer)
    location = db.Column(db.Integer)
    voting = db.Column(db.Integer)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)
    q6 = db.Column(db.Integer)
    q7 = db.Column(db.Integer)
    q8 = db.Column(db.Integer)
    q9 = db.Column(db.Integer)
    q10 = db.Column(db.Integer)
    q11 = db.Column(db.Integer)
    q12 = db.Column(db.Integer)
    q13 = db.Column(db.Integer)
    q14 = db.Column(db.String(120))

    def __init__(self, gender, age, education, location, voting, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12,
                 q13, q14):
        self.gender = gender
        self.age = age
        self.education = education
        self.location = location
        self.voting = voting
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10
        self.q11 = q11
        self.q12 = q12
        self.q13 = q13
        self.q14 = q14


db.create_all()


@app.route("/")
def welcome():
    return render_template('welcome.html')


@app.route("/team")
def show_team():
    return render_template('team.html')


@app.route("/form")
def show_form():
    return render_template('form.html')


@app.route("/raw")
def show_raw():
    fd = db.session.query(Formdata).all()
    return render_template('raw.html', formdata=fd)


@app.route("/result")
def show_result():
    fd_list = db.session.query(Formdata).all()

    qu1 = {"answers": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}}
    qu2 = {"answers": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}}
    qu3 = {"answers": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}}
    qu4 = {"answers": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}}
    qu5 = {"answers": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}}
    qu6 = {"answers": {"1": 0, "2": 0, "3": 0, "4": 0}}
    qu7 = {"answers": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}}
    qu8 = {"answers": {"1": 0, "2": 0, "3": 0, "4": 0}}
    qu9 = {"answers": {"1": 0, "2": 0, "3": 0, "4": 0}}
    qu10 = {"answers": {"1": 0, "2": 0, "3": 0, "4": 0}}
    qu11 = {"answers": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}}
    qu12 = {"answers": {"1": 0, "2": 0, "3": 0, "4": 0}}
    qu13 = {"answers": {"1": 0, "2": 0, "3": 0, "4": 0}}
    qu14 = {"answers": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0}}

    for row in fd_list:
        qu1["answers"][str(row.q1)] += 1
        qu2["answers"][str(row.q2)] += 1
        qu3["answers"][str(row.q3)] += 1
        qu4["answers"][str(row.q4)] += 1
        qu5["answers"][str(row.q5)] += 1
        qu6["answers"][str(row.q6)] += 1
        qu7["answers"][str(row.q7)] += 1
        qu8["answers"][str(row.q8)] += 1
        qu9["answers"][str(row.q9)] += 1
        qu10["answers"][str(row.q10)] += 1
        qu11["answers"][str(row.q11)] += 1
        qu12["answers"][str(row.q12)] += 1
        qu13["answers"][str(row.q13)] += 1
        
        # Multiple answers for q14
        answersList = row.q14.split(',')
        for answ in answersList:
            qu14["answers"][str(answ)] += 1

    allQus = [qu1, qu2, qu3, qu4, qu5, qu6, qu7, qu8, qu9, qu10, qu11, qu12, qu13, qu14]
    allRows = []
    
    for qu in allQus:
        temp = []
        for key, answer in qu["answers"].items():
            temp.append([key, answer])
        allRows.append(temp)

    print(allRows)

    return render_template('result.html', allQus = allQus, allRows=allRows)


@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    gender = request.form['gender']
    age = request.form['age']
    education = request.form['education']
    location = request.form['location']
    voting = request.form['voting']
    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']
    q4 = request.form['q4']
    q5 = request.form['q5']
    q6 = request.form['q6']
    q7 = request.form['q7']
    q8 = request.form['q8']
    q9 = request.form['q9']
    q10 = request.form['q10']
    q11 = request.form['q11']
    q12 = request.form['q12']
    q13 = request.form['q13']
    q14 = ",".join(request.form.getlist('q14'))
    # Save the data
    fd = Formdata(gender, age, education, location, voting, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14)
    db.session.add(fd)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    app.debug = True
    app.run()
