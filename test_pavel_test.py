# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestPavelTest(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_verify_movie_exists_uidc999121bf2c449a088b340e9bc8394aa(self):
        self.actionwords.check_that_the_movie_exists()

    def test_verify_movie_doesnt_exist_uid4f13e0dcce09420cbf85a338ee5c0dbb(self):
        self.actionwords.check_that_the_movie_doesnt_exist()
