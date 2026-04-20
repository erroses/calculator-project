# test_calculator.py
import pytest
from calculator import sum, sub, mul, div


# ─── 덧셈 ────────────────────────────────
class TestSum:
    def test_sum_positive(self):
        assert sum(2, 3) == 5

    def test_sum_negative(self):
        assert sum(-1, -2) == -3

    def test_sum_zero(self):
        assert sum(5, 0) == 5


# ─── 뺄셈 ────────────────────────────────
class TestSub:
    def test_sub_basic(self):
        assert sub(10, 4) == 6

    def test_sub_negative_result(self):
        assert sub(3, 7) == -4


# ─── 곱셈 ────────────────────────────────
class TestMul:
    def test_mul_basic(self):
        assert mul(3, 4) == 12

    def test_mul_by_zero(self):
        assert mul(5, 0) == 0

    def test_mul_negatives(self):
        assert mul(-2, 3) == -6


# ─── 나눗셈 ──────────────────────────────
class TestDiv:
    def test_div_basic(self):
        assert div(10, 2) == 5.0

    def test_div_float_result(self):
        assert div(7, 2) == 3.5

    def test_div_by_zero_raises(self):
        with pytest.raises(ValueError):
            div(5, 0)