i = 0
numbers = []

while i < 6:
    print(f"At the top of i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

i = 0
numbers = []

for i in range(0,6):
    print(f"At the top of the for loop: {i}")
    numbers.append(i)
    
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom of the for loop: {i}")

print("The numbers from the for loop: ")

for num in numbers:
    print(num)
