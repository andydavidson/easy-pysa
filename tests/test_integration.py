import unittest

from easypysa.easypysa import EasyPysa

class UnitTests(unittest.TestCase):
    def test_can_load_executable(self):
        easy = EasyPysa()
        self.assertTrue(easy._check_executable() == "OK")

if __name__ == "__main__":
    unittest.main()
