"""Flask app for adopt app."""

from ast import Add
from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://davidjeffers:1234@localhost:5432/adopt" # added davidjeffers:1234@localhost:5432
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get("/")
def homepage():
    """lists pets"""
    pets = Pet.query.all()
    return render_template("homepage.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def show_pet_form():
    """Display new pet form or submit pet form"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f'{name} added')
        return redirect('/add')

    else:
        return render_template('pet_form.html', form=form)

