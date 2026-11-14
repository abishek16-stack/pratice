data = [2,34,4,5,5,6,75,4,554,3,2,41,1,34,665,99]

even = []
odd = []

for i in data :
    if i%2 == 0 :
        even.append(i)
        
    else:
        odd.append(i)
        
        
print(even)
print(odd)