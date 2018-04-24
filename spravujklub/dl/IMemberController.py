class IMemberController(object):

    def get_all_members(self):
        """Gets all members in the database"""
        raise NotImplementedError()

    def get_member_by_id(self, id):
        """Gets the member by id and returns a Member instance"""
        raise NotImplementedError()

    def get_member_by_mail(self, mail):
        """Gets the member by mail and returns a Member instance"""
        raise NotImplementedError()

    def delete_member(self, member):
        """Deletes an instance of a member from the Database"""
        raise NotImplementedError()

    def create_member(self, name, mail, password):
        """Creates a new member instance and adds it to the Database"""
        raise NotImplementedError()

    def login_member(self, login_mail, login_password):
        """Logs an user into the system"""
        raise NotImplementedError()

    def logout_member(self):
        """Logs out an user from system"""
        raise NotImplementedError()