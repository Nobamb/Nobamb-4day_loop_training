# ### C-07. 단건 조회 메서드 - 이름 검색 (Read)

# **입력**

# ```python
# keyword = input()

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

#     def read_by_name(self, keyword):
#         for member in self.members:
#             if member.name == keyword:
#                 return member
#         return None

# ```

# **출력**

# ```python
# manager = PersonManager()
# manager.add("공욱재", 26)
# manager.add("공미남", 27)
# result = manager.read_by_name(keyword)
# if result:
#     print(result.name, result.age)

# ```

# **실행 결과** (공미남 입력 시)

# ```
# 공미남 27

# ```