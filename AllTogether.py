### Part Four -- your code goes here. 
import random 

number_list = []
n = 10 
for i in range(n):
    numbers = random.randint(1,100)
    number_list.append(numbers)
print(number_list)

l = len(number_list)

while i in number_list:
    calc = numbers % 2
    if calc == 0:
        number_list.remove(i)
    else:
        pass
print(number_list)

#while numbers % 2 != 0:
    #number_list.remove(numbers)
    #print(number_list)