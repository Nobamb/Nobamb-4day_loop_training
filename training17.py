# ### C-02. 관리 클래스 정의 (PersonManager)

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

# class PersonManager:
#     pass

# ```

# **출력**

# ```python
# manager = PersonManager()
# print(manager)

# ```

# **실행 결과**

# ```
# <__main__.PersonManager object at 0x...>

# ```


# Person 클래스 생성
# name, age 받음
# PersonManage 클래스 생성
# pass함
class Preson:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

class PersonManage:
    pass


# PersonManage 생성자 생성
manage = PersonManage()

# 출력
print(manage)