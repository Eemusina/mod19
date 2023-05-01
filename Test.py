import pytest
from calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_multiply_succes(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_adding_succes(self):
        assert self.calc.adding(self, 1, 3) == 4

    def test_subtraction_succes(self):
        assert self.calc.subtraction(self, 4, 1) == 3

    def test_division_succes(self):
        assert self.calc.division(self, 4, 2) == 2

    def teardown(self):
        print('Выполнение метода Teardown')


