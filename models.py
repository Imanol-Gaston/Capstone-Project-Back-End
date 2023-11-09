from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False) 
    description = db.Column(db.String(500), nullable=False) 
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    
    @classmethod
    def create(cls, user_id, description):
      profile = Profile(user_id=user_id, description=description)
      return profile.save()

    def save(self):
      try:
        db.session.add(self)
        db.session.commit()

        return self
      except:
        return False
      
    def json(self):
      return {
        'id': self.id,
        'user_id': self.user_id,
        'description': self.description,
        'created_at': self.created_at
      }


class Experience(db.Model):
    __tablename__ = 'experiences'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False) 
    role = db.Column(db.String(120), nullable=False) 
    supplier = db.Column(db.String(120), nullable=False) 
    product = db.Column(db.String(120), nullable=False) 
    location = db.Column(db.String(120), nullable=False) 
    category = db.Column(db.String(120), nullable=False) 
    description = db.Column(db.String(500), nullable=False) 
    year = db.Column(db.Integer, nullable=False) 
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())