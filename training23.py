# ### C-08. 수정 메서드 (Update)

# **입력**

# ```python
# idx = int(input())
# new_age = int(input())

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

#     def update(self, idx, new_age):
#         self.members[idx].age = new_age

#     def read_all(self):
#         for idx, member in enumerate(self.members):
#             print(idx, member.name, member.age)

# ```

# **출력**

# ```python
# manager = PersonManager()
# manager.add("공욱재", 26)
# manager.add("공미남", 27)
# manager.update(idx, new_age)
# manager.read_all()

# ```

# **실행 결과** (0, 30 입력 시)

# ```
# 0 공욱재 30
# 1 공미남 27

# ```



# 이름 나이 받음
idx = int(input("인덱스"))
new_age= int(input("나이"))




# Person 클래스 생성
# name, age 생성자 받음

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
# PersonManager 클래스생성
class PersonManager:
    # 배열 생성자 생성
    def __init__(self):
        self.manage = []
        
        
    # add 메서드 생성
    # 배열에 값 추가
    def add(self,name,age):
        # person 생성
        person = Person(name, age)
        # 배열에 값 추가
        self.manage.append(person)
    
    # update메서드
    # 나이 변경
    # 인덱스, 새 나이 받음
    def update(self, idx, new_age):
        # 특정 인덱스의 age를 변경
        self.manage[idx].age = new_age
        
    # read_all메서드
    # 인덱스, 이름, 나이 출력
    def read_all(self):
        for idx,member in enumerate(self.manage):
            print(idx, member.name, member.age)
            
            
# PersonManager 생성

manager = PersonManager()

# 추가
manager.add("공욱재", 26)
manager.add("공미남", 27)

# 나이 업데이트
manager.update(idx, new_age)

# read_all 메소드 실행
manager.read_all()