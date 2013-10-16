from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar'
]

setup(
    name='starter',
    version='0.1',
    install_requires=requires,
    author='Paul Everitt',
    description='Set of starter packages for the Pyramid web framework',
    entry_points="""\
      [paste.app_factory]
      sample1 = sample1:main
      sample2 = sample2:main
      """)
