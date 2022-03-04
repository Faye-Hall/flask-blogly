"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

from sqlalchemy import ForeignKey
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
    

class Post(db.Model):
    """User Posts"""
    __tablename__ = "posts"

    def __repr__(self):
        return f"id={self.id}, title={self.title} content={self.content}, DT={self.created_at}"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.Text,
                       nullable=False,
                       unique=True)
    content = db.Column(db.Text,
                       nullable=False)
    created_at = db.Column(db.DateTime,
                            nullable=False,
                            default=datetime.datetime.now
                            )
    user_code = db.Column(db.Integer,
                          db.ForeignKey(User.id))

    person = db.relationship("User", backref= "posts")

    
class Tag(db.Model):
    """Tags"""
    __tablename__= "tags"

    def __repr__(self):
        return f"id= {self.id}, name={self.name}"

    id = db.Column(db.Integer,
                    primary_key=True
                    )
    name = db.Column(db.Text,
                     nullable=False,
                     unique=True
                     )

    post = db.relationship("Post",
    secondary= "posttags", 
     backref="tags")
                    
class PostTag(db.Model):
    """PostTags"""

    __tablename__= "posttags"
    
    def __repr__(self):
        return f"post_id = {self.post_id}, tag_id = {self.tag_id}"

    post_id = db.Column(db.Integer,
                        db.ForeignKey(Post.id),
                        primary_key=True
                        )
    tag_id = db.Column(db.Integer,
                       db.ForeignKey(Tag.id),
                        primary_key=True
                       )
    