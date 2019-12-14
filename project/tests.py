# from django.contrib.auth.models import User
# from django.test import TestCase, Client
# from django.urls import reverse_lazy
# from project.models import Code
# import unittest
#
# # Create your tests here.
# class ProjectTestCase(TestCase):
#     def test_true_is_true(self):
#         """ Tests if True is equal to True. Should always pass. """
#         self.assertEqual(True, True)
#     def test_code_slugify_on_save(self):
#         """ Tests the slug generated when saving a Code. """
#         # Author is a required field in our model.
#         # Create a user for this test and save it to the test database.
#         user = User()
#         user.save()
#
#         # Create and save a new page to the test database.
#         code = Code(title="My Test Code", content="test", author=user)
#         code.save()
#
#         # Make sure the slug that was generated in Page.save()
#         # matches what we think it should be.
#         self.assertEqual(code.slug, "my-test-code")
#
# class CodeListViewTests(TestCase):
#     def test_multiple_codes(self):
#         # Make some test data to be displayed on the page.
#         user = User.objects.create()
#
#         Code.objects.create(title="My Test Code", content="test", author=user)
#         Code.objects.create(title="Another Test Code", content="test", author=user)
#
#         # Issue a GET request to the MakeWiki homepage.
#         # When we make a request, we get a response back.
#         response = self.client.get('/')
#
#         # Check that the response is 200 OK.
#         self.assertEqual(response.status_code, 200)
#
#         # Check that the number of pages passed to the template
#         # matches the number of pages we have in the database.
#         responses = response.context['codes']
#         self.assertEqual(len(responses), 2)
#
#         self.assertQuerysetEqual(
#             responses,
#             ['<Code: My Test Code>', '<Code: Another Test Code>'],
#             ordered=False
#         )
#     def test_create_wiki_page(self):
#         """ Test so that the form page load when visiting create """
#         response = self.client.get("/new_project/")
#         self.assertEqual(response.status_code, 200)
#     def test_specific_page(self):
#         # Create a user for this test
#         user = User.objects.create() # This line will both create the user and save it
#         # Create a page and save
#         test_code = Code.objects.create(title="My Testy Code", content="test", author=user, slug='my-testy-code')
#         # Page.objects.create(title="Another Test Page", content="test again", author=user)
#         # Calling homepage and setting equal to response
#         # make a Get request, self.clent is in TestCase
#         response = self.client.get(reverse_lazy('code-details-project', args=(test_code.slug,)))
#         # Checks if page is ok so response with 200
#         self.assertEqual(response.status_code, 200)
