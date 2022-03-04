from socket import ALG_SET_AEAD_ASSOCLEN
from models import User, Post, Tag, PostTag, db
from app import app

db.session.rollback()

# Create all tables
db.drop_all()
db.create_all()

# Id tables isn't empty, empty it
User.query.delete()
Post.query.delete()
Tag.query.delete()

# Add users
gary = User(first_name = "Gary", last_name = "Mendez")
elliot = User(first_name = "Elliot", last_name = "Stabler")
michael = User(first_name = "Michael", last_name = "Westen")
olivia = User(first_name = "Olivia", last_name = "Benson")
# Add new objects to session, so they'll persist
db.session.add(gary)
db.session.add(elliot)
db.session.add(michael)
db.session.add(olivia)

# Commit otherwise, this'll never get saved
db.session.commit()

first_post = Post(title = "1st Post",
content = "This is the first post!",
user_code = 1
)

second_post = Post(title = " El's first post", 
content = "Wheatly is a dead man!", 
user_code = 2)

third_post = Post(title = "Noah",
content = "Made it home to tuck my son in :)",
user_code = 4)

fourth_post = Post(title = "John",
content = "I miss you, man",
user_code = 1)

fifth_post = Post(title = "Sam and Jesse",
content = "They are the real heroes",
user_code = 3)

# Add new objects to session, so they'll persist
db.session.add(first_post)
db.session.add(second_post)
db.session.add(third_post)
db.session.add(fourth_post)
db.session.add(fifth_post)

# Commit otherwise, this'll never get saved
db.session.commit()


happy = Tag(name = "happy")

# Add new objects to session, so they'll persist
db.session.add(happy)

# Commit otherwise, this'll never get saved
db.session.commit()

one = PostTag(post_id = 3, tag_id = 1)

db.session.add(one)

db.session.commit()