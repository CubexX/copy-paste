import re

from .. import db, EXP_TIME

from datetime import datetime
from time import time
from sqlalchemy.ext.hybrid import hybrid_property


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ts = db.Column(db.Integer)
    content = db.Column(db.Text)

    def __repr__(self):
        return '<Note %i>' % self.id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @hybrid_property
    def date(self):
        return str(datetime.fromtimestamp(self.ts)
                   .strftime('%H:%M, %d.%m.%Y'))

    @hybrid_property
    def disappear_time(self):
        i = EXP_TIME - int(time()) + self.ts

        if i > 60:
            return "%i %s" % (round(i / 60), 'мин')
        else:
            return "%s %s" % (i, 'сек')

    @hybrid_property
    def get_content(self):
        return re.sub('(https?://[^\s]+)', '<a href="\g<1>">\g<1></a>', self.content)
