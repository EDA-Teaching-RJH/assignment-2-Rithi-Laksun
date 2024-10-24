### Part Three -- your code goes here. 

numbers_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

def organise_list():
    numbers_list.sort()
    c = numbers_list.count(1)
    for i in range(c):
        numbers_list.remove(1)
    numbers_list.append(7)
    numbers_list.append(8)
    print(numbers_list)
organise_list()