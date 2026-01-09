# ### B-04. 반환값 있는 메서드

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

#     def get_info(self):
#         return self.name + " " + str(self.age)

# person = Person("공욱재", 26)
# info = person.get_info()

# ```

# **출력**

# ```python
# print(info)

# ```

# **실행 결과**

# ```
# 공욱재 26

# ```


# Person 클래스 생성
# name, age 받음
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    # return 메서드
    def get_info(self):
        return self.name + " " + str(self.age)
    
    
# person 생성
person = Person("공욱재",26)

# 메서드 실행 값 저장
info = person.get_info()

# 출력
print(info)