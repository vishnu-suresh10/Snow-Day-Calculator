from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

from sklearn import tree

from tinydb import TinyDB,Query

db = TinyDB('db.json')
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# Inches, Days Cancelled
X = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],
    [1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],
    [2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],
    [3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],
    [10,0],[10,1],[10,2],[10,3],[10,4],[10,5],[10,100],[10,115],[8,2]]

# Outputs
Y = ['School','School','School','School','School','School','School','School',
    'School','School','School','School','School','School','School','School',
    'School','School','School','School','School','School','School','School',
    'School','School','School','School','School','School','School','School',
    'No School','No School','No School','No School','No School','No School','School','School','No School']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

def checkValueOfInteger(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def formatResults(val):
    if val.find('No'):
        print('NO')
        return 'No School'
    else:
        print('Yes')
        return 'School'

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Inches of Snow:', validators=[validators.required()])
    daysOfNoSchool = TextField('Days of No School:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    # print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        daysOfNoSchool=request.form['daysOfNoSchool']
        # print name

        if form.validate():
            # Save the comment here.
            isValidInch = checkValueOfInteger(name)
            isValidDays = checkValueOfInteger(daysOfNoSchool)

            if isValidInch and isValidDays:
                prediction = clf.predict([[name,daysOfNoSchool]])
                predictionToString = str(prediction)
                formatedPrediction = formatResults(predictionToString)

                flash('There will be ' + formatedPrediction)

                db.insert({'Inches':name, 'Days of No School':daysOfNoSchool})

            else:
                retVal = 'Invalid Values entered'
                flash(retVal)
        else:
            flash('Please Enter a Valid Amount')

    return render_template('form.html', form=form)

if __name__ == "__main__":
    app.run()
