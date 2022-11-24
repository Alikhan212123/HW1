class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Я {self.fullname}. Мне {self.age} лет. Женат ли я? - {self.is_married}")


about_me = Person("Abdykadyrov Syimyk", 17, False)
about_me.introduce_myself()


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        Person.__init__(self, fullname, age, is_married)
        self.marks = marks
        marks = {"History": 5, "math": 3, "geography": 5, "biology": 5}
        
        def asn(self):
            a = 0
            b = 0
            for i in self.marks.values():
                a += i
                b += 1
                print(b / a)

#     "Simon": {
#         "history": 5,
#         "maths": 3,
#         "geography": 5,
#         "biology": 4,
#         "chemistry": 2,
#     } ,
#     "Mura": {
#         "history": 5,
#         "maths": 2,
#         "geography": 5,
#         "biology": 5,
#         "chemistry": 2,
#     }, 
#     "Ulan": {
#         "history": 4,
#         "maths": 5,
#         "geography": 3,
#         "biology": 4,
#         "chemistry": 5,
#     } 
# }
       
    






class Teacher(Person):
    salary = 30000
    def __init__(self, fullname, age, is_married, experience):
        Person.__init__(self, fullname, age, is_married)
        self.experience = experience

    def zarplata(self):
        if self.experience > 3:
            self.salary += self.salary * 0.05
        print(self.salary)



            

klassuha = Teacher("Nailya Vaginurovna", 67, True, 20)
klassuha.zarplata()
klassuha.introduce_myself()








def create_students():
    res = []
    for i in range(3):
        a = Student("Abdykadyrov", 12, True)
        res.append(a)
    return res


