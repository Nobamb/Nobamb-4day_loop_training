# ### C-11. 클래스 기반 CRUD 전체 조합

# **입력**

# ```python
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class PersonManager:
#     def __init__(self):
#         self.members = []

#     def add(self, name, age):
#         person = Person(name, age)
#         self.members.append(person)

#     def read_all(self):
#         for idx, member in enumerate(self.members):
#             print(idx, member.name, member.age)

#     def update(self, idx, new_age):
#         self.members[idx].age = new_age

#     def delete(self, idx):
#         self.members.pop(idx)

#     def get_count(self):
#         return len(self.members)

# def show_menu():
#     print("1. 추가")
#     print("2. 전체조회")
#     print("3. 수정")
#     print("4. 삭제")
#     print("5. 종료")

# ```

# **처리**

# ```python
# def main():
#     manager = PersonManager()
#     while True:
#         show_menu()
#         menu = input()
#         if menu == "1":
#             name = input()
#             age = int(input())
#             manager.add(name, age)
#         elif menu == "2":
#             manager.read_all()
#         elif menu == "3":
#             idx = int(input())
#             new_age = int(input())
#             manager.update(idx, new_age)
#         elif menu == "4":
#             idx = int(input())
#             manager.delete(idx)
#         elif menu == "5":
#             break

# ```

# **출력**

# ```python
# main()

# ```

# **실행 결과** (1, 공욱재, 26, 1, 공미남, 27, 2, 3, 0, 30, 2, 4, 1, 2, 5 순서로 입력 시)

# ```
# 1. 추가
# 2. 전체조회
# 3. 수정
# 4. 삭제
# 5. 종료
# 1. 추가
# 2. 전체조회
# 3. 수정
# 4. 삭제
# 5. 종료
# 1. 추가
# 2. 전체조회
# 3. 수정
# 4. 삭제
# 5. 종료
# 0 공욱재 26
# 1 공미남 27
# 1. 추가
# 2. 전체조회
# 3. 수정
# 4. 삭제
# 5. 종료
# 1. 추가
# 2. 전체조회
# 3. 수정
# 4. 삭제
# 5. 종료
# 0 공욱재 30
# 1 공미남 27
# 1. 추가
# 2. 전체조회
# 3. 수정
# 4. 삭제
# 5. 종료
# 1. 추가
# 2. 전체조회
# 3. 수정
# 4. 삭제
# 5. 종료
# 0 공욱재 30
# 1. 추가
# 2. 전체조회
# 3. 수정
# 4. 삭제
# 5. 종료

# ```



# Person 클래스 생성
# name, age 생성자
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
# PersonManager 클래스 생성
class PersonManager:
    
    def __init__(self):
        # 생성자로 배열받음
        self.manage = []
        
    # 추가(person 생성자를 배열에 추가)
    def add(self, name, age):
        # person 생성
        person = Person(name, age)
        # 배열에 값 추가
        self.manage.append(person)
        
    # 모두 읽기
    # manage에 대해 인덱스, 이름, 나이까지
    def read_all(self):
        for idx, member in enumerate(self.manage):
            print(idx, member.name, member.age)
            
    # update
    # 특정 인덱스의 나이 변경
    def update(self, idx, new_age):
        self.manage[idx].age = new_age
        
    # delete
    # 특정 인덱스의 값 제거
    def delete(self, idx):
        # manage의 특정 인덱스의 값 삭제
        self.manage.pop(idx)
        
    # get_count
    # 개수를 반환
    def get_count(self):
        return len(self.manage)
    
    
    
# PersonManger 생성
manager = PersonManager()