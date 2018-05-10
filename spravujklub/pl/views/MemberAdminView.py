from flask import request, render_template
from spravujklub import app, member_controller
from pl.views.interfaces.ILoginRequiredView import ILoginRequriedView


class MemberAdminView(ILoginRequriedView):
    """Member administration panel"""

    def dispatch_request(self):
        """Render the admin panel website"""
        name = request.values.get("name")
        email = request.values.get("mail")
        password = request.values.get("password")
        delete_id = request.values.get("delete")

        error = None
        if name is not None and email is not None:
            try:
                member_controller.create_member(name=name, mail=email, password=password)
            except Exception as ex:
                error = str(ex)

        if delete_id is not None:
            try:
                delete_id = int(delete_id)
                member_to_delete = member_controller.get_member_by_id(delete_id)
                member_controller.delete_member(member_to_delete)
            except Exception as ex:
                print(str(ex))

        # Render the template
        return render_template("admin_member.html", members=member_controller.get_all_members(), title="Member admin", error=error)


# Catch the errors on import to successfully generate the documentation
try:
    app.add_url_rule('/admin_member', view_func=MemberAdminView.as_view('admin_member'), methods=['GET'])
except Exception as ex:
    print(str(ex))
