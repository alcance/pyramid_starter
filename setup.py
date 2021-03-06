from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'deform',
    'sqlalchemy',
    'pyramid_tm',
    'zope.sqlalchemy',
    'nose',
    'WebTest'
]

setup(
    name='starter',
    version='0.1',
    install_requires=requires,
    author='Paul Everitt',
    description='Set of starter packages for the Pyramid web framework',
    entry_points="""\
      [paste.app_factory]
      starter2 = starter2:main
      starter3 = starter3:main
      starter4 = starter4:main
      [console_scripts]
      initialize_starter_db = starter4.initialize_db:main
      """)
