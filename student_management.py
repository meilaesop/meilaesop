import json
import csv
from pypinyin import lazy_pinyin

students = []
DATA_FILE = "students.json"


def load_students():
    """从 JSON 文件中读取学生数据。"""
    global students
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                students = data
                print("已加载学生数据")
            else:
                students = []
    except FileNotFoundError:
        students = []
    except json.JSONDecodeError:
        print("数据文件格式错误，已重置为空列表")
        students = []


def save_students():
    """把学生数据保存到 JSON 文件中。"""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=2)
    print("数据已保存到 students.json")


def export_report():
    """把学生成绩导出为 CSV 成绩单。"""
    if not students:
        print("暂无学生记录，无法导出")
        return

    with open("成绩单.csv", "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["姓名", "成绩"])
        for student in students:
            writer.writerow([student["name"], student["score"]])

    print("成绩单已导出到 成绩单.csv")


def add_student():
    """添加学生：输入姓名和成绩，并保存到列表。"""
    name = input("请输入学生姓名：").strip()
    if not name:
        print("姓名不能为空")
        return

    try:
        score = float(input("请输入学生成绩："))
    except ValueError:
        print("成绩必须是数字")
        return

    if score < 0 or score > 100:
        print("成绩必须在 0 到 100 之间")
        return

    students.append({"name": name, "score": score})
    save_students()
    print("添加成功")


def show_students():
    """展示全部学生信息。"""
    if not students:
        print("暂无学生记录")
        return

    print("\n===== 学生列表 =====")
    for number, student in enumerate(students, start=1):
        print(f"{number}. {student['name']}：{student['score']:.1f} 分")


def find_student():
    """按姓名查询学生信息。"""
    name = input("请输入要查询的姓名：").strip()
    results = [student for student in students if student["name"] == name]

    if not results:
        print("没有找到该学生")
        return

    print("\n===== 查询结果 =====")
    for student in results:
        print(f"{student['name']}：{student['score']:.1f} 分")


def show_average():
    """计算并显示平均成绩。"""
    if not students:
        print("暂无学生记录")
        return

    average = sum(student["score"] for student in students) / len(students)
    print(f"平均成绩：{average:.1f} 分")


def sort_students_by_score():
    """按成绩从高到低排序并输出。"""
    if not students:
        print("暂无学生记录")
        return

    sorted_students = sorted(students, key=lambda student: student["score"], reverse=True)
    print("\n===== 按成绩排序 =====")
    for number, student in enumerate(sorted_students, start=1):
        print(f"{number}. {student['name']}：{student['score']:.1f} 分")


def sort_students_by_name():
    """按姓名拼音顺序排序并输出。"""
    if not students:
        print("暂无学生记录")
        return

    sorted_students = sorted(students, key=lambda student: lazy_pinyin(student["name"]))
    print("\n===== 按姓名排序 =====")
    for number, student in enumerate(sorted_students, start=1):
        print(f"{number}. {student['name']}：{student['score']:.1f} 分")


def show_student_statistics():
    """统计学生人数、最高分和最低分。"""
    if not students:
        print("暂无学生记录")
        return

    highest_student = max(students, key=lambda student: student["score"])
    lowest_student = min(students, key=lambda student: student["score"])
    print("\n===== 成绩统计 =====")
    print(f"学生总人数：{len(students)} 人")
    print(f"最高分：{highest_student['name']}，{highest_student['score']:.1f} 分")
    print(f"最低分：{lowest_student['name']}，{lowest_student['score']:.1f} 分")


def remove_student():
    """根据姓名删除学生，并保存更新后的数据。"""
    name = input("请输入要删除的学生姓名：").strip()
    for student in students:
        if student["name"] == name:
            students.remove(student)
            save_students()
            print(f"已删除学生：{name}")
            return

    print(f"没有找到学生：{name}")


def modify_score():
    """根据姓名修改学生成绩，并保存到文件。"""
    name = input("请输入要修改成绩的学生姓名：").strip()
    for student in students:
        if student["name"] == name:
            try:
                new_score = float(input(f"请输入 {name} 的新成绩："))
            except ValueError:
                print("成绩必须是数字")
                return

            if new_score < 0 or new_score > 100:
                print("成绩必须在 0 到 100 之间")
                return

            student["score"] = new_score
            save_students()
            print(f"{name} 的成绩已更新为 {new_score:.1f} 分")
            return

    print(f"没有找到学生：{name}")


def show_menu():
    """显示主菜单。"""
    print("\n===== 学生成绩管理系统 =====")
    print("1. 添加学生")
    print("2. 查看全部学生")
    print("3. 查询学生")
    print("4. 查看平均成绩")
    print("5. 删除学生")
    print("6. 修改成绩")
    print("7. 保存到文件")
    print("8. 按成绩排序")
    print("9. 按姓名排序")
    print("10. 查看成绩统计")
    print("11. 导出成绩单")
    print("0. 退出")


def main():
    """程序主入口。"""
    load_students()

    while True:
        show_menu()
        choice = input("请选择功能：").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            find_student()
        elif choice == "4":
            show_average()
        elif choice == "5":
            remove_student()
        elif choice == "6":
            modify_score()
        elif choice == "7":
            save_students()
        elif choice == "8":
            sort_students_by_score()
        elif choice == "9":
            sort_students_by_name()
        elif choice == "10":
            show_student_statistics()
        elif choice == "11":
            export_report()
        elif choice == "0":
            print("程序已退出")
            break
        else:
            print("选择无效，请重新输入")


if __name__ == "__main__":
    main()
