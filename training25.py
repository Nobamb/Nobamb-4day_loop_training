# ### C-10. 개수 반환 메서드

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

#     def get_count(self):
#         return len(self.members)

# ```

# **출력**

# ```python
# manager = PersonManager()
# manager.add("공욱재", 26)
# manager.add("공미남", 27)
# print(manager.get_count())

# ```

# **실행 결과**

# ```
# 2

# ```



# Person 클래스 생성
# name, age 받음
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
# PersonManager 클래스 생성
class PersonManager:
    def __init__(self):
        self.manage = []
        
    # add 메서드 생성
    # 배열에 person 추가
    def add(self, name, age):
        # person 생성
        person = Person(name, age)
        # person 추가
        self.manage.append(person)

    # 개수 받아오기
    def get_count(self):
        return len(self.manage)

            
# PersonManager 생성
manager = PersonManager()

# 추가
manager.add("공욱재", 26)
manager.add("공미남", 27)

# 개수 반환
count = manager.get_count()
# 개수 출력
print(count)