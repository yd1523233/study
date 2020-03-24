from python.calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    def test_add_1(self):
        assert self.calc.add(1, 2) == 3

    def test_add_2(self):
        assert self.calc.add(1, 3) == 5

    def test_add_3(self):
        assert self.calc.add(0, 0.5) == 2

    def test_div_1(self):
        assert self.calc.div(1, 2) == 0.5

    def test_div_2(self):
        assert self.calc.div(1, 0) == 0

    def test_div_3(self):
        assert self.calc.div(0.5, 0.5) == 1
