data = []

for i in range(10):
     num = int(input("Enter the value : "))
     data.append(num)

even_count = 0 
odd_count = 0

for i in data:
    if i%2 ==0:
        even_count += 1
        
    elif i%2 ==1 :
        odd_count += 1
        

print(f"Total even is {even_count}")
print(f"Total Odd is {odd_count}")