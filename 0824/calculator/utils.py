"""工具函数模块。

提供表达式解析、结果格式化等辅助功能。
演示函数式编程风格、类型注解与文档字符串规范。
"""

from __future__ import annotations

import re
from typing import Optional

# 预编译正则表达式：模块加载时编译一次，避免重复编译
# 匹配形如 "3.14 + 2.71" 的表达式，允许负数和科学计数法
_EXPRESSION_PATTERN = re.compile(
    r"""
    ^\s*
    (?P<a>-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)   # 第一个数字（含负号/小数/科学计数法）
    \s+
    (?P<op>\+|-|\*\*|\*|/|%)                     # 运算符
    \s+
    (?P<b>-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)    # 第二个数字
    \s*$
    """,
    re.VERBOSE,
)


def parse_expression(expression: str) -> Optional[tuple[float, str, float]]:
    """使用正则解析二元表达式字符串。

    Args:
        expression: 形如 "3 + 4" 的表达式字符串。

    Returns:
        解析成功返回 (a, op, b) 元组；格式不合法返回 None。

    Example:
        >>> parse_expression("2.5 * 3")
        (2.5, '*', 3.0)
        >>> parse_expression("invalid")
        None
    """
    match = _EXPRESSION_PATTERN.match(expression)
    if not match:
        return None
    return (
        float(match.group("a")),
        match.group("op"),
        float(match.group("b")),
    )


def format_result(
    value: float,
    *,
    precision: int = 4,
    with_thousands_sep: bool = False,
) -> str:
    """将数值格式化为人类可读的字符串。

    Args:
        value: 待格式化的数值。
        precision: 小数保留位数。
        with_thousands_sep: 是否添加千位分隔符。

    Returns:
        格式化后的字符串。

    Raises:
        ValueError: precision 为负数时抛出。

    Example:
        >>> format_result(1234567.89, precision=2, with_thousands_sep=True)
        '1,234,567.89'
    """
    if precision < 0:
        raise ValueError(f"precision 不能为负数，当前为 {precision}")

    if with_thousands_sep:
        return f"{value:,.{precision}f}"
    return f"{value:.{precision}f}"


def is_number(s: str) -> bool:
    """判断字符串是否可解析为数字（含整数、小数、科学计数法、负数）。

    Args:
        s: 待判断的字符串。

    Returns:
        可解析为数字返回 True，否则返回 False。
    """
    try:
        float(s)
        return True
    except ValueError:
        return False
