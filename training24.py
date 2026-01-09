# ### C-09. 삭제 메서드 (Delete)

# **입력**

# ```python
# idx = int(input())

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

#     def delete(self, idx):
#         self.members.pop(idx)

#     def read_all(self):
#         for idx, member in enumerate(self.members):
#             print(idx, member.name, member.age)

# ```

# **출력**

# ```python
# manager = PersonManager()
# manager.add("공욱재", 26)
# manager.add("공미남", 27)
# manager.add("공추남", 28)
# manager.delete(idx)
# manager.read_all()

# ```

# **실행 결과** (1 입력 시)

# ```
# 0 공욱재 26
# 1 공추남 28

# ```