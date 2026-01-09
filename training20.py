# ### C-05. 전체 조회 메서드 (Read)

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

#     def add(self, name, age):
#         person = Person(name, age)
#         self.members.append(person)

#     def read_all(self):
#         for idx, member in enumerate(self.members):
#             print(idx, member.name, member.age)

# ```

# **출력**

# ```python
# manager = PersonManager()
# manager.add("공욱재", 26)
# manager.add("공미남", 27)
# manager.add("공추남", 28)
# manager.read_all()

# ```

# **실행 결과**

# ```
# 0 공욱재 26
# 1 공미남 27
# 2 공추남 28

# ```


# Person 클래스 생성
# name, age 생성자 받음
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        

# PersonManage 클래스 생성
class PersonManage:
    # 생성자 manage는 빈 배열
    def __init__(self):
        self.manage = []
        
    # add(배열에 person값 추가)
    def add(self, name, age):
        person = Person(name, age)
        # 배열추가
        self.manage.append(person)
        
    # 읽기
    # 인덱스, 이름 나이
    def read_all(self):
        for idx, member in enumerate(self.manage):
            print(idx, member.name, member.age)
            
            
# 생성
member = PersonManage()
# 생성자에 값 추가
member.add("공욱재",26)
member.add("공미남",27)
member.add("공추남",28)

# read_all실행
member.read_all()