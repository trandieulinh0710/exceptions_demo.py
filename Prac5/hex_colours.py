COLOURS_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "	#b0bf1a", "AliceBlue": "#f0f8ff",
                "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "	#9966cc",
                "AntiqueWhite": "	#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc"}

colours = input("Please enter a color's name: ")
while colours != "":
    if colours in COLOURS_CODE:
        print(f"{colours} is {COLOURS_CODE[colours]}")
    else:
        print("Invalid colours")
    colours = input("Please enter a color's name: ")
