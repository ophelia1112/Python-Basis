# dict：
user = {'id':001,'name':'amy','age':18}
print(user['id'])
print(user['name'])

# add key and value
user['height'] = 180
user['family_members'] = 6
print(user)

# loop and iteration
# dict.items()：return tuple
# dict.key()：return keys
# dict.value()：return value

for key,value in user.items():
    print(key,value)
print(user.items())
print(list(user.items()))

for key in user.keys():
    print(key)

for value in user.values():
    print(value)




# dict nested in dict
students = [
    {'id':101,'name':'tom','height':190},
    {'id':110,'name':'amy','height':180},
    {'id':112,'name':'alice','height':179},
]

for student in students:
    id,name,height = student['id'],student['name'],student['height']
    print(f'Student number is {id} and his name is {name} and his height is {height}')

# list nested in list
students = {
    'tom' : ['football','basketball'],
    'amy' : ['badminton'],
    'alice' : ['dance'],
}

for student,habby in students.items():
    print(f'Student name is {student} and habby is {habby}')

# package merging and splitting
students = {
    'tom' : {'id':12,'height':180,'job':'teacher'},
    'amy' : {'id':13,'height':179,'job':'nurse'},
    'alice' : {'id':14,'height':168,'job':'writer'},
}

for name,stock in students.items():
    id,height,job = stock['id'],stock['height'],stock['job']
    print(f'The name of student is {name} and student number is {id} and height is {height} and job is{job}')


# set()
# len(set) calculate the length of set
# set.add(key) add the key
# set.remove(key) delete a key
# set.clear() clean all the set elements

# 练习题：比较难
students = {
    'amy' : ['football','basketball'],
    'alice' : ['basketball','dance'],
    'tom' : ['basketball','dance'],
    'xiaozhao' : ['badminton'],
}
likes = set()
for habbies in students.values():
    for habby in habbies:
        likes.add(habby)
print(likes)
