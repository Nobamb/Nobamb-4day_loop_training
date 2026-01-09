# ### C-06. 단건 조회 메서드 - 인덱스 (Read)

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

#     def read_by_index(self, idx):
#         return self.members[idx]

# ```

# **출력**

# ```python
# manager = PersonManager()
# manager.add("공욱재", 26)
# manager.add("공미남", 27)
# result = manager.read_by_index(idx)
# print(result.name, result.age)

# ```

# **실행 결과** (1 입력 시)

# ```
# 공미남 27

# ```

# index값 받음
idx = int(input())



# Person 클래스 생성
# name, age 생성자 받음

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# PersonManage 클래스 생성
class PersonManage:
    # manage빈배열 생성자
    def __init__(self):
        self.manage = []
        
    # 배열 추가
    # name, age를 통해
    # person 생성
    def add(self, name, age):
        person = Person(name, age)
        # 배열에 person추가
        self.manage.append(person)
        
    # 인덱스 받아서 출력
    def read_by_index(self, idx):
        # idx에 해당하는 배열값 반환
        return self.manage[idx]
    
    
# PersonManage 생성자 생성
manager = PersonManage()
# 추가 

manager.add("공욱재", 26)
manager.add("공미남", 27)


# 실행
person = manager.read_by_index(idx)
# 출력
print(person.name, person.age)