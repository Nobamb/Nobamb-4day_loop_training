# ### B-02. self로 속성 접근하는 메서드

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

#     def show_name(self):
#         print(self.name)

# person = Person("공욱재", 26)

# ```

# **출력**

# ```python
# person.show_name()

# ```

# **실행 결과**

# ```
# 공욱재

# ```


# Person class 생성
# name, age받음
# show_name 메서드 추가
# self.name 출력

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # 메서드 show_name
    def show_name(self):
        print(self.name)

# Person 생성
person = Person("공욱재",26)
# 메서드 실행
person.show_name()