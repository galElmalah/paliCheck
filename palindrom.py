"""
checking how many palindroms in a given string
"""


def reverseString(str):
    return str[::-1]


def palindrom(str):
    pali_count = 0
    words = str.split()

    for word in words:
        if word == reverseString(word):#check each word with the same word only reversd
            pali_count+=1
    return pali_count

def main():
    a=input("Enter a string:")
    print(palindrom(a))

main()