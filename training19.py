# ### C-04. 추가 메서드 (Create)

# **입력**

# ```python
# name = input()
# age = int(input())

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

#     def add(self, name, age):
#         person = Person(name, age)
#         self.members.append(person)

# ```

# **출력**

# ```python
# manager = PersonManager()
# manager.add(name, age)
# print(len(manager.members))

# ```

# **실행 결과** (공욱재, 26 입력 시)

# ```
# 1

# ```



# input받음
name = input("이름")
age = int(input("나이"))

# Person 클래스 생성
# name, age받음
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# PersonManage 클래스 생성
# member는 []
# add 메소드 추가
# person 클래스를 통해 배열에 추가

class PersonManage:
    def __init__(self):
        self.manage=[]
        
    def add(self, name, age):
        person = Person(name, age)
        # 추가
        self.manage.append(person)
        
# manager로 생성자
manager = PersonManage()
#  input 받은 값 적용
manager.add(name, age)

# 길이 확인
print(len(manager.manage))