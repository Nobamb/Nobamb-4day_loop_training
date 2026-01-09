# ### A-06. 여러 인스턴스 생성

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

# person1 = Person("공욱재", 26)
# person2 = Person("공미남", 27)
# person3 = Person("공추남", 28)

# ```

# **출력**

# ```python
# print(person1.name)
# print(person2.name)
# print(person3.name)

# ```

# **실행 결과**

# ```
# 공욱재
# 공미남
# 공추남

# ```


# Person 클래스 생성
# name, age 받음
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
# 공욱재 공미남 공추남 받음
person1 = Person("공욱재",26)
person2 = Person("공미남",27)
person3 = Person("공추남",28)

# 출력
# 이름만
print(person1.name)
print(person2.name)
print(person3.name)
