# 1
numbers = []
for i in range(5):
    number = int(input(" Number: "))
    numbers.append(number)
print(f" the first number is: {numbers[0]}")
print(f" the last number is: {numbers[4]}")
print(f"    the smallest number is {min(numbers)}")
print(f" the largest number is {max(numbers)}")
average = sum(numbers) / len(numbers)
print(f" the average number is {average}")

# 2
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input(" What's your name? ")
if username in usernames:
    print(" Access granted")
else:
    print(" Access denied")
