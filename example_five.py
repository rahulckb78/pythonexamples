numbers = [1, 3, 5, 3, 7, 1, 9, 5, 7]
print(list(dict.fromkeys(numbers)))

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = [] and [unique_list.append(x) for x in my_list if x not in unique_list]
print(unique_list) 


