data = [3,4,5,6,7,8,6,5,4,3,6,7,6,8,9]

unique = []
for num in data:
    if num not in unique:
        unique.append(num)

print(unique)