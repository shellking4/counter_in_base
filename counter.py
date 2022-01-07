#!/usr/bin/env python3
import sys
ALLOWED_CHARACTERS_IN_BASE = {
    "two": "01",
    "three": "012",
    "four": "0123",
    "five": "01234",
    "six": "012345",
    "seven": "0123456",
    "eight": "01234567",
    "nine": "012345678",
    "ten": "0123456789",
    "eleven": "0123456789a",
    "twelve": "0123456789ab",
    "thirteen": "0123456789abc",
    "fourteen": "0123456789abcd",
    "fifteen": "0123456789abcde",
    "sixteen": "0123456789abcdef",
    "seventeen": "0123456789abcdefg",
    "eighteen": "0123456789abcdefgh",
    "nineteen": "0123456789abcdefghi",
    "twenty": "0123456789abcdefghij",
    "twenty_one": "0123456789abcdefghijk",
    "twenty_two": "0123456789abcdefghijkl",
    "twenty_three": "0123456789abcdefghijklm",
    "twenty_four": "0123456789abcdefghijklmn",
    "twenty_five": "0123456789abcdefghijklmno",
    "twenty_six": "0123456789abcdefghijklmnop",
    "twenty_seven": "0123456789abcdefghijklmnopq",
    "twenty_eight": "0123456789abcdefghijklmnopqr",
    "twenty_nine": "0123456789abcdefghijklmnopqrs",
    "thirty": "0123456789abcdefghijklmnopqrst",
    "thirty_one": "0123456789abcdefghijklmnopqrstu",
    "thirty_two": "0123456789abcdefghijklmnopqrstuv",
    "thirty_three": "0123456789abcdefghijklmnopqrstuvw",
    "thirty_four": "0123456789abcdefghijklmnopqrstuvwx",
    "thirty_five": "0123456789abcdefghijklmnopqrstuvwxy",
    "thirty_six": "0123456789abcdefghijklmnopqrstuvwxyz",
    "thirty_seven": "0123456789abcdefghijklmnopqrstuvwxyzA",
    "thirty_eight": "0123456789abcdefghijklmnopqrstuvwxyzAB",
    "thirty_nine": "0123456789abcdefghijklmnopqrstuvwxyzABC",
    "fourty": "0123456789abcdefghijklmnopqrstuvwxyzABCD",
    "fourty_one": "0123456789abcdefghijklmnopqrstuvwxyzABCDE",
    "fourty_two": "0123456789abcdefghijklmnopqrstuvwxyzABCDEF",
    "fourty_three": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFG",
    "fourty_four": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGH",
    "fourty_five": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHI",
    "fourty_six": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJ",
    "fourty_seven": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJK",
    "fourty_eight": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL",
    "fourty_nine": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM",
    "fifty": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN",
    "fifty_one": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN0",
    "fifty_two": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP",
    "fifty_three": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ",
    "fifty_four": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR",
    "fifty_five": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS",
    "fifty_six": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST",
    "fifty_seven": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU",
    "fifity_eight": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV",
    "fifity_nine": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW",
    "sixty": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX",
    "sixty_one": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY",
    "sixty_two": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "sixty_three": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNNOPQRSTUVWXY@",
    "sixty_four": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNNOPQRSTUVWXYZ@/",
}

def encode(num,  allowed_characters):
    if num == 0:
        return allowed_characters[0]
    arr = []
    arr_append = arr.append 
    _divmod = divmod 
    base = len(allowed_characters)
    while num:
        num, rem = _divmod(num, base)
        arr_append(allowed_characters[rem])
    arr.reverse()
    return ''.join(arr)

