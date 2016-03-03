import unittest
from contribute import Contribute
class TestContributions(unittest.TestCase):
    def test_contribute_list_size(self):
        contrib = Contribute()
        self.assertEqual(len(contrib.contribution_list()), 3)

    def test_contribute_content(self):
        contrib = Contribute()
        self.assertEqual(contrib.contribution_list(),
                         ["potato", "cars", "animals"])

    def test_contribute_has_content(self):
        """ Contribution test if it has objects """
        contrib = Contribute()
        self.assertTrue(contrib.contribution_list())

if __name__ == '__main__':
    unittest.main()
