# define a class
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        return f'My name is {self.name}, and I am {self.age} years old.'

Tom = Student('Tom',18)
print(Tom.name,Tom.age,Tom.introduce())





# revise the attribution of the objects in class
class StudentGrades:
    def __init__(self,name,philology,math):
        self.name = name
        self.philology = philology
        self.math = math
    def update(self,course,grade):
        if course == 'philology':
            self.philology = grade
        elif course == 'math':
            self.math = grade
Tom = StudentGrades('tom',88,99)

# revise the value
Tom.math = 89
print(Tom.math,Tom.philology)




# object can in the list and dictionary
tom = StudentGrades('tom',88,99)
amy = StudentGrades('amy',87,93)
alex = StudentGrades('alex',88,90)
student_list = [tom,amy,alex]
for student in student_list:
    print(student.name,student.philology,student.math)

student_dict = {'tom':tom,
                'amy':amy,
                'alex':alex
                }
for name,student in student_dict.items():
    print(f'The grade of {name} is {student.philology},{student.math}')


class Car:
    def __init__(self,model,price):
        self.model = model
        self.price = price

    def info(self):
        print(f'车型是{self.model},价格是{self.price}万元')





# class exercise

class gasolineCar(Car):
    def __init__(self,model,price,box_size):
        super().__init__(model,price)
        self.box_size = box_size

    def add_gasoline(self,money):
        print(f'add gasoline at {money}')
    def info(self):
        super().info()
        print('i am more powerful due to the use of gasoline')
car01 = gasolineCar('car1',60,50)
print(car01.model,car01.price,car01.box_size)
car01.info()
car01.add_gasoline(200)


class ElectricCar(Car):
    def __init__(self,model,price,battery_size):
        super().__init__(model,price)
        self.battery_size = battery_size

    def add_electric(self,money):
        print(f'The price of car is {self.price},it charged $ {money} ')
    def info(self):
        super().info()
        print(' i am electric car so i am more saving')

car02 = ElectricCar('car2',200,100)
print(car02.model,car02.price,car02.battery_size)
car02.info()
car02.add_electric(90)

