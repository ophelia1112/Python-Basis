# Input function can help to input information

number = input('Input a number to calculate the square: ')
number = int(number)
print(f'The number you input is {number}, it is the square : {number * number}')

number = input('Please enter into a number: ')
number = int(number)
if number % 2 == 0:
    print(f'The number you input is {number}, an even number.')
else:
    print(f'The number you input is {number}, an odd number')


# practice
number,sum_value = 1,0 
while number <= 100: 
    sum_value += number
    number += 1 
print(sum_value)



# input "quit" to quit
while True:
    fruit = input('Please input your favourite fruit, if you want to quit then enter "quit": ')
    if fruit == 'quit':
        break
    else:
        print(f'You favourite fruit is {fruit}')
        

# example1 calculate the weight
while True:
    print('#' * 20)
    weight = input('Please enter the weight of your package（kg）,if you want to quit then enter "quit":')
    if weight == 'quit':
        break
    else:
        weight = float(weight)
        if weight <= 0:
            print('wrong weight')
            continue
        if weight < 1:
            print('The price is 7')
        elif 1 < weight < 3:
            price = 7 + 2 * weight
            print(price)
        elif weight >= 3:
            price = 7 + 3 * weight
            print(price)
        else:
            print('wrong: ',weight)




# example2 crawl some websites
import time 
web_wait_to_get = ['web1','web2','web3'] 
web_successfully_get = [] 

while web_wait_to_get:
    new_web = web_wait_to_get.pop()
    
    print('crawling web:',new_web)
    time.sleep(1)  
    web_successfully_get.append(new_web)

print('successfully crawled',web_success)
print('wait to be crawled',web_todo)






# game: guess the number
import random
target = random.randint(1,100)
success = False
time = 0
while time <= 10:
    number = input('Input the number you guess: ')
    if not str(number).isnumeric(): 
        print('The item you input not a number, try again')
        continue
    number = int(number) 
    if number == target:
        print('Congratulations, you guessed it!')
        success = True 
        break
    elif number < target:
        print(f'The number you input is {number},too small.')
    else:
        print(f'The number you input is {number},too big.')
    time += 1
else:
    print(f'I am regret that you are wrong, the answer is {target}')


