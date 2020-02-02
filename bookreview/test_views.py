from django.test import TestCase

# test confirms that the app is linked to the overall project and can identify the homepage
class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)

# test confirms that the the user is directed to the bookreview page when it is requested and tha correct template is being loaded
    def test_get_review_page(self):
        page = self.client.get("/bookreview/review/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bookreview.html")