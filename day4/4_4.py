data = [22,35,67,56,78,76,43,37,99,999]

largest = data[0]

secound_largest = None

for num in data :
    if num > largest:
        secound_largest = largest
        largest = num
        
    elif num > secound_largest and num != largest:
        secound_largest = num
        
        
print(secound_largest)