import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import StarterViews

        request = testing.DummyRequest()
        inst = StarterViews(request)
        response = inst.home()
        self.assertIn(b'Home View', response.body)


class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from . import main

        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<h1>Home View', res.body)