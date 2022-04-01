"""Forms for adopt app."""

from tkinter.tix import Select
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    """Form for adding pets"""


    name = StringField("pet-name", validators=[InputRequired()])
    species = SelectField("pet-species", choices=[("cat","Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")], validators=[InputRequired()])
    photo_url = StringField("photo-url", validators=[ URL()])
    age = SelectField("pet-age", choices=[("baby", "Baby"), ("young", "Young"), ("adult", "Adult"), ("senior", "Senior") ], validators=[InputRequired()])
    notes = TextAreaField("pet-notes", validators=[Optional()])


