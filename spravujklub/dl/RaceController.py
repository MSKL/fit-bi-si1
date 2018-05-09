from dl import IRaceController
from datetime import datetime
from dl.models import Race


class RaceController(IRaceController):
    """Database controller for Race objects."""

    def __init__(self, db):
        """
        Initialise the controller with a reference to the database.

        :param db: database
        """

        self.db = db

    def get_race_by_id(self, id):
        """
        Get a race by id. If not found, raise an exception.

        :type id: int
        :param id: id of the race
        :rtype: Race
        :return: race with the id
        """

        race = Race.query.get(id)

        if race is None:
            raise Exception("Race with id %s not found." % str(id))

        return race

    def get_all_races(self):
        """
        Gets all races in the database

        :rtype: list
        :return: all races in the database
        """

        return Race.query.all()

    def add_race(self, name, created_by_user_id, date, deadline, info):
        """
        Add a race to the database.

        :type name: str
        :param name: name of the race
        :type created_by_user_id: int
        :param created_by_user_id: id of the user that created the race
        :type date: datetime
        :param date: date of the race
        :type deadline: datetime
        :param deadline: deadline of the race sign in
        :type info: str
        :param info: information about the race
        """

        # Convert the parameters
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M')
        deadline = datetime.strptime(deadline, '%Y-%m-%dT%H:%M')
        new_race = Race(name, date, deadline, created_by_user_id, info)

        # Commit the session
        self.db.session.add(new_race)
        self.db.session.commit()

    def delete_race(self, race):
        """
        Delete a race from the database.

        :type race: Race
        :param race: race to be deleted
        """

        # TODO: not implemented yet
        pass
