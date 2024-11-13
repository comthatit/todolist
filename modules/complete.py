from modules.add import todo_list

def complete_task():
    task_num = int(input("완료할 할 일 번호를 입력하세요: ")) - 1
    if 0 <= task_num < len(todo_list):
        todo_list[task_num]["completed"] = True
        print(f"'{todo_list[task_num]['task']}'가 완료되었습니다.")
    else:
        print("올바르지 않은 번호입니다.")