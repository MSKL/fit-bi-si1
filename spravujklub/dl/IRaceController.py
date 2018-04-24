class IRaceController(object):

    def get_race_by_id(self, id):
        """Get a race by ID"""
        raise NotImplementedError()

    def get_all_races(self):
        """Gets all races in the database"""
        raise NotImplementedError()

    def add_race(self, name, created_by_user_id, date, deadline, info):
        """Adds an instance of a race to the database"""
        raise NotImplementedError()

    def delete_race(self, race):
        """Deletes an instance of the race from the database"""
        raise NotImplementedError()
