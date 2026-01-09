# ### A-05. 인스턴스 속성 수정

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
# person.name = "공미남"
# person.age = 27

# ```

# **출력**

# ```python
# print(person.name)
# print(person.age)

# ```

# **실행 결과**

# ```
# 공미남
# 27

# ```



# Person 클래스 생성

# name, age받음
class Person:
    def __init__(self, name, age):
        self.name =name
        self.age = age

# person받음, 공욱재 26
person = Person("공욱재",26)

# 변경
# 공미남 27

person.name = "공미남"
person.age = 27

# 출력
print(person.name)
print(person.age)