arr = [3,4,5]

for i in arr:
    arr += arr[list(i)]
    print(arr)  