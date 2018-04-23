class IRaceController(object):

    def add_race(self, race):
        """Adds an instance of a race to the database"""
        raise NotImplementedError()

    def delete_race(self, race):
        """Deletes an instance of the race from the database"""
        raise NotImplementedError()

    def get_signed_up_members(self, race):
        """Gets the members that are going to the race"""
        raise NotImplementedError()

    def get_all_races(self):
        """Gets all races in the database"""
        raise NotImplementedError()