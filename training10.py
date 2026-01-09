# ### B-03. 매개변수 있는 메서드

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

#     def add_years(self, years):
#         print(self.age + years)

# person = Person("공욱재", 26)

# ```

# **출력**

# ```python
# person.add_years(5)

# ```

# **실행 결과**

# ```
# 31

# ```

# ---


# Person 클래스 생성
# name, age 받음

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # add_years 메서드 
    # year 받음
    # 출력
    def add_years(self, year):
        print(self.age + year)
        
        
# Person 받음
person = Person("공욱재",26)
# add_years 메서드 사용
person.add_years(5)