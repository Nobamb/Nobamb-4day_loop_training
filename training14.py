# ### B-07. 메서드 내에서 다른 메서드 호출

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

#     def display(self):
#         info = self.get_info()
#         print(info)

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


# 클래스 Person 생성
# name, age 생성자 받음
# get_info = name, age 반환
# display = get_info 값 출력

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # 값 반환
    def get_info(self):
        return self.name + " " + str(self.age)
    
    # 값 출력
    def display(self):
        info = self.get_info()
        print(info)
        
        
# person 생성
person = Person("공욱재",26)

# 실행
person.display()