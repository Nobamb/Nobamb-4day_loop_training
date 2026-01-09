# ---

# ### B-06. 정보 출력 메서드

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

#     def display(self):
#         print(self.name, self.age)

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



# Person 클래스 생성
# name, age 생성자 받음
# display 메서드
# name, age 출력

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # 메서드 display
    def display(self):
        print(self.name, self.age)
        
        
# person 생성
person = Person("공욱재",26)
# 메소드 실행
person.display()