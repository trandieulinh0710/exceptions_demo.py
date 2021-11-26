# 1
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print("Your name is", name)

# 3
in_file = open("numbers.txt", "r")
first_line = int(in_file.readline())
second_line = int(in_file.readline())
in_file.close()
total = first_line + second_line
print(total)

# 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    all_line = int(line)
    total += all_line
in_file.close()
print(total)
