from socket import ALG_SET_AEAD_ASSOCLEN
from models import User, db
from app import app

db.session.rollback()

# Create all tables
db.drop_all()
db.create_all()

# Id tables isn't empty, empty it
User.query.delete()

# Add users
alan = User(first_name = "Alan", last_name = "Alda")
joel = User(first_name = "Joel", last_name = "Burton")
jane = User(first_name = "Jane", last_name = "Smith")

# Add new objects to session, so they'll persist
db.session.add(alan)
db.session.add(joel)
db.session.add(jane)

# Commit otherwise, this'll never get saved
db.session.commit()