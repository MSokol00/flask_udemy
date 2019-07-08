from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    
    name = StringField('Name of the puppy: ')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id = IntegerField("Id Number of Puppy to remove")
    submit = SubmitField('Remove Puppy')


class AddOwnerForm(FlaskForm):

    name = StringField('Name of owner:')
    puppy_id = IntegerField('Id of puppy:')
    submit = SubmitField('Add Owner')
