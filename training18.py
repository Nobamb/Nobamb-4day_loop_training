# ### C-03. 관리 클래스에 리스트 속성

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
#     def __init__(self):
#         self.members = []

# ```

# **출력**

# ```python
# manager = PersonManager()
# print(manager.members)

# ```

# **실행 결과**

# ```
# []

# ```


# Person 클래스 생성
# name, age
class Person:
    def __init__(self, name, age):
        self.name =name
        self.age =age
        

# PersonManage 클래스 생성
# 생성자는 배열
class PersonManage:
    def __init__(self):
        self.manage = []
        
        
# PersonManage 클래스 받음
manager = PersonManage()

# 출력
print(manager.manage)