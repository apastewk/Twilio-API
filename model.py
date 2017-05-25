"""Models for my database to store questions questions."""

import os
from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostreSQL database.  Getting the through the
# Flask-SQLAlchemy helper library.

db = SQLAlchemy()


################################################################################

# Model definitions

class User(db.Model):
    """User of something website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    email = db.Column(db.String(64))
    phonenumber = db.Column(db.String(10))
    question = db.Column(db.String(500))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id: {} email: {}>".format(self.user_id, self.email)


################################################################################

def connect_to_db(app, db_uri="postgresql:///twiliodb"):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    """Will conenct to the db."""

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."
