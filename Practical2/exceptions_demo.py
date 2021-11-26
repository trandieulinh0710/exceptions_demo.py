try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:  # keep asking when user enter 0 for denominator avoid zero division error
        print("Enter none zero for denominator")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur? when user enter float for numerator and denominator
# When will a ZeroDivisionError occur? when denominator is 0
