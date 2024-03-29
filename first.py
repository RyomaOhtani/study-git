def determine_zodiac(year):
    zodiac_signs = {
        0: "子(Rat)",
        1: "丑(Ox)",
        2: "寅(Tiger)",
        3: "卯(Rabbit)",
        4: "辰(Dragon)",
        5: "巳(Snake)",
        6: "午(Horse)",
        7: "未(Goat)",
        8: "申(Monkey)",
        9: "酉(Rooster)",
        10: "戌(Dog)",
        11: "亥(Pig)"
    }

    zodiac_index = (year - 4) % 12
    zodiac_sign = zodiac_signs[zodiac_index]
    return zodiac_sign

try:
    birth_year = int(input("Enter your birth year: "))
    zodiac = determine_zodiac(birth_year)
    print("Your zodiac sign is:", zodiac)
except ValueError:
    print("Invalid input. Please enter a valid birth year.")

# 追記しました