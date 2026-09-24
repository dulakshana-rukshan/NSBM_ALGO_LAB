numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers)

num_index = int(input("Enter Value Index:"))

for i in range(num_index,len(numbers)-1):
    numbers[i] = numbers[i + 1]

numbers.pop()
print(numbers)

