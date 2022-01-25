"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)

    '''for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")'''

    subjects = []
    for total in input_file:
        first_line = input_file.readline()
        second_line = input_file.readline()
        total = total.strip()
        parts = total.split(',')
        parts[2] = int(parts[2])
        subjects.append(parts)
    return subjects
    input_file.close()


def display_data(data):
    for blank in data:
        print("{} is taught by {} and has {:.0f} students".format(blank[0], blank[1], blank[2]))


main()
