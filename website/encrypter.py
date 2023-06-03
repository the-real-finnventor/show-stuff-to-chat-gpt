"""from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
"""

from cryptography.fernet import Fernet
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import User


encrypter = Blueprint('encrypter', __name__)


@encrypter.route('/encrypt', methods=['GET', 'POST'])
@login_required
def encrypt():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        text = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                key = user.encryption_key
                encrypted_password = Fernet(key).encrypt(password)
                flash(
                    f'Password Encrypted! Your encrypted password is {encrypted_password}', category='success')
            else:
                flash('Incorrect Password', category='error')
        else:
            flash("I'm sorry. I don't recognize that email address.",
                  category='error')

    return render_template("encrypt.html", user=current_user)
