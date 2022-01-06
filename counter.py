#!/usr/bin/env python3

import sys


def encode(num, allowed_characters):
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

def count_for_base2(pos_number):
    range_stop = pow(2, pos_number)
    for i in range(0, range_stop):
        string = f'{i:b}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)


def count_for_base3(pos_number):
    allowed_characters = "012"
    range_stop = pow(3, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base4(pos_number):
    allowed_characters = "0123"
    range_stop = pow(4, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)


def count_for_base5(pos_number):
    allowed_characters = "01234"
    range_stop = pow(5, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base6(pos_number):
    allowed_characters = "012345"
    range_stop = pow(6, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base7(pos_number):
    allowed_characters = "0123456"
    range_stop = pow(7, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base8(pos_number):
    range_stop = pow(8, pos_number)
    for i in range(0, range_stop):
        string = f'{i:o}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base9(pos_number):
    allowed_characters = "012345678"
    range_stop = pow(9, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base10(pos_number):
    range_stop = pow(10, pos_number)
    for i in range(0, range_stop):
        string = f'{i:d}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)


def count_for_base11(pos_number):
    allowed_characters = "0123456789a"
    range_stop = pow(11, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base12(pos_number):
    allowed_characters = "0123456789ab"
    range_stop = pow(12, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base13(pos_number):
    allowed_characters = "0123456789abc"
    range_stop = pow(13, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base14(pos_number):
    allowed_characters = "0123456789abcd"
    range_stop = pow(14, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base15(pos_number):
    allowed_characters = "0123456789abcde"
    range_stop = pow(15, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base16(pos_number):
    range_stop = pow(16, pos_number)
    for i in range(0, range_stop):
        string = f'{i:x}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)


def count_for_base17(pos_number):
    allowed_characters = "0123456789abcdefg"
    range_stop = pow(17, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)


def count_for_base18(pos_number):
    allowed_characters = "0123456789abcdefgh"
    range_stop = pow(18, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base19(pos_number):
    allowed_characters = "0123456789abcdefghi"
    range_stop = pow(19, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base20(pos_number):
    allowed_characters = "0123456789abcdefghij"
    range_stop = pow(20, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base21(pos_number):
    allowed_characters = "0123456789abcdefghijk"
    range_stop = pow(21, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)


def count_for_base22(pos_number):
    allowed_characters = "0123456789abcdefghijkl"
    range_stop = pow(22, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base23(pos_number):
    allowed_characters = "0123456789abcdefghijklm"
    range_stop = pow(23, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base24(pos_number):
    allowed_characters = "0123456789abcdefghijklmn"
    range_stop = pow(24, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base25(pos_number):
    allowed_characters = "0123456789abcdefghijklmno"
    range_stop = pow(25, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base26(pos_number):
    allowed_characters = "0123456789abcdefghijklmnop"
    range_stop = pow(26, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base27(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopq"
    range_stop = pow(27, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base28(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqr"
    range_stop = pow(28, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base29(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrs"
    range_stop = pow(29, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base30(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrst"
    range_stop = pow(30, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base31(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstu"
    range_stop = pow(31, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base32(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuv"
    range_stop = pow(32, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base33(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvw"
    range_stop = pow(33, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base34(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwx"
    range_stop = pow(34, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base35(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxy"
    range_stop = pow(35, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base36(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyz"
    range_stop = pow(36, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base37(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzA"
    range_stop = pow(37, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base38(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzAB"
    range_stop = pow(38, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base39(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABC"
    range_stop = pow(39, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base40(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCD"
    range_stop = pow(40, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base41(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDE"
    range_stop = pow(41, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base42(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEF"
    range_stop = pow(42, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base43(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFG"
    range_stop = pow(43, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base44(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGH"
    range_stop = pow(44, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base45(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHI"
    range_stop = pow(45, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base46(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJ"
    range_stop = pow(46, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base47(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJK"
    range_stop = pow(47, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base48(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL"
    range_stop = pow(48, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base49(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM"
    range_stop = pow(49, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base50(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN"
    range_stop = pow(50, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base51(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO"
    range_stop = pow(51, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base52(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP"
    range_stop = pow(52, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base53(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ"
    range_stop = pow(53, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base54(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR"
    range_stop = pow(54, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base55(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS"
    range_stop = pow(55, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base56(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST"
    range_stop = pow(56, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base57(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU"
    range_stop = pow(57, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base58(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV"
    range_stop = pow(58, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base59(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW"
    range_stop = pow(59, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base60(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX"
    range_stop = pow(60, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base61(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY"
    range_stop = pow(61, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base62(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    range_stop = pow(62, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base63(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@"
    range_stop = pow(63, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

def count_for_base64(pos_number):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@/"
    range_stop = pow(64, pos_number)
    for i in range(0, range_stop):
        string = f'{encode(i, allowed_characters)}'
        if (len(string) < pos_number):
            missing_pos = pos_number - len(string)
            for p in range(0, missing_pos):
                string = f'0{string}'
        print(string)

base_number = int(sys.argv[1])
pos_number = int(sys.argv[2])
if (base_number == 2):
    count_for_base2(pos_number)
if (base_number == 3):
    count_for_base3(pos_number)
if (base_number == 4):
    count_for_base4(pos_number)
if (base_number == 5):
    count_for_base5(pos_number)
if (base_number == 6):
    count_for_base6(pos_number)
if (base_number == 7):
    count_for_base7(pos_number)
if (base_number == 8):
    count_for_base8(pos_number)
if (base_number == 9):
    count_for_base9(pos_number)
if (base_number == 10):
    count_for_base10(pos_number)
if (base_number == 11):
    count_for_base11(pos_number)
if (base_number == 12):
    count_for_base12(pos_number)
if (base_number == 13):
    count_for_base13(pos_number)
if (base_number == 14):
    count_for_base14(pos_number)
if (base_number == 15):
    count_for_base15(pos_number)
if (base_number == 16):
    count_for_base17(pos_number)
if (base_number == 17):
    count_for_base17(pos_number)
if (base_number == 18):
    count_for_base18(pos_number)
if (base_number == 19):
    count_for_base19(pos_number)
if (base_number == 20):
    count_for_base20(pos_number)
if (base_number == 21):
    count_for_base21(pos_number)
if (base_number == 22):
    count_for_base22(pos_number)
if (base_number == 23):
    count_for_base23(pos_number)
if (base_number == 24):
    count_for_base24(pos_number)
if (base_number == 25):
    count_for_base25(pos_number)
if (base_number == 26):
    count_for_base26(pos_number)
if (base_number == 27):
    count_for_base27(pos_number)
if (base_number == 28):
    count_for_base28(pos_number)
if (base_number == 29):
    count_for_base29(pos_number)
if (base_number == 30):
    count_for_base30(pos_number)
if (base_number == 31):
    count_for_base31(pos_number)
if (base_number == 32):
    count_for_base32(pos_number)
if (base_number == 33):
    count_for_base33(pos_number)
if (base_number == 34):
    count_for_base34(pos_number)
if (base_number == 35):
    count_for_base35(pos_number)
if (base_number == 36):
    count_for_base36(pos_number)
if (base_number == 37):
    count_for_base37(pos_number)
if (base_number == 38):
    count_for_base38(pos_number)
if (base_number == 39):
    count_for_base39(pos_number)
if (base_number == 40):
    count_for_base40(pos_number)
if (base_number == 41):
    count_for_base41(pos_number)
if (base_number == 42):
    count_for_base42(pos_number)
if (base_number == 43):
    count_for_base43(pos_number)
if (base_number == 44):
    count_for_base44(pos_number)
if (base_number == 45):
    count_for_base45(pos_number)
if (base_number == 46):
    count_for_base46(pos_number)
if (base_number == 47):
    count_for_base47(pos_number)
if (base_number == 48):
    count_for_base48(pos_number)
if (base_number == 49):
    count_for_base49(pos_number)
if (base_number == 50):
    count_for_base50(pos_number)
if (base_number == 51):
    count_for_base51(pos_number)
if (base_number == 52):
    count_for_base52(pos_number)
if (base_number == 53):
    count_for_base53(pos_number)
if (base_number == 54):
    count_for_base54(pos_number)
if (base_number == 55):
    count_for_base55(pos_number)
if (base_number == 56):
    count_for_base56(pos_number)
if (base_number == 57):
    count_for_base57(pos_number)
if (base_number == 58):
    count_for_base58(pos_number)
if (base_number == 59):
    count_for_base59(pos_number)
if (base_number == 60):
    count_for_base60(pos_number)
if (base_number == 61):
    count_for_base61(pos_number)
if (base_number == 62):
    count_for_base62(pos_number)
if (base_number == 63):
    count_for_base63(pos_number)
if (base_number == 64):
    count_for_base64(pos_number)
