# ### B-07. 메서드 내에서 다른 메서드 호출

# **입력**

# ```
# 없음

# ```

# **처리**

# ```python
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_info(self):
#         return self.name + " " + str(self.age)

#     def display(self):
#         info = self.get_info()
#         print(info)

# person = Person("공욱재", 26)

# ```

# **출력**

# ```python
# person.display()

# ```

# **실행 결과**

# ```
# 공욱재 26

# ```


