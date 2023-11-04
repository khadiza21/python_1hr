slist = ["rice", "soup","lentil","beef"]
int_list = [0,2,3,4,4,2]
print(slist)


int_list = [2,3,4,1,4,2,4,5,4,2,4,3]


print(int_list)
print(int_list[5])
print(int_list[-1]) #slicing or getting last index 
print(int_list[1:5]) #here 1 index is start and 5 is the last index here showing   data of index 1 to 4
print(int_list[:5])#showing data from first index to index 5
print(int_list[4:])#showing data from index 4 to last index


max_value = max(int_list)
min_value = min(int_list)
print("Sum of the list is ", sum(int_list))
print("Minimum value of the list ",min_value)
print("Maximum value of the list ", max_value)

#minimum value finding by manuallay
minValue = int_list[0]
for val in int_list:
    if val < max_value:
        max_value = val
print("Minimum value find...",max_value)
