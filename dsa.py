my_list = []
#append
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert value
my_list.insert(1, 15)

#extend
my_list.extend(50, 60, 70)

#remove last element
my_list.pop()

#ascending order
my_list.sort()

index_of_30 = my_list.index(30)
print(index_of_30)