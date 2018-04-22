
"""
# Create an empty DB file
sqlite3 database/database.db
sqlite> .exit
"""

# Create the tables based on the structure of the database specified in the models.py
from main import db
db.create_all()

"""
# DB file now contains the member table, lets insert an user
sqlite3 database/database.db
sqlite> .tables
member
sqlite> insert into member values (0, "Cenda", "cenda@cendovajeskyne.cz");
sqlite> .exit
"""
