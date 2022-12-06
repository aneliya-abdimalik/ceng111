a = input()
number = list(a)
if '?' in number:
    if number[0] == '?':
    # 6 is an inverse multiplicative of 2 in mod 11
        if number[5] == 'X':
            d0 = (6 * (10 - 3 * int(number[1]) - 5 * int(number[2]) - 7 * int(number[3]))) % 11
            print(str(d0) + number[1] + number[2] + number[3] + number[4] + 'X')
        else:
            d0 = (6 * (int(number[5]) - 3 * int(number[1]) - 5 * int(number[2]) - 7 * int(number[3]))) % 11
            print(str(d0) + number[1] + number[2] + number[3] + number[4] + number[5])
    if number[1] == '?':
    # 4 is an inverse multiplicative of 3 in mod 11
        if number[5] == 'X':
            d1 = (4 * (10 - 2 * int(number[0]) - 5 * int(number[2]) - 7 * int(number[3]))) % 11
            print(number[0] + str(d1) + number[2] + number[3] + number[4] + 'X')
        else:
            d1 = (4 * (int(number[5]) - 2 * int(number[0]) - 5 * int(number[2]) - 7 * int(number[3]))) % 11
            print(number[0] + str(d1) + number[2] + number[3] + number[4] + number[5])

    if number[2] == "?":
         # 9 is an inverse multiplicative of 5 in mod 11
        if number[5] == 'X':
            d2 = (9 * (10 - 2 * int(number[0]) - 3 * int(number[1]) - 7 * int(number[3]))) % 11
            print(number[0] + number[1] + str(d2) + number[3] + number[4] + 'X')
        else:
            d2 = (9 * (int(number[5]) - 2 * int(number[0]) - 3 * int(number[1]) - 7 * int(number[3]))) % 11
            print(number[0] + number[1] + str(d2) + number[3] + number[4] + number[5])

    if number[3] == "?":
        # 8 is an inverse multiplicative of 7 in mod 11
        if number[5] == 'X':
            d3= (8 * (10 - 2 * int(number[0]) - 3 * int(number[1]) - 5 * int(number[2]))) % 11
            print(number[0] + number[1] + number[2] + str(d3) + number[4] + 'X')
        else:
            d3 = (8 * (int(number[5]) - 2 * int(number[0]) - 3 * int(number[1]) - 5 * int(number[2]))) % 11
            print(number[0] + number[1] + number[2] + str(d3) + number[4] + number[5])

    if number[5] == '?':
        d5 = (2 * int(number[0]) + 3 * int(number[1]) + 5 * int(number[2]) + 7 * int(number[3])) % 11
        if d5 == 10:
            print(number[0] + number[1] + number[2] + number[3] + number[4] + 'X')
        else:
            print(number[0] + number[1] + number[2] + number[3] + number[4] + str(d5))

else:
    check = (2 * int(number[0]) + 3 * int(number[1]) + 5 * int(number[2]) + 7 * int(number[3])) % 11
    if number[5]!='X' and check == int(number[5]):
        print("VALID")
    elif number[5]=='X' and check == 10:
        print("VALID")
    else:
        print("INVALID")
