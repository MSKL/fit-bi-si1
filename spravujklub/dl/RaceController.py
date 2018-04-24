from dl.IRaceController import IRaceController
from datetime import datetime
from dl.models.Race import Race


class RaceController(IRaceController):

    def __init__(self, db):
        self.db = db

    def get_race_by_id(self, id):
        return Race.query.get(id)

    def get_all_races(self):
        """Gets all races in the database"""
        return Race.query.all()

    def add_race(self, name, created_by_user_id, date, deadline, info):
        # Convert the parameters
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M')
        deadline = datetime.strptime(deadline, '%Y-%m-%dT%H:%M')
        new_race = Race(name, date, deadline, created_by_user_id, info)

        # Commit the session
        self.db.session.add(new_race)
        self.db.session.commit()
