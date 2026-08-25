"""Calculator 核心类的单元测试。

测试规范要点：
- 测试文件以 test_ 开头，测试函数以 test_ 开头
- 每个测试函数只测一个行为
- 使用 Arrange-Act-Assert（准备-执行-断言）三段式结构
- 使用 pytest.fixture 复用测试对象
- 使用 pytest.mark.parametrize 做参数化测试
- 使用 pytest.raises 测试异常
"""

from __future__ import annotations

import pytest

from calculator import Calculator, OperationError


# ======================================================================
# Fixtures：复用的测试对象
# ======================================================================

@pytest.fixture
def calc() -> Calculator:
    """返回一个默认精度的 Calculator 实例。"""
    return Calculator(precision=4)


@pytest.fixture
def calc_with_history() -> Calculator:
    """返回一个开启历史记录的 Calculator 实例。"""
    return Calculator(precision=2, enable_history=True)


# ======================================================================
# 初始化与配置测试
# ======================================================================

class TestCalculatorInit:
    """测试 Calculator 的初始化逻辑。"""

    def test_default_precision(self) -> None:
        """默认精度应为 4。"""
        calc = Calculator()
        assert calc.precision == 4

    def test_custom_precision(self) -> None:
        """自定义精度应正确设置。"""
        calc = Calculator(precision=8)
        assert calc.precision == 8

    @pytest.mark.parametrize("invalid_precision", [-1, 11, 100])
    def test_invalid_precision_raises(self, invalid_precision: int) -> None:
        """精度超出 0~10 范围应抛出 ValueError。"""
        with pytest.raises(ValueError, match="precision 必须在"):
            Calculator(precision=invalid_precision)

    def test_history_disabled_by_default(self) -> None:
        """默认不开启历史记录。"""
        calc = Calculator()
        assert calc.enable_history is False
        assert calc.history == []


# ======================================================================
# 基本运算测试
# ======================================================================

class TestBasicOperations:
    """测试四则运算。"""

    def test_add(self, calc: Calculator) -> None:
        """加法：正数相加。"""
        # Arrange / Act
        result = calc.add(2, 3)
        # Assert
        assert result == 5

    def test_add_negative(self, calc: Calculator) -> None:
        """加法：含负数。"""
        assert calc.add(-5, 3) == -2

    def test_add_float(self, calc: Calculator) -> None:
        """加法：浮点数精度处理。"""
        assert calc.add(0.1, 0.2) == 0.3

    def test_subtract(self, calc: Calculator) -> None:
        """减法。"""
        assert calc.subtract(10, 4) == 6

    def test_multiply(self, calc: Calculator) -> None:
        """乘法。"""
        assert calc.multiply(3, 4) == 12

    def test_divide(self, calc: Calculator) -> None:
        """除法：正常情况。"""
        assert calc.divide(10, 4) == 2.5

    def test_divide_by_zero_raises(self, calc: Calculator) -> None:
        """除法：除零应抛出 OperationError。"""
        with pytest.raises(OperationError, match="除数不能为零"):
            calc.divide(10, 0)

    def test_power(self, calc: Calculator) -> None:
        """幂运算。"""
        assert calc.power(2, 10) == 1024

    def test_power_negative_exponent(self, calc: Calculator) -> None:
        """幂运算：负指数。"""
        assert calc.power(2, -1) == 0.5


# ======================================================================
# 参数化测试：批量测试多种输入
# ======================================================================

class TestParametrizedOperations:
    """使用 parametrize 批量测试运算。"""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 1, 2),
            (0, 0, 0),
            (-1, 1, 0),
            (100, 200, 300),
            (0.1, 0.2, 0.3),
        ],
        ids=["1+1", "0+0", "-1+1", "100+200", "0.1+0.2"],
    )
    def test_add_parametrized(
        self, calc: Calculator, a: float, b: float, expected: float
    ) -> None:
        """参数化测试加法。"""
        assert calc.add(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [(10, 2, 5), (9, 3, 3), (7, 2, 3.5), (1, 3, 0.3333)],
    )
    def test_divide_parametrized(
        self, calc: Calculator, a: float, b: float, expected: float
    ) -> None:
        """参数化测试除法。"""
        assert calc.divide(a, b) == expected


