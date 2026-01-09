# ### C-07. 단건 조회 메서드 - 이름 검색 (Read)

# **입력**

# ```python
# keyword = input()

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

#     def read_by_name(self, keyword):
#         for member in self.members:
#             if member.name == keyword:
#                 return member
#         return None

# ```

# **출력**

# ```python
# manager = PersonManager()
# manager.add("공욱재", 26)
# manager.add("공미남", 27)
# result = manager.read_by_name(keyword)
# if result:
#     print(result.name, result.age)

# ```

# **실행 결과** (공미남 입력 시)

# ```
# 공미남 27

# ```

# 입력 받음
name = input("이름")


# Person 클래스 생성
# name, age 받음
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# PersonManage 클래스
class PersonManage:
    def __init__(self):
        # 배열
        self.manage = []
    # 배열에 값 추가
    def add(self, name, age):
        # person 생성
        person  = Person(name, age)
        # 배열에 값 추가
        self.manage.append(person)
        
    # 이름으로 값찾기
    def read_by_name(self, name):
        # manage 순회
        for member in self.manage:
            # 이름이 같으면
            if member.name == name:
                # 값 리턴
                return member
            
        # 없으면 none
        return None
    
# 생성자 생성
manager = PersonManage()

# 추가
manager.add("공욱재", 26)
manager.add("공미남", 27)

# 이름 찾기
result = manager.read_by_name(name)

# 값이 존해하면 출력
if result:
    print(result.name, result.age)