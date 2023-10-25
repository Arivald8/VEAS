import unittest
from src import __version__


class TestVersion(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    
    def test_version(self):
        self.assertEqual(__version__, "0.1")

