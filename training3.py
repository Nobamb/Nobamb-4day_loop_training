# ### A-03. 인스턴스 생성

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

# person = Person("공욱재", 26)

# ```

# **출력**

# ```python
# print(person)

# ```

# **실행 결과**

# ```
# <__main__.Person object at 0x...>

# ```



# Person 클래스 받음
# 생성자 name, age
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
# Person 지정(new x)
# name = 공욱재
# age = 26
person = Person("공욱재",26)

# 출력
print(person)