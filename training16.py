# ## 섹션 C. 데이터 클래스와 관리 클래스 분리

# ### C-01. 데이터 클래스 정의 (Person)

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

#     def __str__(self):
#         return self.name + " " + str(self.age)

# ```

# **출력**

# ```python
# person = Person("공욱재", 26)
# print(person)

# ```

# **실행 결과**

# ```
# 공욱재 26

# ```


# Person 클래스 생성
# name, age 생성자로 받음
# __str__
# name, age를 출력
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # str
    # name, age 반환
    def __str__(self):
        return self.name + " " + str(self.age)
    
    
# person 생성
person = Person("공욱재", 26)
# person 출력
print(person)