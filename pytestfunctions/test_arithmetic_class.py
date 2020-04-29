import pytest
from selenium import webdriver

from pytestfunctions.arithmetic_class import ArithmeticClass


class TestArithmeticModule:

    @pytest.fixture()
    def setUp(self):
        self.ac = ArithmeticClass()

    def test_add(self):
        # ac = ArithmeticClass()
        res = self.ac.add(10, 20)
        assert res == 30  # pass
        res = self.ac.add(20.30, 20.70)
        assert res == 40  # fail
        res = self.ac.add(20.30, '23')
        assert res == 43.30  # fail

    def test_mod(self):
        # ac = ArithmeticClass()
        res = self.ac.mod(20, 10)
        assert res == 0

    def test_mul(self):
        # ac = ArithmeticClass()
        res = self.ac.product(10, 20)
        assert res == 200
