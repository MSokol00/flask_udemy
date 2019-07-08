import os
from forms import AddForm, DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret key'

# SQL DATABASE SECTION#
BASEDIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


# MODELS #


class Puppy(db.Model):
    """"Puppy table"""
    
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        if self.owner:
            return f'Puppy name: {self.name}, owner: {self.owner.name}.'
        else:
            return f'Puppy name: {self.name}, owner: No owner.'


class Owner(db.Model):
    """Owner table"""
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))
    
    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
        

# VIEW FUNCTION #

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    
    form = AddForm()
    
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html', form=form)


@app.route('/list')
def list_pup():
    
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@app.route('/del', methods=['GET','POST'])
def del_pup():
    
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)


@app.route('/addOwner', methods=['GET', 'POST'])
def add_owner():
    form = AddOwnerForm()
    if form.validate_on_submit():
        name = form.name.data
        puppy_id = form.puppy_id.data
        new_owner = Owner(name=name, puppy_id=puppy_id)
        db.session.add(new_owner)
        db.session.commit()
        flash(f'You just added owner: {new_owner.name}')
        return redirect(url_for('add_owner'))
    return render_template('addOwner.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
