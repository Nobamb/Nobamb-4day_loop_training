# ### A-07. 인스턴스를 리스트에 저장

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

# members = []
# members.append(Person("공욱재", 26))
# members.append(Person("공미남", 27))
# members.append(Person("공추남", 28))

# ```

# **출력**

# ```python
# for member in members:
#     print(member.name, member.age)

# ```

# **실행 결과**

# ```
# 공욱재 26
# 공미남 27
# 공추남 28

# ```


# Person 생성
# name, age 받음
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# 배열 지정
members = []

# members 배열에 person 추가
members.append(Person("공욱재",26))
members.append(Person("공미남",27))
members.append(Person("공추남",28))

# members 전부 출력
# name, age모두
for member in members:
    print(member.name, member.age)