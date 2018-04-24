class IRace(object):

    def add_member(self, member):
        """Adds a member to the DB"""
        raise NotImplementedError()

    def remove_member(self, member):
        """Removes a member from the DB"""
        raise NotImplementedError()