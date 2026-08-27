import json
import os
from students import save_students,load_students
# 把主程序的 load_students,save_students 复制过来，或者import导入

def test_case():
    # 准备测试数据
    test_data = {
        "001":{"name":"张三","score":88},
        "002":{"name":"李四","score":76}
    }
    save_students(test_data)
    loaded = load_students()
    assert loaded["001"]["name"] == "张三"
    assert loaded["001"]["score"] == 88
    print("持久化读写测试通过")

    score_list = [v["score"] for v in loaded.values()]
    assert max(score_list) == 88
    assert min(score_list) ==76
    print("统计计算测试通过")

    #清理测试文件
    if os.path.exists("students.json"):
        os.remove("students.json")
    print("全部单元测试完成")

if __name__ == "__main__":
    test_case()
