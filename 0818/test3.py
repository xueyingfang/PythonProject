# ============================================================
# 1. 自定义异常（重点：继承 Exception）
# ============================================================
class ScoreError(Exception):
    """成绩不合法时抛出"""
    pass


# ============================================================
# 2. 业务函数（重点：raise 主动抛出异常）
# ============================================================
def calc_grade(score):
    """根据分数返回等级"""
    if score < 0 or score > 100:
        raise ScoreError(f"分数 {score} 不在 0-100 范围内")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"


# ============================================================
# 3. 主程序（重点：try-except-else-finally 完整结构）
# ============================================================
def main():
    scores = []  # 存储录入的成绩

    print("=== 成绩录入工具 ===")
    print("输入分数后回车，输入 q 结束\n")

    while True:
        user_input = input("请输入成绩：").strip()

        if user_input.lower() == "q":
            break

        try:
            # 可能出错的代码
            score = float(user_input)  # 可能 ValueError
            grade = calc_grade(score)  # 可能 ScoreError
            result = 100 / (100 - score)  # 可能 ZeroDivisionError（刚好100分时）

        except ValueError:
            # 捕获：输入不是数字
            print("  ✗ 输入错误：请输入数字\n")

        except ScoreError as e:
            # 捕获：自定义异常，成绩超范围
            print(f"  ✗ 成绩错误：{e}\n")

        except ZeroDivisionError:
            # 捕获：除以零（刚好100分时触发，演示用）
            print("  ✗ 满分情况，特殊处理\n")
            grade = "A+"

        else:
            # 没有异常才执行
            scores.append(score)
            print(f"  ✓ 录入成功：{score} 分，等级 {grade}\n")

        finally:
            # 无论是否异常都执行（这里演示用，实际可用于清理资源）
            pass

    # ---------- 结束后保存到文件（重点：文件操作异常） ----------
    print(f"\n共录入 {len(scores)} 个成绩")
    if scores:
        print(f"平均分：{sum(scores) / len(scores):.2f}")

    try:
        with open("scores.txt", "w", encoding="utf-8") as f:
            for s in scores:
                f.write(f"{s}\n")
        print("成绩已保存到 scores.txt")
    except PermissionError:
        print("保存失败：没有文件写入权限")
    except OSError as e:
        print(f"保存失败：{e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序已退出")
