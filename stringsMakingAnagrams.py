def increaseFrequency(dictionary, char):
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

def number_needed(a, b):
    aChars = {}
    bChars = {}
    for char in a:
        increaseFrequency(aChars, char)
    for char in b:
        increaseFrequency(bChars, char)
    neededDeletions = 0
    for char in aChars:
        if char not in bChars:
            neededDeletions += aChars[char]
        else:
            difference = abs(aChars[char] - bChars[char])
            neededDeletions += difference
    for char in bChars:
        if char not in aChars:
            neededDeletions += bChars[char]
    return neededDeletions

a = input().strip()
b = input().strip()

print(number_needed(a, b))
