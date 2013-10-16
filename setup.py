from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
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
      """)
