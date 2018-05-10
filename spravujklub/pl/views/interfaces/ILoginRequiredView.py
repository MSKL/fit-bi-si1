from flask_login import login_required
from pl.views.interfaces import IDefaultView


class ILoginRequriedView(IDefaultView):
    """View that requires the user to be logged in"""

    decorators = [login_required]

    def dispatch_request(self):
        raise NotImplementedError
