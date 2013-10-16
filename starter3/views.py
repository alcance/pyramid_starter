from random import randint

from pyramid.view import view_config


class StarterViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='home.jinja2')
    def home(self):
        return dict(page_title='Home View')

    @view_config(route_name='output', renderer='json')
    def output(self):
        return dict(output=randint(10000, 99999))