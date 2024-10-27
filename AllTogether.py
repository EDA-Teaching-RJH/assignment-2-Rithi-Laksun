### Part Four -- your code goes here. 
import random
number_list = []
init_number_range = 10
first_rand_num = 1
last_rand_num = 100

def init_random_num():
  for i in range(init_number_range):
    numbers = random.randint(first_rand_num,last_rand_num)
    number_list.append(numbers)
  return number_list

def remove_even_number(number_list, i_number):
  while(i_number  < len(number_list)):
    result = [ev for ev in number_list if ev %2 !=0]
    return result
  exit()

print("The random list: ", init_random_num())  #prints the original lists
print("New list: ", remove_even_number(number_list,0))  #prints the new list without even numbers
