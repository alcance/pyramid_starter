from pyramid.response import Response
from pyramid.view import view_config


class StarterViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return Response('<body><h1>Home View</h1></body>')