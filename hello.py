students = []


def add_student():
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
    print("添加成功")


def show_students():
    if not students:
        print("暂无学生记录")
        return

    for number, student in enumerate(students, start=1):
        print(f"{number}. {student['name']}：{student['score']:.1f} 分")


def find_student():
    name = input("请输入要查询的姓名：").strip()
    results = [student for student in students if student["name"] == name]

    if not results:
        print("没有找到该学生")
        return

    for student in results:
        print(f"{student['name']}：{student['score']:.1f} 分")


def show_average():
    if not students:
        print("暂无学生记录")
        return

    average = sum(student["score"] for student in students) / len(students)
    print(f"平均成绩：{average:.1f} 分")

def remove_student():
    name = input("请输入要删除的学生姓名：").strip()
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print(f"已删除学生：{name}")
            return

    print(f"没有找到学生：{name}")

def modify_score():
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
            print(f"{name} 的成绩已更新为 {new_score:.1f} 分")
            return

    print(f"没有找到学生：{name}")     
        

def main():
    while True:
        print("\n===== 学生成绩管理系统 =====")
        print("1. 添加学生")
        print("2. 查看全部学生")
        print("3. 查询学生")
        print("4. 查看平均成绩")
        print("5. 删除学生")
        print("6. 修改成绩")
        print("0. 退出")

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
        elif choice == "0":
            print("程序已退出")
            break
        else:
            print("选择无效，请重新输入")


if __name__ == "__main__":
    main()