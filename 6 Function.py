# function

def print_hello():
    print('hello world')
    print('hello')
print_hello()


# function with parameter

def introduce(name): 
    print(f'my name is {name},I am a student')
introduce('Amy') 
introduce('Tom')  

# calculate numbers from 1-10
def sum_numbers(number):
    sum_value = 0 
    for i in range(1,number + 1): 
        sum_value += i  
    print('The sum is:',sum_value)
sum_numbers(10)


# multiple parameters in function 
def introduce(name,gender):
    print(f'My name is {name}, and I am a {gender}')
introduce('Tom','boy')

# default parameters in function
def introduce(name,gender,age = 6):  #其中年龄就是默认参数
    print(f'My name is {name}, and I am a {gender},my age is {age}')
introduce('Tom','boy')
# the default parameter can be changed if you set different parameter but if you dont set then the default one
introduce('Amy','girl',5) 



# the return value of function
def add(x,y):
    x = int(x)
    y = int(y)
    return x + y
result = add(7,8)  
print('The result is：',result)


# function which return a dictionary
students = {  #学生信息汇总
    'Tom' : {'id' : 101,'age' : 21,'height' : 189},
    'Amy' : {'id' : 102,'age' : 20,'height' : 178},
    'Alex' : {'id' : 103,'age' : 23,'height' : 190},
}

def get_student(name):  
    if name in students:
        return students[name]  
    else:
        return None

get_name = get_student('Tom')
print(get_name)


# function which return a list
total = {
    'fruit' : ['apple','banana','orange'],
    'animal' : ['cat','dog','monkey'],
}
def get_information(something):
    if something in total:
        return total[something]
    else:
        return None

get_something1 = get_information('fruit')
get_something2 = get_information('animal')
print(get_something1,get_something2)



# lambda function(user-defined function)
students_grades = [('Tom',89),('Amy',90),('Alex',78)] 
students_grades.sort(key = lambda x:x[1])
new_list = sorted(students_grades, key = lambda x:x[1], reverse = True)
print(students_grades)
print(new_list)



