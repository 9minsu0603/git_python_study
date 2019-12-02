import json
import os

"""
student = [
    {
        'no': 1,
        'name': '김승영',
        'score': {'국어': 90, '영어': 90, '수학': 90}
    },
    {
        'no': 2,
        'name': '지재삼',
        'score': {'국어': 80, '영어': 79, '수학': 69}
    }
]
"""
file_name = 'json_student_data.txt'


def std_list_read_file():
    if os.path.isfile(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:  # json 형태의 파일 load
            x = json.load(f)
            return json.loads(x)
    else:
        return [
            {
                'no': 1,
                'name': '김승영',
                'score': {'국어': 90, '영어': 90, '수학': 90}
            },
            {
                'no': 2,
                'name': '지재삼',
                'score': {'국어': 80, '영어': 79, '수학': 69}
            }
        ]


def show_menu():
    try:
        return int(input("1. 학생목록, 2. 학생 추가, 3. 학생 수정, 4. 학생 삭제, 5. 종료 [1-5] 번호를 입력하세요."))
    except ValueError as e:
        print("숫자 [1-5]값만 가능")
        exit(0)


def show_std_list(students):
    pass


def std_list_write_file(students):
    json_student = json.dumps(students, ensure_ascii=False)
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(json_student, f, ensure_ascii=False)


def add_std_info(students):
    pass


def get_std_info(msg):
    pass


def update_std_info(students):
    pass


def delete_std_info(students):
   pass


if __name__ == "__main__":
    students = std_list_read_file()
    while True:
        res = show_menu()
        if res == 1:
            show_std_list(students)
        elif res == 2:
            add_std_info(students)
        elif res == 3:
            update_std_info(students)
        elif res == 4:
            delete_std_info(students)
        else:
            std_list_write_file(students)
            break;
    print("프로그램 종료")