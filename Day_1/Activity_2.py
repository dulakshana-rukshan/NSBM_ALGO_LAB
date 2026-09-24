numbers = [10, 20, 30, 40, 50, 60, 70]

num = int(input("Enter Number:"))

num_index = int(input("Enter Value Index:"))

# numbers.insert(num_index,num)
# print(numbers)

#################################################################

numbers.append(0)

for i in range(len(numbers)-1,num_index,-1):
    numbers[i] = numbers[i -1]

numbers[num_index] = num

print(numbers)

