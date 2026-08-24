"""计算器包：演示 Python 调试、测试与代码规范最佳实践。"""

from calculator.core import Calculator, OperationError
from calculator.utils import format_result, parse_expression

__all__ = [
    "Calculator",
    "OperationError",
    "format_result",
    "parse_expression",
]

__version__ = "1.0.0"
