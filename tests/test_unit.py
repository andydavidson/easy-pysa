import unittest

from easypysa.easypysa import EasyPysa

class UnitTests(unittest.TestCase):
    def test_can_read_index(self):
        easy = EasyPysa(easyrsa_directory="test_data")
        self.assertTrue(easy._check_executable() == "OK")

if __name__ == "__main__":
    unittest.main()
