# ### C-09. 삭제 메서드 (Delete)

# **입력**

# ```python
# idx = int(input())

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

#     def delete(self, idx):
#         self.members.pop(idx)

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
# manager.delete(idx)
# manager.read_all()

# ```

# **실행 결과** (1 입력 시)

# ```
# 0 공욱재 26
# 1 공추남 28

# ```


# 인덱스 받기
idx = int(input("인덱스"))


# Person 클래스 생성
# name, age 생성자 받음
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
# PersonManager 클래스 생성
class PersonManager:
    def __init__(self):
        # 빈배열 manage 생성
        self.manage = []
        
    # add 메소드
    # manage에 person 추가
    def add(self, name, age):
        # person 생성
        person = Person(name, age)
        # 배열에 값 추가
        self.manage.append(person)
        
    # delete 추가
    def delete(self,idx):
        # manage의 idx번째 값 삭제
        self.manage.pop(idx)
        
    # read_all
    # name, age인덱스까지 모두 읽기
    def read_all(self):
        for idx, member in enumerate(self.manage):
            print(idx, member.name, member.age)
            
            
# PersonManager 생성
manager = PersonManager()

# 추가
manager.add("공욱재", 26)
manager.add("공미남", 27)
manager.add("공추남", 28)

# 삭제
manager.delete(idx)

# 출력
manager.read_all()