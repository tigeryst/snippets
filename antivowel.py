vowels = ["a", "e", "i", "o", "u"]


def anti_vowel(text):
    result = []
    for char in text:
        if not char.lower() in vowels:
            result.append(char)
    return "".join(result)


print(anti_vowel("Hey my name is Tiger and I am learning to code"))
