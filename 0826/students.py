import json
import os

# 数据文件名称
DATA_FILE = "students.json"


def load_students():
    """从json文件加载学生数据，文件不存在返回空字典"""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        print("json文件损坏，已重置为空数据")
        return {}
    except Exception as e:
        print(f"读取文件异常：{e}")
        return {}


def save_students(students):
    """保存学生字典写入json文件"""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(students, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"保存文件失败：{e}")


def show_statistics(students):
    """统计：最高分、最低分、平均分"""
    if len(students) == 0:
        print("没有学生数据，无法统计")
        return
    score_list = [v["score"] for v in students.values()]
    max_score = max(score_list)
    min_score = min(score_list)
    avg_score = sum(score_list) / len(score_list)
    print("\n====成绩统计信息====")
    print(f"学生总人数：{len(students)}")
    print(f"最高分：{max_score}")
    print(f"最低分：{min_score}")
    print(f"平均分：{avg_score:.2f}")


def show_sort_by_score(students):
    """按成绩降序排序展示学生"""
    if len(students) == 0:
        print("当前没有学生数据")
        return
    # 把字典转列表，按成绩从高到低排序
    stu_list = sorted(students.items(), key=lambda item: item[1]["score"], reverse=True)
    print("\n====学生成绩排序(降序)====")
    for sid, info in stu_list:
        print(f"学号:{sid:6} | 姓名:{info['name']:8} | 成绩:{info['score']}")


def main():
    students = load_students()
    while True:
        print("\n===== 学生成绩管理系统 =====")
        print("1. 添加学生成绩")
        print("2. 删除学生")
        print("3. 修改学生成绩")
        print("4. 查询单个学生")
        print("5. 显示全部学生")
        print("6. 成绩统计(最高/最低/平均)")
        print("7. 按成绩排序展示")
        print("0. 退出系统")
        print("============================")

        choice = input("请输入功能编号：").strip()

        # 1 添加学生
        if choice == "1":
            try:
                sid = input("输入学生学号：").strip()
                if sid == "":
                    print("错误：学号不能为空！")
                    continue
                if sid in students:
                    print("该学号已经存在，不能重复添加！")
                    continue
                name = input("输入学生姓名：").strip()
                if name == "":
                    print("错误：姓名不能为空！")
                    continue
                score_input = input("输入学生成绩：")
                score = float(score_input)
                if not (0 <= score <= 100):
                    print("成绩范围必须0‑100！添加失败")
                    continue
                students[sid] = {"name": name, "score": score}
                save_students(students)
                print(f"添加成功：学号:{sid} 姓名:{name} 成绩:{score}")
            except ValueError:
                print("异常：成绩必须输入数字！")

        # 2 删除学生
        elif choice == "2":
            sid = input("请输入要删除学生学号：").strip()
            if sid in students:
                del students[sid]
                save_students(students)
                print(f"学号 {sid} 删除完成")
            else:
                print(f"错误：学号 {sid} 不存在！")

        #3 修改学生成绩
        elif choice == "3":
            sid = input("请输入要修改的学生学号：").strip()
            if sid not in students:
                print("该学号不存在！")
                continue
            try:
                new_score_input = input(f"当前学生：{students[sid]['name']}，请输入新成绩：")
                new_score = float(new_score_input)
                if not (0 <= new_score <= 100):
                    print("成绩必须0‑100，修改失败")
                    continue
                students[sid]["score"] = new_score
                save_students(students)
                print("成绩修改成功")
            except ValueError:
                print("异常：成绩必须输入数字！")

        #4 查询单个学生
        elif choice == "4":
            sid = input("输入要查询的学号：").strip()
            if sid in students:
                s = students[sid]
                print(f"学号:{sid} | 姓名:{s['name']} | 成绩:{s['score']}")
            else:
                print("未找到该学生")

        #5 全部展示
        elif choice == "5":
            if len(students) == 0:
                print("当前没有学生数据")
            else:
                print("\n---全部学生列表---")
                for k, v in students.items():
                    print(f"学号:{k:6} | 姓名:{v['name']:8} | 成绩:{v['score']}")

        #6 统计
        elif choice == "6":
            show_statistics(students)

        #7 按成绩排序
        elif choice == "7":
            show_sort_by_score(students)

        #0退出
        elif choice == "0":
            print("程序即将退出，再见！")
            break
        else:
            print("输入无效，请输入菜单上的数字0‑7！")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n检测到强制中断(Ctrl+C)，程序结束。")
    except Exception as e:
        print(f"\n发生未知异常：{e}")
