class IRace(object):
    """Race interface class. Contains all methods required by the Member instances."""

    def add_member(self, member):
        """Adds a member to the DB"""
        raise NotImplementedError()

    def remove_member(self, member):
        """Removes a member from the DB"""
        raise NotImplementedError()