# ### B-08. 문자열 표현 메서드 (**str**)

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

# person = Person("공욱재", 26)

# ```

# **출력**

# ```python
# print(person)

# ```

# **실행 결과**

# ```
# 공욱재 26

# ```


# 클래스 Person 생성
# name, age 생성자 받음
# __str__
# name, age 출력
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # str
    # name, age 반환
    def __str__(self):
        return self.name + " "+str(self.age)
    
    
    
# person 생성
person =  Person("공욱재",26)

# person 출력
print(person)