# ======================================================================
# 表达式解析测试
# ======================================================================

class TestEvaluate:
    """测试 evaluate 方法解析字符串表达式。"""

    @pytest.mark.parametrize(
        "expression, expected",
        [
            ("3 + 4", 7),
            ("10 - 3", 7),
            ("2 * 5", 10),
            ("8 / 2", 4),
            ("2 ** 10", 1024),
            ("10 % 3", 1),
        ],
    )
    def test_valid_expressions(
        self, calc: Calculator, expression: str, expected: float
    ) -> None:
        """测试合法表达式的计算。"""
        assert calc.evaluate(expression) == expected

    def test_invalid_format_raises(self, calc: Calculator) -> None:
        """表达式格式错误应抛出 OperationError。"""
        with pytest.raises(OperationError, match="表达式格式错误"):
            calc.evaluate("3 +")

    def test_unsupported_operator_raises(self, calc: Calculator) -> None:
        """不支持的运算符应抛出 OperationError。"""
        with pytest.raises(OperationError, match="不支持的运算符"):
            calc.evaluate("3 & 4")

    def test_non_numeric_raises(self, calc: Calculator) -> None:
        """非数字操作数应抛出 OperationError。"""
        with pytest.raises(OperationError, match="无法解析为数字"):
            calc.evaluate("abc + 4")


# ======================================================================
# 历史记录测试
# ======================================================================

class TestHistory:
    """测试运算历史记录功能。"""

    def test_history_records_operations(self, calc_with_history: Calculator) -> None:
        """开启历史记录后，运算应被记录。"""
        calc_with_history.add(1, 2)
        calc_with_history.multiply(3, 4)

        assert len(calc_with_history.history) == 2
        assert "1 + 2 = 3" in calc_with_history.history
        assert "3 * 4 = 12" in calc_with_history.history

    def test_history_not_recorded_when_disabled(self, calc: Calculator) -> None:
        """未开启历史记录时，history 应始终为空。"""
        calc.add(1, 2)
        calc.multiply(3, 4)
        assert calc.history == []

    def test_clear_history(self, calc_with_history: Calculator) -> None:
        """清空历史记录后应为空。"""
        calc_with_history.add(1, 2)
        calc_with_history.clear_history()
        assert calc_with_history.history == []

    def test_history_returns_copy(self, calc_with_history: Calculator) -> None:
        """history 属性应返回副本，修改返回值不影响内部状态。"""
        calc_with_history.add(1, 2)
        history = calc_with_history.history
        history.append("fake entry")
        assert "fake entry" not in calc_with_history.history


# ======================================================================
# 精度与边界测试
# ======================================================================

class TestPrecision:
    """测试精度处理。"""

    def test_integer_result_returns_int(self) -> None:
        """结果为整数时应返回 int 类型。"""
        calc = Calculator(precision=4)
        result = calc.add(2, 3)
        assert isinstance(result, int)
        assert result == 5

    def test_float_result_returns_float(self) -> None:
        """结果为小数时应返回 float 类型。"""
        calc = Calculator(precision=4)
        result = calc.divide(1, 3)
        assert isinstance(result, float)

    def test_high_precision(self) -> None:
        """高精度设置应保留更多小数位。"""
        calc = Calculator(precision=8)
        result = calc.divide(1, 7)
        assert result == 0.14285714

    def test_zero_precision(self) -> None:
        """精度为 0 时应返回整数。"""
        calc = Calculator(precision=0)
        assert calc.divide(7, 2) == 4  # 四舍五入


# ======================================================================
# repr 测试
# ======================================================================

class TestRepr:
    """测试对象的字符串表示。"""

    def test_repr_contains_key_info(self) -> None:
        """repr 应包含精度、历史开关和历史条数。"""
        calc = Calculator(precision=3, enable_history=True)
        calc.add(1, 2)
        repr_str = repr(calc)
        assert "precision=3" in repr_str
        assert "enable_history=True" in repr_str
        assert "history_count=1" in repr_str
