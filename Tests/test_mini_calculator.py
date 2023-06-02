from App.mini_calculator import MiniCalc
import pytest


class TestMiniCalc:
    # setup_method() and teardown_method() will execute for each test case
    def setup_method(self):
        print('Executes at the beginning')
        self.clac1 = MiniCalc(3, 5)

    def teardown_method(self):
        print('Executes at the end')

    def test_sum(self):
        assert self.clac1.sum() == 8, 'Sum is not working!'

    @pytest.mark.skip(reason='work in progress')
    def test_subtraction(self):
        assert self.clac1.subtraction() == -2, 'Subtraction is not working!'

    def test_multiplication(self):
        assert self.clac1.multiplication() == 15, 'Multiplication is not working!'

    @pytest.mark.skip(reason='work in progress')
    def test_division(self):
        assert self.clac1.division() == 0.6, 'Division is not working!'

    def test_sum_custom(self):
        assert self.clac1.sum_custom(33, 77) == 110, 'Custom Sum is not working!'

    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            (1, 1, 2),
            (1, 2, 3),
            (5, 5, 10),
        ],
    )
    def test_sum_custom_param(self, a, b, expected):
        assert self.clac1.sum_custom(a, b) == expected, 'Custom Sum is not working!'
