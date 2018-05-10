from flask.views import View


class IDefaultView(View):
    """Interface for a generic view"""

    def dispatch_request(self):
        """Displach the request"""
        raise NotImplementedError


