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