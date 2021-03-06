from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from .models import DBSession, Base


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings,
                          root_factory='.models.root_factory')

    config.add_route('wiki_view', '/',
                     factory='.models.root_factory')
    config.add_route('wikipage_add', '/add',
                     factory='.models.root_factory')
    config.add_route('wikipage_view', '/{uid}',
                     factory='.models.page_factory')
    config.add_route('wikipage_edit', '/{uid}/edit',
                     factory='.models.page_factory')

    config.add_static_view(name='static', path='starter4:static')
    config.add_static_view('deform_static', 'deform:static/')
    config.include('pyramid_jinja2')
    config.scan('.views')
    return config.make_wsgi_app()