from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    config.add_route('output', '/output')
    config.add_static_view(name='static', path='starter3:static')
    config.include('pyramid_jinja2')
    config.scan('.views')
    return config.make_wsgi_app()