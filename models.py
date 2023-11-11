from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False) 
    brief_description = db.Column(db.String(500), nullable=False) 
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    fullname = db.Column(db.String(50), nullable=False)
    full_description = db.Column(db.String(3000), nullable=True)
    
    @classmethod
    def create(cls, user_id, brief_description, fullname, full_description):
      profile = Profile(user_id=user_id, brief_description=brief_description, fullname=fullname, full_description=full_description)
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
        'brief_description': self.brief_description,
        'created_at': self.created_at,
        'fullname': self.fullname,
        'full_description': self.full_description
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