# Snow Day Calculator

A website that uses Machine Learning to predict the chance of school closing due to snow.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

* Python 2
* Scikit Learn
* Flask
* Wtforms
* Bootstrap

All Libraries Used

```
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

from sklearn import tree
```

### Installing

Download the repository from Github(https://github.com/vishnu-suresh10/Snow-Day-Calculator). Then open Command Prompt or Shell and navigate to the directory.

```
clone https://github.com/vishnu-suresh10/Snow-Day-Calculator.git

pip install -U -r requirements.txt 
```

Then run the command
```
python main.py
```

## Built With

* [Scikit Learn](http://scikit-learn.org/stable/)
* [Flask](http://flask.pocoo.org/)
* [WTForms](https://wtforms.readthedocs.io/en/stable/)
* [Bootstrap](https://getbootstrap.com/)

## Versioning

We use [SemVer](http://semver.org/) for versioning. We are currently on version 2.0.0

## Authors

* **Vishnu Suresh** - *Created and Developed the the Frontend and Backend* - [Vishnu Suresh](https://github.com/vishnu-suresh10)
