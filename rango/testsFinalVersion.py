import os
import re
from datetime import datetime, timedelta
from django.test import TestCase
from django.conf import settings
from .models import Category, Page
from django.urls import reverse

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

f"{FAILURE_HEADER} {FAILURE_FOOTER}"


class ConfigurationTests(TestCase):
    """
        Tests to see if AuthenticationMiddleware data is added to the setting file:
    """
    def test_middleware_present(self):
        self.assertTrue('django.contrib.auth.middleware.AuthenticationMiddleware' in settings.MIDDLEWARE)

    """
        Tests to see if Authentication app is added in the setting file:
    """
    def test_session_app_present(self):
        self.assertTrue('django.contrib.auth' in settings.INSTALLED_APPS)


class ModelTests(TestCase):
    def setUp(self):
        category_py = Category.objects.get_or_create(name='University of Glasgow', views=9999, likes=9999, rank=1, region='United Kingdom')
        Category.objects.get_or_create(name='UoG', views=222, likes=222, rank=3, region='United Kingdom')

        Page.objects.get_or_create(category=category_py[0],
                                   title='UoG',
                                   url='https://www.gla.ac.uk',
                                   rank=1,
                                   content='This is my favourite University, salute!',
                                   views=156)

    def test_category_model(self):
        category_py = Category.objects.get(name='University of Glasgow')
        self.assertEqual(category_py.views, 9999,
                         f"{FAILURE_HEADER}Tests on the Category model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
        self.assertEqual(category_py.likes, 9999,
                         f"{FAILURE_HEADER}Tests on the Category model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
        self.assertEqual(category_py.rank, 1,
                         f"{FAILURE_HEADER}Tests on the Category model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
        self.assertEqual(category_py.region, 'United Kingdom',
                         f"{FAILURE_HEADER}Tests on the Category model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")

        category_dj = Category.objects.get(name='UoG')
        self.assertEqual(category_dj.views, 222,
                         f"{FAILURE_HEADER}Tests on the Category model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
        self.assertEqual(category_dj.likes, 222,
                         f"{FAILURE_HEADER}Tests on the Category model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
        self.assertEqual(category_dj.rank, 3,
                         f"{FAILURE_HEADER}Tests on the Category model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
        self.assertEqual(category_dj.region, 'United Kingdom',
                         f"{FAILURE_HEADER}Tests on the Category model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")

    def test_page_model(self):

        category_py = Category.objects.get(name='University of Glasgow')
        page = Page.objects.get(title='UoG')
        self.assertEqual(page.url, 'https://www.gla.ac.uk',
                         f"{FAILURE_HEADER}Tests on the Page model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
        self.assertEqual(page.views, 156,
                         f"{FAILURE_HEADER}Tests on the Page model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
        self.assertEqual(page.title, 'UoG',
                         f"{FAILURE_HEADER}Tests on the Page model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
        self.assertEqual(page.category, category_py,
                         f"{FAILURE_HEADER}Tests on the Page model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
        self.assertEqual(page.rank, 1,
                         f"{FAILURE_HEADER}Tests on the Page model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")
        self.assertEqual(page.content, 'This is my favourite University, salute!',
                         f"{FAILURE_HEADER}Tests on the Page model failed. Check you have all required attributes (including those specified in the exercises!), and try again.{FAILURE_FOOTER}")

