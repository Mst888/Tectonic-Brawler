# bot_logic in original

import random


def sifre_olusturucu(sifre_uzunlugu):
    ogeler = "+-/*!&$#?=@<>"
    sifre = ""

    for i in range(sifre_uzunlugu):
        sifre += random.choice(ogeler)

    return sifre


def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)


def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"
    
def double_letter(str):
    result = ''
    for letter in str:
        result += letter * 2
    return result

def secret_function(a, b):
    return a + b
    print(double_letter("Hello"))                 # HHeelllloo
    print(secret_function(1, 2))                  # 3
    print(secret_function("Hello, ", "world!"))   # Hello, world!
