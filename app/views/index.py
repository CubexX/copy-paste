from time import time

from flask import request, render_template
from app import app, EXP_TIME

from ..models.note import Note


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form.get('content')

        if len(content) > 1:
            note = Note(ts=int(time()), content=content)
            note.save()

    notes = Note.query.filter(Note.ts > int(time()) - EXP_TIME) \
        .order_by(Note.id.desc())

    return render_template('index.html',
                           notes=notes)
