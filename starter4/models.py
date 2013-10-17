from pyramid.security import Allow, Everyone

from sqlalchemy import (
    Column,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Root(Base):
    __tablename__ = 'wikiroot'
    uid = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)


class Page(Base):
    __tablename__ = 'wikipages'
    uid = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
    body = Column(Text)


def root_factory(request):
    return DBSession.query(Root).one()


def page_factory(request):
    uid = int(request.matchdict['uid'])
    return DBSession.query(Page).filter_by(uid=uid).one()