# list for data storage
animals = ['cats','dogs','chickens']
print(animals)
print(type(animals))


# use index to find data
print(animals[0])
print(animals[-1])


new_list = ['apple','banana','grapes']
message = f'i want to eat {new_list[0]}'
print(message)


# you can add, delete and revise data in your list
new_list[0] = 'pear'
print(new_list)


new_list.append('oranges')
print(new_list)

new_list.remove('pear')
print(new_list)


# sort your list
grades = [11,89,45,67,87,34]
grades.sort()
print(grades)


grades.sort(reverse=True)
print(grades)


# use another way to sort list but not to revise list
grades1 = sorted(grades)
print(grades,grades1)
grades2 = sorted(grades,reverse=True)
print(grades,grades2)


# calculate the longth of list
print('the number of the grades is: ',len(grades))



# list and loop

list1 = ['lili','amy','tom']
for i in list1:
    print(i)
    
for name in list1:
    print(f'my name is {name}')
    print(name)
    
    
    
    
# use range function to generate number list
for number in range(1,21):
    print(number)
    


# use simple function to calculate
data = [1,2,3,4,5,6,7,8]
print('the max value in list is:',max(data))
print('the min value in list is: ',min(data))
print('the sum of numbers is: ',sum(data))
print('the number of the numbers is: ',len(data))



# solve some interesting problems
# generate the square of the number in 1-100
numbers = [i*i for i in range(1,101)]
print(numbers)


# generate the square of the even number in 1-100
numbers = [i*i for i in range(1,101) if i % 2 == 0]
print(numbers)

# generate the square of the odd number in 1-100
numbers = [i*i for i in range(1,101) if i % 2 ==1]
print(numbers)
numbers = [i for i in range(1,101)]
print(numbers)


# the slice of the list
numbers = list(range(10))
# from 2 to 5 but not contain 5
print(numbers[2:5])  
# from 0 to 6
print(numbers[:6])  
# from 5 and till to the end
print(numbers[5:])  
# add a parameter of step
print(numbers[6:9:2])
# all number
print(numbers[:]) 




# tuple
student = (1001,'tom',20)
# tuple can not be changed so the data are more safe


