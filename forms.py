"""Forms for adopt app."""

from flask_wtf import Flaskform
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional

class AddPetForm(Flaskform):
    """Form for adding pets"""


    name = StringField("pet-name", validators=[InputRequired()])
    species = StringField("pet-species", validators=[InputRequired()])
    photo_url = StringField("photo-url", validators=[InputRequired()])
    age = StringField("pet-age", validators=[InputRequired()])
    notes = TextAreaField("pet-notes", validators=[Optional()])


