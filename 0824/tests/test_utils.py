"""工具函数模块的单元测试。

演示纯函数的测试方法：输入确定、无副作用、易于测试。
"""

from __future__ import annotations

import pytest

from calculator.utils import format_result, is_number, parse_expression


# ======================================================================
# parse_expression 测试
# ======================================================================

class TestParseExpression:
    """测试表达式解析函数。"""

    @pytest.mark.parametrize(
        "expression, expected",
        [
            ("3 + 4", (3.0, "+", 4.0)),
            ("10 - 3", (10.0, "-", 3.0)),
            ("2.5 * 4", (2.5, "*", 4.0)),
            ("8 / 2", (8.0, "/", 2.0)),
            ("2 ** 10", (2.0, "**", 10.0)),
            ("10 % 3", (10.0, "%", 3.0)),
            ("-5 + 3", (-5.0, "+", 3.0)),
            ("1.5e2 * 2", (150.0, "*", 2.0)),
        ],
    )
    def test_valid_expressions(
        self, expression: str, expected: tuple[float, str, float]
    ) -> None:
        """合法表达式应正确解析为三元组。"""
        assert parse_expression(expression) == expected

    @pytest.mark.parametrize(
        "invalid_expression",
        [
            "",
            "3 +",
            "+ 4",
            "3 4",
            "3 + 4 + 5",
            "abc + def",
            "3 & 4",
        ],
    )
    def test_invalid_expressions_return_none(self, invalid_expression: str) -> None:
        """不合法表达式应返回 None。"""
        assert parse_expression(invalid_expression) is None

    def test_whitespace_tolerance(self) -> None:
        """应容忍表达式两端的多余空白。"""
        assert parse_expression("  3   +   4  ") == (3.0, "+", 4.0)


# ======================================================================
# format_result 测试
# ======================================================================

class TestFormatResult:
    """测试结果格式化函数。"""

    def test_basic_formatting(self) -> None:
        """基本格式化应保留指定小数位。"""
        assert format_result(3.14159, precision=2) == "3.14"

    def test_integer_value(self) -> None:
        """整数也应按精度补零。"""
        assert format_result(42, precision=3) == "42.000"

    def test_thousands_separator(self) -> None:
        """千位分隔符应正确添加。"""
        assert format_result(1234567.89, precision=2, with_thousands_sep=True) == "1,234,567.89"

    def test_negative_number(self) -> None:
        """负数格式化应保留负号。"""
        assert format_result(-1234.5, precision=1) == "-1234.5"

    def test_zero(self) -> None:
        """零的格式化。"""
        assert format_result(0, precision=4) == "0.0000"

    def test_negative_precision_raises(self) -> None:
        """负精度应抛出 ValueError。"""
        with pytest.raises(ValueError, match="precision 不能为负数"):
            format_result(3.14, precision=-1)

    def test_rounding(self) -> None:
        """应正确四舍五入。"""
        assert format_result(2.345, precision=2) == "2.35"


# ======================================================================
# is_number 测试
# ======================================================================

class TestIsNumber:
    """测试数字判断函数。"""

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("123", True),
            ("-456", True),
            ("3.14", True),
            ("-0.5", True),
            ("1e10", True),
            ("2.5E-3", True),
            ("", False),
            ("abc", False),
            ("12a", False),
            ("1.2.3", False),
            ("--1", False),
        ],
    )
    def test_is_number(self, s: str, expected: bool) -> None:
        """测试各种字符串的数字判断。"""
        assert is_number(s) == expected
