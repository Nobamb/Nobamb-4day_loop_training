# ### C-08. 수정 메서드 (Update)

# **입력**

# ```python
# idx = int(input())
# new_age = int(input())

# ```

# **처리**

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

#     def update(self, idx, new_age):
#         self.members[idx].age = new_age

#     def read_all(self):
#         for idx, member in enumerate(self.members):
#             print(idx, member.name, member.age)

# ```

# **출력**

# ```python
# manager = PersonManager()
# manager.add("공욱재", 26)
# manager.add("공미남", 27)
# manager.update(idx, new_age)
# manager.read_all()

# ```

# **실행 결과** (0, 30 입력 시)

# ```
# 0 공욱재 30
# 1 공미남 27

# ```