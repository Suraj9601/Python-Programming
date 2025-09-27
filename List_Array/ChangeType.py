list = [1, 2, 3, 4, 5, 6, 7]
print("Original List type : ", type(list[0]))
print(list)

new_arr = [float(i) for i in list]
print("New List type : ", type(new_arr[0]))
print(new_arr)
