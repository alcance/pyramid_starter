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
        result = inst.home()
        self.assertEqual('Home View', result['name'])

    def test_output(self):
        from .views import StarterViews

        request = testing.DummyRequest()
        inst = StarterViews(request)
        result = inst.output()
        self.assertIn('output', result)


class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from . import main

        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<h1>Home View', res.body)

    def test_output(self):
        res = self.testapp.get('/output', status=200)
        self.assertIn('output', res.json_body)
        self.assertEqual(res.content_type, 'application/json')