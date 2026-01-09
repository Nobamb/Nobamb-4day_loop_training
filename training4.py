# ### A-04. 인스턴스 속성 접근

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
# print(person.name)
# print(person.age)

# ```

# **실행 결과**

# ```
# 공욱재
# 26

# ```



# class 선언
# Person 클래스, name, age 받음
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
# person 받음
# 공욱재, 26
person = Person("공욱재",26)

# 하나씩 출력
# 이름
print(person.name)
# 나이
print(person.age)