

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate=Migrate(app, db)



#My Models to create Tables
class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.String, nullable = False)
    seeking_description = db.Column(db.String(120))
    shows = db.relationship('Shows', backref='venue', lazy=True)
    

    def __repr__(self):
      return f"<venue id={self.id} name={self.name}>"


    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)))
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.String, nullable = False)
    seeking_description = db.Column(db.String(120))
    shows = db.relationship('Shows', backref='artist', lazy=True)
    

  
    def __repr__(self):
      return f"<artist id={self.id} name={self.name}>"

class Shows(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)

    def __repr__(self):
      return f"<artist id={self.id} venue id={self.id}>"