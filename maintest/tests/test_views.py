from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class SimpleTest(TestCase):
    def test_home(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_session_ready_for_test(self):
        resp = self.client.get(reverse("first_test_ready"))
        self.assertEqual(resp.status_code, 200)

    def test_gen_test_not_accessible_direct(self):
        resp = self.client.get(reverse("first_test"))
        self.assertEqual(resp.status_code, 302)
    
    def test_gen_test_accessible_via_ready_for_test(self):
        resp = self.client.get(reverse("first_test_ready"))
        resp1 = self.client.get(reverse("first_test"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp1.status_code, 200)

    def test_result_page_inaccessible_via_get_request(self):
        resp = self.client.get(reverse("result"))
        self.assertEqual(resp.status_code, 302)

    def test_review_page_inaccessible_direct(self):
        resp = self.client.get(reverse("review_answers"))
        self.assertEqual(resp.status_code, 302)
