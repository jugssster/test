import unittest
from unittest import mock

from main import year_of_birth

class TestYearOfBirth(unittest.TestCase):
    def test_age_of_22(self):
        """
        Test that it can return right year of birth for age of 22
        """
        with mock.patch('builtins.input', return_value=22):
            self.assertEqual(year_of_birth(), 2001)

if __name__ == '__main__':
    unittest.main()
