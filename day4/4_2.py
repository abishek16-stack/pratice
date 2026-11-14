data =[1,2,3,4,55,6,7,8,9]

largest = data[0]

for i in data:
    if i > largest:
        largest = i
        
print(largest)