def count_for_base(base_number, pos_number):
    range_stop = pow(base_number, pos_number)
    for i in range(0, range_stop):
        string = ""
        if (base_number == 2):
            string = f'{i:b}'
        if (base_number == 3):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["three"])}'
        if (base_number == 4):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["four"])}'
        if (base_number == 5):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["five"])}'
        if (base_number == 6):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["six"])}'
        if (base_number == 7):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["seven"])}'
        if (base_number == 8):
            string = f'{i:o}'
        if (base_number == 9):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["nine"])}'
        if (base_number == 10):
            string = f'{i:d}'
        if (base_number == 11):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["eleven"])}'
        if (base_number == 12):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["twelve"])}'
        if (base_number == 13):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["thirteen"])}'
        if (base_number == 14):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fourteen"])}'
        if (base_number == 15):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fifteen"])}'
        if (base_number == 16):
            string = f'{i:x}'
        if (base_number == 17):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["seventeen"])}'
        if (base_number == 18):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["eighteen"])}'
        if (base_number == 19):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["nineteen"])}'
        if (base_number == 20):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["twenty"])}'
        if (base_number == 21):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["twenty_one"])}'
        if (base_number == 22):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["twenty_two"])}'
        if (base_number == 23):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["twenty_three"])}'
        if (base_number == 24):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["twenty_four"])}'
        if (base_number == 25):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["twenty_five"])}'
        if (base_number == 26):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["twenty_six"])}'
        if (base_number == 27):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["twenty_seven"])}'
        if (base_number == 28):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["twenty_eight"])}'
        if (base_number == 29):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["twenty_nine"])}'
        if (base_number == 30):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["thirty"])}'
        if (base_number == 31):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["thirty_one"])}'
        if (base_number == 32):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["thirty_two"])}'
        if (base_number == 33):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["thirty_three"])}'
        if (base_number == 34):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["thirty_four"])}'
        if (base_number == 35):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["thirty_five"])}'
        if (base_number == 36):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["thirty_six"])}'
        if (base_number == 37):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["thirty_seven"])}'
        if (base_number == 38):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["thirty_eight"])}'
        if (base_number == 39):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["thirty_nine"])}'
        if (base_number == 40):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fourty"])}'
        if (base_number == 41):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fourty_one"])}'
        if (base_number == 42):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fourty_two"])}'
        if (base_number == 43):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fourty_three"])}'
        if (base_number == 44):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fourty_four"])}'
        if (base_number == 45):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fourty_five"])}'
        if (base_number == 46):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fourty_six"])}'
        if (base_number == 47):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fourty_seven"])}'
        if (base_number == 48):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fourty_eight"])}'
        if (base_number == 49):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fourty_nine"])}'
        if (base_number == 50):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fifty"])}'
        if (base_number == 51):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fifty_one"])}'
        if (base_number == 52):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fifty_two"])}'
        if (base_number == 53):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fifty_three"])}'
        if (base_number == 54):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fifty_four"])}'
        if (base_number == 55):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fifty_five"])}'
        if (base_number == 56):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fifty_six"])}'
        if (base_number == 57):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fifty_seven"])}'
        if (base_number == 58):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fifty_eight"])}'
        if (base_number == 59):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["fifty_nine"])}'
        if (base_number == 60):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["sixty"])}'
        if (base_number == 61):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["sixty_one"])}'
        if (base_number == 62):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["sixty_two"])}'
        if (base_number == 63):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["sixty_three"])}'
        if (base_number == 64):
            string = f'{encode(i, ALLOWED_CHARACTERS_IN_BASE["sixty_four"])}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def proceed():
    args = sys.argv[1:]
    get = False
    if len(args) == 0:
        base_number = input("The base: ")
        positions_number = input("Number of positions: ")
        try:
            base_number = int(base_number)
            positions_number = int(positions_number)
            get = True
        except:
            print("Please, give integers as arguments")
    elif len(args) == 2:
        try:
            base_number = int(args[0])
            positions_number = int(args[1])
            get = True
        except:
            print("Please, give integers as arguments")
    else:
        print("Program needs 2 arguments")
    if get:
        if 2 <= base_number and base_number <= 64:
            count_for_base(base_number, positions_number)
        else:
            print("Please, give a base between 2 and 64.")
proceed()
