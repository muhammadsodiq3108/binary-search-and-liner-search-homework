birinchi = 0
oxirgi = 0
numbers = [4, 7, 2, 7, 9, 7, 1]
target = 7

for i in range (len(numbers)):
    if numbers[i] == target:
        birinchi = i
    oxirgi = i

print(birinchi)
print(oxirgi)

