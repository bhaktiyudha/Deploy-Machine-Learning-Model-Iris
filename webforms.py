import requests
import json 
from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

class ReusableForm(Form):
    sepallength = TextField('sepallength:', validators=[validators.required()])
    sepalwidth = TextField('sepalwidth:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    #print(form.errors)
    if request.method == 'POST':
        sepallength=request.form['sepallength']
        sepalwidth=request.form['sepalwidth']
        petallength=request.form['petallength']
        petalwidth=request.form['petalwidth']

        if form.validate():
            url = 'http://localhost:5000/apiIris'
            result = requests.post(url,json={'iris':[float(sepallength),float(sepalwidth),float(petallength),float(petalwidth)]})
            response = str(result.json().get('result'))
            flash('{}'.format(response))

        else:
            flash('Error: All Fields are Required')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(port=5001)