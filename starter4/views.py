import colander
import deform.widget

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from .models import (
    DBSession,
    Page)


class WikiPage(colander.MappingSchema):
    title = colander.SchemaNode(colander.String())
    body = colander.SchemaNode(colander.String())


class WikiViews(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def wiki_form(self):
        schema = WikiPage()
        return deform.Form(schema, buttons=('submit',))

    @property
    def reqts(self):
        return self.wiki_form.get_widget_resources()

    @view_config(route_name='wiki_view',
                 renderer='templates/wiki_view.jinja2')
    def wiki_view(self):
        pages = DBSession.query(Page).order_by(Page.title)
        return dict(pages=pages)

    @view_config(route_name='wikipage_add',
                 renderer='templates/wikipage_addedit.jinja2')
    def wikipage_add(self):
        form = self.wiki_form.render()

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = self.wiki_form.validate(controls)
            except deform.ValidationFailure as e:
                # Form is NOT valid
                return dict(form=e.render())

            # Form is valid, make a new identifier and add to list
            new_title = appstruct['title']
            new_body = appstruct['body']
            DBSession.add(Page(title=new_title, body=new_body))

            # Get the new ID and redirect
            page = DBSession.query(Page).filter_by(title=new_title).one()
            new_uid = page.uid
            # Now visit new page
            url = self.request.route_url('wikipage_view', uid=new_uid)
            return HTTPFound(url)

        return dict(form=form)

    @view_config(route_name='wikipage_view',
                 renderer='templates/wikipage_view.jinja2')
    def wikipage_view(self):
        return dict()

    @view_config(route_name='wikipage_edit',
                 renderer='templates/wikipage_addedit.jinja2')
    def wikipage_edit(self):

        wiki_form = self.wiki_form
        context = self.context

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = wiki_form.validate(controls)
            except deform.ValidationFailure as e:
                return dict(page=context, form=e.render())

            # Change the content and redirect to the view
            context.title = appstruct['title']
            context.body = appstruct['body']

            url = self.request.route_url('wikipage_view',
                                         uid=context.uid)
            return HTTPFound(url)

        form = wiki_form.render(
            dict(
                title=context.title,
                body=context.body
            )
        )

        return dict(form=form)