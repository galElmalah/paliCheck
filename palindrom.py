"""
checking how many palindroms in a given string
"""


def reverseString(str):
    return str[::-1]


def palindrom(str):
    pali_count = 0
    words = [str.split()]

    for word in words:
        if word == reverseString(word):
            pali_count+=1
    return pali_count
