"""Python 调试技巧综合示例。

本脚本演示以下调试手段：
1. logging 模块：替代 print，分级输出，可写入文件
2. breakpoint() / pdb：交互式调试器
3. assert 断言：开发期防御性检查
4. 异常追踪：traceback 模块定位错误
5. 性能调试：time / cProfile 计时

运行方式：
    python examples/debugging_demo.py
"""

from __future__ import annotations

import logging
import sys
import time
import traceback
from pathlib import Path

# 将 src 目录加入 sys.path，使脚本可直接运行
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from calculator import Calculator, OperationError  # noqa: E402


# ======================================================================
# 1. logging 配置
# ======================================================================

def setup_logging(level: int = logging.DEBUG) -> None:
    """配置日志系统：同时输出到控制台和文件。

    日志级别从低到高：DEBUG < INFO < WARNING < ERROR < CRITICAL
    生产环境通常设为 INFO 或 WARNING，开发环境设为 DEBUG。
    """
    log_format = (
        "%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s"
    )
    logging.basicConfig(
        level=level,
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout),  # 控制台输出
            logging.FileHandler("debug_demo.log", mode="w", encoding="utf-8"),
        ],
    )


logger = logging.getLogger(__name__)


# ======================================================================
# 2. 断言（assert）示例
# ======================================================================

def calculate_discount(price: float, discount_rate: float) -> float:
    """计算折扣价。

    使用 assert 在开发期验证输入合法性。
    注意：assert 在 Python 以 -O 优化模式运行时会被移除，
    因此不能用于运行时的业务校验（业务校验应使用 if + raise）。
    """
    # 开发期断言：价格必须为正
    assert price > 0, f"价格必须大于 0，当前为 {price}"
    # 折扣率必须在 0~1 之间
    assert 0 <= discount_rate <= 1, f"折扣率必须在 0~1 之间，当前为 {discount_rate}"

    discounted = price * (1 - discount_rate)
    logger.debug("折扣计算: price=%.2f, rate=%.2f -> %.2f", price, discount_rate, discounted)
    return discounted


# ======================================================================
# 3. pdb 交互式调试示例
# ======================================================================

def demo_pdb_debugging() -> None:
    """演示如何使用 breakpoint() 进入交互式调试。

    取消下方 breakpoint() 的注释即可体验。
    进入 pdb 后常用命令：
        n (next)      执行下一行
        s (step)      进入函数
        c (continue)  继续执行
        p <expr>      打印表达式值
        l (list)      查看当前代码
        w (where)     查看调用栈
        q (quit)      退出调试器
    """
    calc = Calculator(precision=2, enable_history=True)

    numbers = [10, 20, 30]
    total = 0
    for n in numbers:
        # 👇 取消注释以下行，程序运行到此处会自动进入 pdb 调试器
        # breakpoint()
        total = calc.add(total, n)
        logger.info("累加 %d 后 total = %s", n, total)

    logger.info("最终累加结果: %s", total)


# ======================================================================
# 4. 异常追踪（traceback）示例
# ======================================================================

def demo_exception_traceback() -> None:
    """演示如何捕获异常并打印完整调用栈。"""
    calc = Calculator()

    try:
        # 故意触发除零错误
        calc.divide(10, 0)
    except OperationError as e:
        logger.error("捕获到运算错误: %s", e)
        # 打印完整异常追踪（包含调用栈）
        logger.debug("完整异常追踪:\n%s", traceback.format_exc())
    except Exception:
        # 兜底：捕获所有未预期异常，打印完整栈后重新抛出
        logger.critical("未预期的异常:\n%s", traceback.format_exc())
        raise


# ======================================================================
# 5. 性能调试：计时与 cProfile
# ======================================================================

def demo_performance_timing() -> None:
    """演示使用 time.perf_counter() 进行精确计时。"""
    calc = Calculator(precision=6)

    start = time.perf_counter()

    # 执行大量运算
    results = []
    for i in range(1, 1001):
        results.append(calc.power(i, 2))

    elapsed = time.perf_counter() - start
    logger.info("1000 次幂运算耗时: %.4f 秒", elapsed)
    logger.info("前 5 个结果: %s", results[:5])


def demo_cprofile() -> None:
    """演示使用 cProfile 进行函数级性能分析。

    cProfile 会统计每个函数的调用次数和耗时，帮助定位性能瓶颈。
    """
    import cProfile
    import pstats
    from io import StringIO

    calc = Calculator(precision=6)

    def heavy_computation() -> None:
        for i in range(1, 500):
            calc.add(i, i * 0.5)
            calc.multiply(i, 1.1)

    profiler = cProfile.Profile()
    profiler.enable()
    heavy_computation()
    profiler.disable()

    # 将统计结果输出为字符串
    stream = StringIO()
    stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")
    stats.print_stats(10)  # 只显示耗时最长的前 10 个函数
    logger.info("cProfile 性能分析（前 10 名）:\n%s", stream.getvalue())


# ======================================================================
# 主函数
# ======================================================================

def main() -> None:
    """运行所有调试示例。"""
    setup_logging(level=logging.DEBUG)

    logger.info("=" * 60)
    logger.info("Python 调试技巧演示开始")
    logger.info("=" * 60)

    # 1. 断言示例
    logger.info("\n--- 1. 断言（assert）示例 ---")
    print(f"折扣价: {calculate_discount(100, 0.2)}")  # 应为 80.0

    # 2. pdb 调试示例
    logger.info("\n--- 2. pdb 交互式调试示例 ---")
    demo_pdb_debugging()

    # 3. 异常追踪示例
    logger.info("\n--- 3. 异常追踪示例 ---")
    demo_exception_traceback()

    # 4. 性能计时示例
    logger.info("\n--- 4. 性能计时示例 ---")
    demo_performance_timing()

    # 5. cProfile 示例
    logger.info("\n--- 5. cProfile 性能分析示例 ---")
    demo_cprofile()

    logger.info("\n" + "=" * 60)
    logger.info("所有调试示例运行完毕，日志已写入 debug_demo.log")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
