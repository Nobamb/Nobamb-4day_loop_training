# ### B-01. 매개변수 없는 메서드

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

#     def greet(self):
#         print("안녕하세요")

# person = Person("공욱재", 26)

# ```

# **출력**

# ```python
# person.greet()

# ```

# **실행 결과**

# ```
# 안녕하세요

# ```


# Person 클래스 생성
# name, age받음
# 매개변수 없는 greet 메서드 생성
# greet는 "안녕하세요"출력

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print("안녕하세요")
        
        
        
# Person 생성자 받음
person = Person("공욱재",26)

# 메서드 테스트
person.greet()