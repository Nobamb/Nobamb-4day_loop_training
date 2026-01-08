# ### A-02. 생성자로 속성 초기화

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

# ```

# **출력**

# ```python
# print(Person)

# ```

# **실행 결과**

# ```
# <class '__main__.Person'>

# ```


# Person 클래스 생성
# 생성자 포함

class Person:
    # 생성자
    # name, age 받음
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# Person 출력
print(Person)