"""计算器核心逻辑模块。

本模块演示以下代码规范要点：
- 完整的类型注解（type hints）
- Google 风格文档字符串（docstring）
- 自定义异常类
- 日志记录（logging）替代 print 调试
- 常量大写命名、私有成员下划线前缀
"""

from __future__ import annotations

import logging

# 模块级日志器：命名应使用 __name__，便于按模块过滤日志
logger = logging.getLogger(__name__)

# 常量使用全大写下划线分隔
MAX_PRECISION = 10
SUPPORTED_OPERATORS = {"+", "-", "*", "/", "**", "%"}


class OperationError(Exception):
    """计算器运算错误。

    当运算过程中出现非法操作（如除零、不支持的运算符）时抛出。

    Attributes:
        expression: 触发错误的原始表达式字符串。
        message: 人类可读的错误描述。
    """

    def __init__(self, expression: str, message: str) -> None:
        self.expression = expression
        self.message = message
        super().__init__(f"[{expression}] {message}")


class Calculator:
    """支持基本四则运算与幂运算的计算器。

    所有运算方法均返回 float 或 int，精度由 precision 控制。

    Args:
        precision: 结果保留的小数位数，范围 0~10。
        enable_history: 是否记录运算历史。

    Raises:
        ValueError: precision 超出合法范围时抛出。

    Example:
        >>> calc = Calculator(precision=2)
        >>> calc.add(1.5, 2.3)
        3.8
    """

    def __init__(
        self,
        precision: int = 4,
        enable_history: bool = False,
    ) -> None:
        if not 0 <= precision <= MAX_PRECISION:
            raise ValueError(
                f"precision 必须在 0~{MAX_PRECISION} 之间，当前为 {precision}"
            )
        self.precision = precision
        self.enable_history = enable_history
        # 私有属性使用单下划线前缀
        self._history: list[str] = []

        logger.debug(
            "Calculator 初始化完成: precision=%d, enable_history=%s",
            precision,
            enable_history,
        )

    # ------------------------------------------------------------------
    # 基本运算
    # ------------------------------------------------------------------

    def add(self, a: float, b: float) -> float:
        """加法运算。

        Args:
            a: 第一个加数。
            b: 第二个加数。

        Returns:
            四舍五入到 precision 位的和。
        """
        result = self._round(a + b)
        self._record(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """减法运算（a - b）。"""
        result = self._round(a - b)
        self._record(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """乘法运算。"""
        result = self._round(a * b)
        self._record(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """除法运算（a / b）。

        Args:
            a: 被除数。
            b: 除数，不能为 0。

        Returns:
            四舍五入到 precision 位的商。

        Raises:
            OperationError: 除数为 0 时抛出。
        """
        if b == 0:
            logger.warning("除零尝试: %s / %s", a, b)
            raise OperationError(f"{a} / {b}", "除数不能为零")
        result = self._round(a / b)
        self._record(f"{a} / {b} = {result}")
        return result

    def power(self, base: float, exponent: float) -> float:
        """幂运算（base ** exponent）。

        Args:
            base: 底数。
            exponent: 指数。

        Returns:
            四舍五入到 precision 位的幂结果。
        """
        result = self._round(base ** exponent)
        self._record(f"{base} ** {exponent} = {result}")
        return result

    # ------------------------------------------------------------------
    # 复合运算
    # ------------------------------------------------------------------

    def evaluate(self, expression: str) -> float:
        """解析并计算简单的二元表达式字符串。

        支持格式："a op b"，op 为 + - * / ** % 之一。

        Args:
            expression: 形如 "3 + 4" 的表达式字符串。

        Returns:
            计算结果。

        Raises:
            OperationError: 表达式格式错误或运算符不支持时抛出。
        """
        logger.info("开始解析表达式: %r", expression)

        parts = expression.strip().split()
        if len(parts) != 3:
            raise OperationError(
                expression,
                f"表达式格式错误，应为 'a op b'，实际得到 {len(parts)} 段",
            )

        a_str, op, b_str = parts
        if op not in SUPPORTED_OPERATORS:
            raise OperationError(expression, f"不支持的运算符: {op}")

        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError as exc:
            raise OperationError(
                expression, f"无法解析为数字: {a_str!r} 或 {b_str!r}"
            ) from exc

        logger.debug("解析成功: a=%s, op=%s, b=%s", a, op, b)

        if op == "+":
            return self.add(a, b)
        if op == "-":
            return self.subtract(a, b)
        if op == "*":
            return self.multiply(a, b)
        if op == "/":
            return self.divide(a, b)
        if op == "**":
            return self.power(a, b)
        # op == "%"
        return self._round(a % b)

    # ------------------------------------------------------------------
    # 历史记录
    # ------------------------------------------------------------------

    @property
    def history(self) -> list[str]:
        """运算历史的只读副本。"""
        return list(self._history)

    def clear_history(self) -> None:
        """清空运算历史。"""
        self._history.clear()
        logger.debug("历史记录已清空")

    # ------------------------------------------------------------------
    # 内部辅助方法
    # ------------------------------------------------------------------

    def _round(self, value: float) -> float:
        """将结果四舍五入到指定精度。

        若结果为整数则返回 int 类型，避免 3.0 这类输出。
        """
        rounded = round(value, self.precision)
        if rounded == int(rounded):
            return int(rounded)
        return rounded

    def _record(self, entry: str) -> None:
        """记录一条运算历史（仅在 enable_history 为 True 时生效）。"""
        if self.enable_history:
            self._history.append(entry)
            logger.debug("已记录历史: %s", entry)

    def __repr__(self) -> str:
        """返回开发者友好的对象表示。"""
        return (
            f"Calculator(precision={self.precision!r}, "
            f"enable_history={self.enable_history!r}, "
            f"history_count={len(self._history)})"
        )
