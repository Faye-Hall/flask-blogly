"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User."""
    __tablename__ = "users"

    def __repr__(self):
        return f"ID = {self.id}, firstname = {self.first_name}, lastname = {self.last_name}"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.Text,
                    nullable=False,
                    unique=True)
    last_name = db.Column(db.Text,
                    nullable=False,
                    unique=True)
    image_url = db.Column(db.Text,
                    nullable=False,
                    unique=False,
                    default= "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"
)               
    

