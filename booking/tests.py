from django.test import TestCase

# Create your tests here.
class SampleTest(TestCase):
    def test_example(self):
        """Test if 1 + 1 equals 2"""
        self.assertEqual(1 + 1, 2)