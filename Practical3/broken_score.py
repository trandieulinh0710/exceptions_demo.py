def main():
    score = float(input("Enter score: "))
    Grade(score)


def Grade(score):
    if score > 100 or score < 0:
        print("Invalid score")
    elif score >= 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    else:
        print("Bad")


main()