# ### B-05. 속성 수정 메서드

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

#     def set_age(self, new_age):
#         self.age = new_age

# person = Person("공욱재", 26)
# person.set_age(30)

# ```

# **출력**

# ```python
# print(person.age)

# ```

# **실행 결과**

# ```
# 30

# ```




# Person 클래스 생성
# name, age 받음
# set_age를 통해 값 변경
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def set_age(self, new_age):
        # age의 값을 new_age로 변경
        self.age = new_age
        
# person 적용
person = Person("공욱재",26)

# person의 나이 변경
person.set_age(31)

# 출력
print(person.age)