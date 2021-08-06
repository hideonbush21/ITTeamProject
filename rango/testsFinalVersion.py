import os
import re
# import forms
from datetime import datetime, timedelta
from django.test import TestCase
from django.conf import settings
from django.forms import fields as django_fields
from . import forms
from .models import Category, Page

# from .. import rango

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


class ConfigurationTests(TestCase):
    def test_module_exists(self):
        """
        Tests that the forms.py module exists in the expected location.
        """
        project_path = os.getcwd()
        rango_app_path = os.path.join(project_path, 'rango')
        forms_module_path = os.path.join(rango_app_path, 'forms.py')

        self.assertTrue(os.path.exists(forms_module_path),
                        f"{FAILURE_HEADER}We couldn't find Rango's new forms.py module. This is required to be created at the top of Section 7.2. This module should be storing your two form classes.{FAILURE_FOOTER}")

    def test_category_form_class(self):

        project_path = os.getcwd()
        rango_app_path = os.path.join(project_path, 'rango')
        forms_module_path = os.path.join(rango_app_path, 'forms.py')

        self.assertTrue('CategoryForm' in dir(forms),
                        f"{FAILURE_HEADER}The class CategoryForm could not be found in Rango's forms.py module. Check you have created this class in the correct location, and try again.{FAILURE_FOOTER}")

        from .forms import CategoryForm
        # category_form = CategoryForm()
        #
        # # Do you correctly link Category to CategoryForm?
        # self.assertEqual(type(category_form.__dict__['instance']), Category,
        #                  f"{FAILURE_HEADER}The CategoryForm does not link to the Category model. Have a look in the CategoryForm's nested Meta class for the model attribute.{FAILURE_FOOTER}")
        #
        # fields = category_form.fields
        #
        # expected_fields = {
        #     'name': django_fields.CharField,
        #     'views': django_fields.IntegerField,
        #     'likes': django_fields.IntegerField,
        #     'rank': django_fields.CharField,
        #     'region': django_fields.CharField,
        # }
        #
        # for expected_field_name in expected_fields:
        #     expected_field = expected_fields[expected_field_name]
        #
        #     self.assertTrue(expected_field_name in fields.keys(),
        #                     f"{FAILURE_HEADER}The field '{expected_field_name}' was not found in your CategoryForm implementation. Check you have all required fields, and try again.{FAILURE_FOOTER}")
        #     self.assertEqual(expected_field, type(fields[expected_field_name]),
        #                      f"{FAILURE_HEADER}The field '{expected_field_name}' in CategoryForm was not of the expected type '{type(fields[expected_field_name])}'.{FAILURE_FOOTER}")