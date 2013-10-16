from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('wiki_view', '/')
    config.add_route('wikipage_add', '/add')
    config.add_route('wikipage_view', '/{uid}')
    config.add_route('wikipage_edit', '/{uid}/edit')
    config.add_static_view(name='static', path='starter4:static')
    config.add_static_view('deform_static', 'deform:static/')
    config.include('pyramid_jinja2')
    config.scan('.views')
    return config.make_wsgi_app()